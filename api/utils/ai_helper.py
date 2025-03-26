from llama_cpp import Llama
import os

# Load Llama model (update path to your local .gguf model)
MODEL_PATH = "models/llama-3.2-1b.Q4_K_M.gguf"

# Initialize Llama model
llm = Llama(model_path=MODEL_PATH, n_ctx=512)

async def suggest_task(idea: str) -> str:
    """
    Generate a task name and description using Llama 3.2.
    """
    prompt = f"Suggest a task name and description based on this idea: {idea}"
    
    output = llm(prompt, max_tokens=100, echo=False)
    
    return output["choices"][0]["text"].strip()
