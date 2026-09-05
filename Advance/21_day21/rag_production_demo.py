import os
import numpy as np
from openai import OpenAI
from agents import set_tracing_disabled

# 1. Initialize official OpenAI client pointing to LMStudio
client = OpenAI(
    api_key="your_openrouter_api_key", 
    base_url="http://localhost:1234/v1"  # Retargeting local workstations if needed
)

set_tracing_disabled(True)


# 2. In-Memory Enterprise Knowledge Base (Unstructured Chunks)
documents = [
    "Grading Policy: Midterm exams account for 30%, homework assignments 20%, and the final engineering project 50%.",
    "Office Hours: Professor Deepak conducts technical office hours on Tuesdays and Thursdays from 2:00 PM to 4:00 PM in Room 302.",
    "Late Submission Policy: Deliverables submitted within 24 hours past deadline incur an automatic 10% grade deduction. Zero submissions accepted thereafter.",
    "Prerequisites: Students must complete CSE (Intro to Systems Programming) with a grade of C or higher prior to enrollment."
]

# 3. Vector Operations and Embedding Interfaces
def get_embedding(text: str) -> list[float]:
    """Transforms arbitrary text sequences into 1536-dimensional dense vectors."""
    response = client.embeddings.create(
        model="text-embedding-bge-small-en-v1.5", # Use text embedding models
        input=text
    )
    return response.data[0].embedding

def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """Evaluates geometric cosine similarity: cos(theta) = (a . b) / (||a|| * ||b||)"""
    a = np.array(vec_a, dtype=np.float32)
    b = np.array(vec_b, dtype=np.float32)
    norm_product = np.linalg.norm(a) * np.linalg.norm(b)
    if norm_product == 0:
        return 0.0
    return float(np.dot(a, b) / norm_product)

# 4. Ingestion Pipeline: Build Vector Space Index
print("[Ingestion] Generating dense embeddings across document chunks...")
# doc_embeddings = [get_embedding(doc) for doc in documents] # Convert to normal loop
doc_embeddings = []

for doc in documents:
    doc_embeddings.append(get_embedding(doc))

print(f"[Ingestion] Completed. Indexed {len(doc_embeddings)} vectors in memory.\n")

# 5. Production RAG Execution Pipeline
def rag_query(user_question: str) -> str:
    # Step A: RETRIEVAL - Project query into latent space & find nearest neighbor
    query_vector = get_embedding(user_question)
    # similarities = [cosine_similarity(query_vector, doc_vec) for doc_vec in doc_embeddings]
    similarities = []
    for doc_vec in doc_embeddings:
        similarities.append(cosine_similarity(query_vector, doc_vec))
    
    best_idx = int(np.argmax(similarities))
    best_similarity = similarities[best_idx]
    retrieved_chunk = documents[best_idx]

    print(f"Query: {user_question}")
    print(f"Nearest Neighbor Chunk: Index {best_idx} (Cosine Similarity: {best_similarity:.4f})")
    print(f"Retrieved Passage: {retrieved_chunk}\n")

    # Step B: AUGMENTATION - Format grounded system constraints
    system_prompt = (
        "You are an authoritative enterprise academic assistant. "
        "Synthesize responses strictly and exclusively from the provided context. "
        "If the requested information is absent from the context, explicitly state "
        "'I do not have sufficient information in the provided documentation to answer this question.'"
    )
    user_prompt = f"Context:\n{retrieved_chunk}\n\nQuestion: {user_question}"

    # Step C: GENERATION - Grounded completion
    completion = client.chat.completions.create(
        model="qwen2.5-0.5b-instruct-mlx",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.0,  # Greedy decoding for strict reproducibility
        # max_tokens=20 # you can play with this and above
    )
    return completion.choices[0].message.content

# 6. Execute Live Test Queries
if __name__ == "__main__":
    # Test 1: Zero Lexical Overlap Query (Semantic match)
    # q1 = "When can I meet with the instructor in person?"
    # res1 = rag_query(q1)
    # print(f"[Model Generation]:\n{res1}\n")
    # print("=" * 70 + "\n")

    # Test 2: Out-Of-Domain Boundary Query (Hallucination resistance test)
    q2 = "I did not completed assignment how can I get affected?"
    res2 = rag_query(q2)
    print(f"[Model Generation]:\n{res2}\n")