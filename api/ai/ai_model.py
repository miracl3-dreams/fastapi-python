import ollama

def load_model():
    """
    Load the llama3.2:1b model.
    """
    model_name = "llama3.2:1b"
    return model_name

def generate_response(model, user_input: str) -> str:
    """
    Generates a response from the Ollama AI model.
    """
    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": user_input}])
        return response.get("message", {}).get("content", "No response generated.")
    except Exception as e:
        return f"Error: {str(e)}"
