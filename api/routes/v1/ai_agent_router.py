from fastapi import APIRouter
from api.controllers.ai_agent_controller import AIAgentController

router = APIRouter()
ai_agent_controller = AIAgentController()

@router.get("/suggest-task/{idea}")
async def get_suggested_task(idea: str):
    """AI-powered endpoint for task suggestions."""
    suggestion = await ai_agent_controller.generate_task_suggestion(idea)
    return suggestion

@router.get("/summarize-task/{description}")
async def summarize_task(description: str):
    """AI-powered endpoint to summarize task descriptions."""
    summary = await ai_agent_controller.summarize_task_description(description)
    return {"summary": summary}

@router.get("/task-priority/{description}")
async def get_task_priority(description: str):
    """AI-powered endpoint to estimate task priority."""
    priority = await ai_agent_controller.get_task_priority(description)
    return {"priority": priority}
