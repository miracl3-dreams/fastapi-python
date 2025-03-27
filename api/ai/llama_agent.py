import subprocess

class LlamaAgent:
    def __init__(self, model_name="llama3.2:1b"):
        self.model_name = model_name

    def generate_response(self, prompt: str) -> str:
        try:
            result = subprocess.run(
                ["ollama", "run", self.model_name, prompt],
                capture_output=True,
                text=True
            )
            return result.stdout.strip()
        except Exception as e:
            return f"Error generating response: {str(e)}"
