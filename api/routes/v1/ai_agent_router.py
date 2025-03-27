from fastapi import APIRouter, Depends
from api.services.ai_agent_service import AIAgentService

router = APIRouter()

@router.post("/chat")
async def chat_with_ai(prompt: str, ai_service: AIAgentService = Depends()):
    response = ai_service.get_ai_response(prompt)
    return {"response": response}
