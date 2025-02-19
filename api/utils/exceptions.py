from fastapi import HTTPException, status

class EmailAlreadyExistsException(HTTPException):
    def __init__(self, message="An admin with this email already exists."):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=message)

class ResourceNotFoundException(HTTPException):
    def __init__(self, resource: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource} not found."
        )
        
