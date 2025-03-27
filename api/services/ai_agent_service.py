from api.ai.llama_agent import LlamaAgent

class AIAgentService:
    def __init__(self):
        self.agent = LlamaAgent()

    async def get_ai_response(self, prompt: str) -> str:
        return self.agent.generate_response(prompt)
    
    async def suggest_task_improvements(self, task_description: str) -> str:
        prompt = f"Analyze and improve this task: {task_description}"
        return self.agent.generate_response(prompt)
    
    
