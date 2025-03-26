from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.task_ai_agent_service import suggest_task

class AIAgentController:
    """Controller for AI-powered task functionalities"""

    async def generate_task_suggestion(self, idea: str):
        """Generates a task suggestion using AI."""
        try:
            return suggest_task(idea)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")

    # async def summarize_task_description(self, description: str):
    #     """Summarizes a task description using AI."""
    #     try:
    #         return summarize_task(description)
    #     except Exception as e:
    #         raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")

    # async def get_task_priority(self, description: str):
    #     """Estimates task priority using AI."""
    #     try:
    #         return estimate_task_priority(description)
    #     except Exception as e:
    #         raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")
