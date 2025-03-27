from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.ai_agent_service import AIAgentService
from api.utils.database import get_db

class AIAgentController:
    def __init__(self):
        self.ai_service = AIAgentService()

    async def suggest_task(self, task_description: str, db: AsyncSession = Depends(get_db)):
        """Generates AI-powered suggestions for a given task description."""
        suggestion = await self.ai_service.suggest_task_improvements(task_description)
        if not suggestion:
            raise HTTPException(status_code=400, detail="Failed to generate task suggestion.")
        return {"suggestion": suggestion}
