import os
import json
import numpy as np
import tiktoken
from typing import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from openai import AsyncOpenAI

# -------------------------------------------------------------
# 1. Environment & Comparable Baseline Cloud Pricing
# -------------------------------------------------------------
LMSTUDIO_BASE_URL = os.getenv("LMSTUDIO_BASE_URL", "http://localhost:1234/v1")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-bge-small-en-v1.5")
COMPLETION_MODEL = os.getenv("COMPLETION_MODEL", "qwen2.5-0.5b-instruct-mlx")

# Reference cloud costs per 1,000,000 tokens for ROI/Savings tracking
CLOUD_PRICING = {
    "embedding_per_1m": 0.02,       # Cloud embedding equivalent
    "prompt_per_1m": 0.15,          # Cloud prompt input equivalent
    "completion_per_1m": 0.60      # Cloud completion token equivalent
}

# Initialize Async client targeting local workstation daemon
client = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY", "local-lmstudio"),
    base_url=LMSTUDIO_BASE_URL
)
tokenizer = tiktoken.get_encoding("cl100k_base")

# -------------------------------------------------------------
# 2. Knowledge Base & Vector Utility Functions
# -------------------------------------------------------------
documents = [
    "Grading Policy: Midterm exams account for 30%, homework assignments 20%, and the final engineering project 50%.",
    "Office Hours: Professor Ada conducts technical office hours on Tuesdays and Thursdays from 2:00 PM to 4:00 PM in Room 302.",
    "Late Submission Policy: Deliverables submitted within 24 hours past deadline incur an automatic 10% grade deduction. Zero submissions accepted thereafter.",
    "Prerequisites: Students must complete CS101 (Intro to Systems Programming) with a grade of C or higher prior to enrollment."
]
doc_embeddings: list[np.ndarray] = []

async def get_embedding(text: str) -> np.ndarray:
    res = await client.embeddings.create(model=EMBEDDING_MODEL, input=text)
    return np.array(res.data[0].embedding, dtype=np.float32)

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    norm_product = np.linalg.norm(a) * np.linalg.norm(b)
    if norm_product == 0:
        return 0.0
    return float(np.dot(a, b) / norm_product)

# -------------------------------------------------------------
# 3. Application Lifespan (Pre-compute document embeddings once)
# -------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    global doc_embeddings
    print(f"[Startup] Indexing knowledge base against LMStudio at {LMSTUDIO_BASE_URL}...")
    doc_embeddings = []
    for doc in documents:
        emb = await get_embedding(doc)
        doc_embeddings.append(emb)
    print(f"[Startup] Successfully indexed {len(doc_embeddings)} chunks in memory.\n")
    yield

app = FastAPI(title="Local RAG Agent API", version="1.0.0", lifespan=lifespan)

class QueryRequest(BaseModel):
    question: str = Field(
        ..., 
        json_schema_extra={"example": "When can I meet with the instructor in person?"}
    )

# class QueryRequest(BaseModel):
#     question: str = Field(..., example="When can I meet with the instructor in person?")

# -------------------------------------------------------------
# 4. Asynchronous SSE Generator with Integrated Cost Telemetry
# -------------------------------------------------------------
async def stream_rag_pipeline(question: str) -> AsyncGenerator[str, None]:
    # Step A: RETRIEVE
    query_emb = await get_embedding(question)
    similarities = [cosine_similarity(query_emb, doc_vec) for doc_vec in doc_embeddings]
    best_idx = int(np.argmax(similarities))
    best_score = similarities[best_idx]
    retrieved_chunk = documents[best_idx]

    # Token tracking for Retrieval
    emb_tokens = len(tokenizer.encode(question))
    emb_cost_equiv = (emb_tokens / 1_000_000) * CLOUD_PRICING["embedding_per_1m"]

    # Emit Retrieval Metadata Event
    retrieval_meta = {
        "event": "retrieval",
        "data": {
            "matched_chunk": retrieved_chunk,
            "similarity": round(best_score, 4),
            "embedding_tokens": emb_tokens
        }
    }
    yield f"data: {json.dumps(retrieval_meta)}\n\n"

    # Step B: AUGMENT
    system_prompt = (
        "You are an authoritative enterprise academic assistant. "
        "Synthesize responses strictly and exclusively from the provided context. "
        "If absent, state: 'I do not have sufficient information in the provided documentation.'"
    )
    user_prompt = f"Context:\n{retrieved_chunk}\n\nQuestion: {question}"
    prompt_tokens = len(tokenizer.encode(system_prompt + user_prompt))

    # Step C: GENERATE (Token Streaming)
    stream = await client.chat.completions.create(
        model=COMPLETION_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.0,
        max_tokens=120,
        stream=True
    )

    completion_tokens = 0
    async for chunk in stream:
        if chunk.choices and len(chunk.choices) > 0:
            delta = chunk.choices[0].delta.content
            if delta:
                completion_tokens += len(tokenizer.encode(delta))
                token_event = {"event": "token", "data": delta}
                yield f"data: {json.dumps(token_event)}\n\n"

    # Step D: Final Telemetry Event
    prompt_cost_equiv = (prompt_tokens / 1_000_000) * CLOUD_PRICING["prompt_per_1m"]
    completion_cost_equiv = (completion_tokens / 1_000_000) * CLOUD_PRICING["completion_per_1m"]
    total_savings_usd = emb_cost_equiv + prompt_cost_equiv + completion_cost_equiv

    metrics_payload = {
        "event": "metrics",
        "data": {
            "local_inference_cost_usd": 0.0,
            "tokens_processed": {
                "embedding_tokens": emb_tokens,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": emb_tokens + prompt_tokens + completion_tokens
            },
            "equivalent_cloud_cost_saved_usd": round(total_savings_usd, 8)
        }
    }
    yield f"data: {json.dumps(metrics_payload)}\n\n"
    yield "data: [DONE]\n\n"

@app.post("/api/v1/chat")
async def chat_endpoint(request: QueryRequest):
    return StreamingResponse(
        stream_rag_pipeline(request.question),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )

@app.get("/healthz")
async def health():
    return {"status": "healthy", "chunks_indexed": len(doc_embeddings)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

# How to test 
# Run python3 app.py
# in other terminal run 
"""
curl -N -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "When can I meet with the instructor in person?"}'
"""