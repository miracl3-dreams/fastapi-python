from api.ai.ai_model import load_model, generate_response

# Load AI Model once at startup
model = load_model()

def get_ai_response(user_input: str) -> str:
    """
    Processes user input and returns an AI-generated response.
    """
    return generate_response(model, user_input)
