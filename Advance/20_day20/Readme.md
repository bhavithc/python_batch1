# Lesson Plan: Architectural Design Patterns for AI Agents
## 1. Learning Objectives & Core Concepts

[Common workflow patterns for AI agents | Claude by Anthropic](https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them)
[Building Effective AI Agents – Demystifying the Anthropic ...](https://www.linkedin.com/pulse/building-effective-ai-agents-demystifying-anthropic-white-ajay-taneja-erprc)
[Build AI Agents: 40 Key Lessons from Anthropic's Masterclass](https://www.maryammiradi.com/blog/build-ai-agents-anthropic-lessons) [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

## Learning Objectives

* Distinguish between deterministic workflows and autonomous agentic loops in production systems.
* Implement four foundational structural design patterns using an asynchronous python client framework.
* Troubleshoot production failures such as context bloat, tool output instability, and infinite routing loops.
* Reconfigure client infrastructure to run workloads locally via LM Studio endpoints. [1, 2, 3, 4, 5, 6] 

## Workflows vs. Agents
When building production systems with Large Language Models (LLMs), a primary architectural boundary must be drawn between pre-orchestrated workflows and autonomous agents: [2, 7] 

* Workflows: These are systems where LLMs move through pre-defined, deterministic paths. Control flow is handled by standard code loops, conditional checks, or hardcoded routers. Workflows trade autonomous flexibility for exceptional predictability, predictable execution costs, lower latencies, and trivial debugging. [2, 6, 7] 
* Agents: These are systems where the LLM autonomously dictates its own control flow and iterates via an internal environment loop. The model decides which tools to call, evaluates the environment's feedback, and terminates only when it judges the goal complete. This offers extreme flexibility but introduces non-deterministic execution paths, risk of compounding errors, and unpredictable latency profiles. [1, 7, 8] 

Production Rule of Thumb: Always favor the simplest architectural construct. Begin with direct prompts, scale to structured workflows, and introduce full agentic loops only when a problem domain requires dynamic tool sequences that cannot be anticipated programmatically. [1, 9, 10, 11] 
For full context on these frameworks, consult the [Anthropic Engineering Guide](https://www.anthropic.com/engineering/building-effective-agents) and their breakdown of [Common Workflow Patterns](https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them).
[1, 12] 

## 2. Structural Design Patterns: Serial Chain

## Pattern 1: The Serial (Chain) Pattern
The serial chain executes a linear sequence where a complex goal is decomposed into discrete, single-purpose steps. The output of Step $N$ is cleanly injected as context into Step $N+1$, ensuring each model call remains highly specialized. [4, 13, 14] 

```python
import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
# Client configuration pointing to OpenRouter
open_ai_client = AsyncOpenAI(
    api_key="your_openrouter_api_key", 
    base_url="https://openrouter.ai"
)
chat_model = OpenAIChatCompletionsModel(
    model="meta-llama/llama-3.3-70b-instruct",
    openai_client=open_ai_client
)
# Step 1 Agent: Focuses solely on core structural layout
architect_agent = Agent(
    name="System Architect",
    instructions="You are a software architect. Given a requirement, output ONLY a flat list of microservices needed. Do not write markdown, code blocks, or introductions.",
    model=chat_model
)
# Step 2 Agent: Uses the previous architectural list to draft specific interfaces
api_designer_agent = Agent(
    name="API Designer",
    instructions="You take a list of microservices and write gRPC proto3 definitions for them. Output valid protobuf syntax only.",
    model=chat_model
)
async def main():
    user_requirement = "Build an e-commerce platform with a shopping cart, payment processing, and inventory tracking."
    
    print("--- Executing Step 1: Architecting Services ---")
    step1_result = await Runner.run(architect_agent, user_requirement)
    services_list = step1_result.final_output
    print(services_list)
    
    print("\n--- Executing Step 2: Generating gRPC Interfaces ---")
    # Clean pipeline handoff: Pass output directly as next input context
    step2_result = await Runner.run(api_designer_agent, services_list)
    print(step2_result.final_output)
if __name__ == "__main__":
    asyncio.run(main())
```

## 3. Structural Design Patterns: Parallel (Fork-Join)

## Pattern 2: The Parallel Pattern
The parallel design pattern fans out a query to multiple independent LLM instances concurrently to analyze separate concerns. It then aggregates their independent outputs into a single, unified context block programmatically. [4, 15] 

```python
import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
open_ai_client = AsyncOpenAI(
    api_key="your_openrouter_api_key", 
    base_url="https://openrouter.ai"
)
chat_model = OpenAIChatCompletionsModel(
    model="meta-llama/llama-3.3-70b-instruct",
    openai_client=open_ai_client
)
# Specialist Workers
security_expert = Agent(
    name="Security Analyst",
    instructions="Analyze the given system idea for potential security vulnerabilities. Be brief and concise.",
    model=chat_model
)
cloud_expert = Agent(
    name="Cloud Infrastructure Architect",
    instructions="Provide a targeted AWS infrastructure roadmap for the given system idea. Be brief.",
    model=chat_model
)
# Synthesizing Aggregator
aggregator_agent = Agent(
    name="Technical Coordinator",
    instructions="You are given a security review and a cloud layout. Synthesize them into an executive summary.",
    model=chat_model
)
async def main():
    target_idea = "A real-time ride-sharing application using peer-to-peer data links."
    
    print("--- Running Concurrent Parallel Analysis ---")
    # Fan-out: Execute concurrent tasks using asyncio.gather
    security_task = Runner.run(security_expert, target_idea)
    cloud_task = Runner.run(cloud_expert, target_idea)
    
    security_res, cloud_res = await asyncio.gather(security_task, cloud_task)
    
    # Fan-in: Concat context for unified aggregation
    combined_context = f"Security Analysis:\n{security_res.final_output}\n\nCloud Layout:\n{cloud_res.final_output}"
    
    print("--- Merging Coordinated Results ---")
    final_summary = await Runner.run(aggregator_agent, combined_context)
    print(final_summary.final_output)
if __name__ == "__main__":
    asyncio.run(main())
```

## 4. Structural Design Patterns: Router Pattern
## Pattern 3: The Router Pattern
A specialized routing model evaluates input queries against distinct classification boundaries, directing the payload to the single most qualified downstream agent setup. This avoids polluting prompts with conflicting instructions. [4, 13, 16] 

```python
import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
open_ai_client = AsyncOpenAI(
    api_key="your_openrouter_api_key", 
    base_url="https://openrouter.ai"
)
chat_model = OpenAIChatCompletionsModel(
    model="meta-llama/llama-3.3-70b-instruct",
    openai_client=open_ai_client
)
router_agent = Agent(
    name="Language Classifier",
    instructions="Classify the incoming programming query. Respond with exactly one token: 'python' or 'cpp'.",
    model=chat_model
)
python_specialist = Agent(
    name="Python Guru",
    instructions="You are an expert Python developer. Resolve this task using clean PEP8 compliant code syntax.",
    model=chat_model
)
cpp_specialist = Agent(
    name="C++ Core Engineer",
    instructions="You are a performance systems engineer. Resolve this using Modern C++ guidelines without allocations.",
    model=chat_model
)
async def route_and_execute(user_query: str):
    # Route step
    route_decision = await Runner.run(router_agent, user_query)
    chosen_path = route_decision.final_output.strip().lower()
    print(f"\nRouter Decision: {chosen_path}")
    
    # Dynamic execution path selection
    if "python" in chosen_path:
        result = await Runner.run(python_specialist, user_query)
    elif "cpp" in chosen_path:
        result = await Runner.run(cpp_specialist, user_query)
    else:
        return "Routing error: unknown path layout execution requested."
        
    return result.final_output
async def main():
    q1 = "How do I implement custom memory arenas using placement new?"
    q2 = "Write a fast asynchronous list comprehension to slice generator data."
    
    print(await route_and_execute(q1))
    print(await route_and_execute(q2))
if __name__ == "__main__":
    asyncio.run(main())
```

## 5. Structural Design Patterns: Evaluator-Optimizer Loop

## Pattern 4: The Evaluator-Optimizer Loop
This pattern acts as a quality control engine. A generator model creates an artifact, which an evaluator model scores against predefined rubrics. If the artifact fails to meet the criteria, the evaluation metrics are fed back to the generator as instructions for iterative improvement. [4, 13] 

```python
import asyncio
import jsonfrom openai 
import AsyncOpenAIfrom agents import Agent, Runner, OpenAIChatCompletionsModel
open_ai_client = AsyncOpenAI(
    api_key="your_openrouter_api_key", 
    base_url="https://openrouter.ai"
)
chat_model = OpenAIChatCompletionsModel(
    model="meta-llama/llama-3.3-70b-instruct",
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
```

## 6. Failure Modes & Local LM Studio Transition

## Common Failures in Production Agent Systems

   1. Infinite Routing Loops: In evaluator loops or open-ended tool environments, models can get trapped repeating identical responses or flipping infinitely between two choices. Mitigation: Always enforce an external hardcoded loop counter limit to break execution safely. [1, 5] 
   2. Context Window Pollution: Passing raw multi-turn session logs down a chain stacks tokens exponentially, raising costs and degrading processing accuracy. Mitigation: Explicitly strip metadata and compress outputs into short summaries at agent task boundaries. [1, 16] 
   3. Tool Output Instability: Agent loops depend heavily on tool feedback string predictability. A tool error message layout change can cause an autonomous model to misinterpret the state. Mitigation: Wrap all custom execution environments in rigid schema handling and string cleanups. [1, 17] 

------------------------------
## Switching Infrastructure: Local Setup via LM Studio
To run classroom demonstrations locally without internet connectivity or OpenRouter token spend, retarget your initialization block. LM Studio creates an OpenAI-compatible local server on port 1234. [6] 

```python
import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
# 1. Point client directly to your local workstation port
local_lm_studio_client = AsyncOpenAI(
    api_key="lm-studio-dummy-key",         # LM Studio bypasses authentication checks
    base_url="http://localhost:1234/v1"     # Default local instance server port endpoint
)
# 2. Initialize the wrapper layer
# The 'model' parameter can be set to any identifier string; 
# LM Studio automatically uses whatever model is currently loaded in the active UI memory.
local_chat_model = OpenAIChatCompletionsModel(
    model="local-loaded-model", 
    openai_client=local_lm_studio_client
)
# 3. Instantiate agents normally
local_math_agent = Agent(
    name="Math tutor",
    instructions="You are a precise mathematics teacher. Output answers cleanly without markdown.",
    model=local_chat_model
)
async def main():
    print("Executing query on local workstation inference engine...")
    result = await Runner.run(local_math_agent, "What is 45 plus 55?")
    print(f"Result: {result.final_output}")
if __name__ == "__main__":
    asyncio.run(main())
```

## Classroom Verification Checklist for Students

   1. Launch LM Studio on the local machine.
   2. Download an instruction-following model (e.g., Qwen2.5-7B-Instruct or Llama-3-8B-Instruct).
   3. Click the Local Server icon on the left-hand navigation pane.
   4. Select the model target from the top dropdown selection, and click Start Server.
   5. Run the python script directly from your terminal.

------------------------------
## Design Framework Reference Matrix

| Pattern Name | Control Setup | Primary Use Case | Risk / Tradeoff |
|---|---|---|---|
| Serial Chain | Fixed Code Pipeline | Ordered multi-stage structured tasks | Pipeline breaks if any early step drops context |
| Parallelization | Concurrent Gather | Fast analysis of independent components | Concurrency bursts spike local memory or rate limits |
| Routing | Conditional Branching | Handling inputs with variable intentions | Misclassification isolates requests completely |
| Evaluator-Optimizer | Dynamic Feedback Loop | High-quality text generation, editing, code optimization | Introduces higher latency and token loops |

For additional details on multi-agent alignment and verification loops, refer to the [Anthropic Human-Agent Collaboration Review](https://claude.com/blog/building-effective-human-agent-teams).
[18] 

[1] [https://www.anthropic.com](https://www.anthropic.com/engineering/building-effective-agents)
[2] [https://www.linkedin.com](https://www.linkedin.com/pulse/building-effective-ai-agents-demystifying-anthropic-white-ajay-taneja-erprc)
[3] [https://github.com](https://github.com/machinedge/building-effective-agents/blob/main/building-effective-agents.md)
[4] [https://blog.devgenius.io](https://blog.devgenius.io/why-anthropics-building-effective-agents-raises-the-bar-and-which-agent-patterns-to-avoid-e60a143940df)
[5] [https://www.anthropic.com](https://www.anthropic.com/research/multiagent-systems)
[6] [https://www.youtube.com](https://www.youtube.com/watch?v=JEERoZQbG9k&t=1291)
[7] [https://www.linkedin.com](https://www.linkedin.com/posts/linasbeliunas_this-anthropic-engineer-wrote-the-monumental-activity-7459243921077059584-i1qZ)
[8] [https://www.anthropic.com](https://www.anthropic.com/research/trustworthy-agents)
[9] [https://www.anthropic.com](https://www.anthropic.com/engineering/harness-design-long-running-apps)
[10] [https://www.linkedin.com](https://www.linkedin.com/posts/lewisowain_if-you-want-to-build-ai-systems-learn-these-activity-7441092702097559552-eDHz)
[11] [https://www.linkedin.com](https://www.linkedin.com/posts/hanane-d-algo-trader_anthropic-just-dropped-a-guide-about-common-activity-7435670294540992513-IoDz)
[12] [https://claude.com](https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them)
[13] [https://medium.com](https://medium.com/@vasundra.srinivasan/building-effective-ai-agents-a-practical-application-92e1e1537f64)
[14] [https://github.com](https://github.com/cloudflare/agents/blob/main/guides/anthropic-patterns/README.md)
[15] [https://www.anthropic.com](https://www.anthropic.com/engineering/building-effective-agents)
[16] [https://www.anthropic.com](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
[17] [https://www.anthropic.com](https://www.anthropic.com/engineering/writing-tools-for-agents)
[18] [https://claude.com](https://claude.com/blog/building-effective-human-agent-teams)
