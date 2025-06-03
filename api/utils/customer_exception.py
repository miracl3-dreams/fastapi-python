from fastapi import HTTPException

def not_found_exception(entity: str):
    raise HTTPException(status_code=404, detail=f"{entity} not found")
