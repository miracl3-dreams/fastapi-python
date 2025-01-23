from fastapi.responses import JSONResponse
from utils.app_response import AppResponse
from utils.custom_error import AuthError, NotFoundError, ValidationError

def handle_exception(error: Exception) -> JSONResponse:
    """
    Handle exceptions raised in the application and return a structured response.

    Args:
        error (Exception): The exception to handle.

    Returns:
        JSONResponse: A structured JSON response based on the error.
    """
    # Default response details
    response_message = str(error)
    status_code = 500

    # Check if the error is a custom error
    if isinstance(error, (AuthError, ValidationError, NotFoundError)):
        response_message = error.message
        status_code = error.status_code

    # Send the error response using AppResponse
    return AppResponse.send_error(
        data=None,
        message=response_message,
        code=status_code,
    )
