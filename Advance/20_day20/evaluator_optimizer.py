import asyncio
import json
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

set_tracing_disabled(True)

# Client configuration pointing to OpenRouter
open_ai_client = AsyncOpenAI(
    api_key="your_openrouter_api_key", 
    base_url="http://localhost:1234/v1"
)

chat_model = OpenAIChatCompletionsModel(
    model="llama-3.2-1b-instruct",
    openai_client=open_ai_client
)

generator_agent = Agent(
    name="Code Refiner",
    instructions="Optimize the execution speed of the provided function code. Return only the optimized code block.",
    model=chat_model
)

evaluator_agent = Agent(
    name="Quality Assurer",
    instructions=(
        "Analyze the provided code optimization. Ensure it introduces zero undefined behavior or safety regressions. "
        "Format your answer strictly as a JSON object with two keys: "
        "'approved' (boolean true/false) and 'feedback' (string detailing exact issues found)."
        "Just provide the answer in pure JSON no markdown, nothing  "
    ),
    model=chat_model
)

async def main():
    original_code = "void process(int* arr, int n) { for(int i=0; i<n; i++) { arr[i] = arr[i] * 2; } }"
    current_draft = original_code
    max_loops = 3
    
    for iteration in range(max_loops):
        print(f"\n--- Optimization Loop Run {iteration + 1} ---")
        
        # Quality Evaluation step
        eval_result = await Runner.run(evaluator_agent, f"Code to review:\n{current_draft}")
        print(eval_result)
        raw_json = eval_result.final_output
        
        try:
            clean_json = raw_json.strip().removeprefix("n```json").removesuffix("```").strip()
            review_report = json.loads(clean_json)
        except Exception:
            print("Failed to cleanly parse structured evaluator JSON. Aborting loop safely.")
            break

        is_passing = review_report.get("approved", False)
        feedback = review_report.get("feedback", "No validation logs provided.")
        
        if is_passing:
            print(">>> Success: Evaluator approved code draft.")
            break
            
        print(f">>> Rejected by Evaluator. Feedback: {feedback}")
        
        # Optimization step based on feedback
        generation_prompt = f"Original:\n{original_code}\nCurrent:\n{current_draft}\nFeedback to fix:\n{feedback}"
        gen_result = await Runner.run(generator_agent, generation_prompt)
        current_draft = gen_result.final_output
        
    print("\n--- Final Polished Compilation ---")
    print(current_draft)
if __name__ == "__main__":
    asyncio.run(main())