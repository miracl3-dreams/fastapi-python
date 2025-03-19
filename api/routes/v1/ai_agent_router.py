from fastapi import APIRouter, HTTPException
from api.services.ai_agent_service import get_ai_response 

router = APIRouter()

@router.post("/predict")
async def ai_predict(input_text: str):
    """
    AI Agent endpoint to process user input and return a response from Ollama.
    """
    try:
        response = get_ai_response(input_text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI processing failed: {str(e)}")
