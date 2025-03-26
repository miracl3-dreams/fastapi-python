import re
from api.ai.ai_model import load_model, generate_response
from api.utils.database import get_db
from api.models.task_model import Task

# Load AI Model once at startup
model = load_model()

def suggest_task(idea: str) -> dict:
    """
    Uses AI to suggest a task name and description.
    """
    prompt = f"Suggest a task related to: {idea}. Provide a task name and a short description."
    response = generate_response(model, prompt).strip()

    # Use regex to extract task_name and task_description
    match = re.match(r'\"?(.*?)\"?\n\nDescription:\n\n(.+)', response, re.DOTALL)
    if match:
        task_name = match.group(1).strip()
        task_description = match.group(2).strip()
    else:
        task_name = "Unknown Task"
        task_description = response if response else "No valid AI-generated description."

    return {"task_name": task_name, "task_description": task_description}

def save_ai_task(task_name: str, task_description: str):
    """
    Saves AI-generated tasks into the database (if it doesn't already exist).
    """
    db = get_db()
    existing_task = db.query(Task).filter(Task.task_name == task_name).first()
    
    if not existing_task:
        new_task = Task(task_name=task_name, task_description=task_description, status=False)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
    
    db.close()
