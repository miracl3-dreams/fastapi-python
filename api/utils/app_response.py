from fastapi.responses import JSONResponse
from api.config.config import config  
class AppResponse:
    @staticmethod
    def send_success(
        *,
        data: any,
        message: str = "",
        code: int = 200,
        total_results: int = None,
    ) -> JSONResponse:
        """
        Send a successful response with optional data and total results.

        Args:
            data (any): The data to include in the response.
            message (str): The success message.
            code (int): The HTTP status code (default is 200).
            total_results (int): Optional total results for paginated data.

        Returns:
            JSONResponse: A structured JSON response.
        """
        response_content = {
            "status": "success",
            "message": message,
            "data": data,
            "code": code,
        }

        if total_results is not None:
            response_content["totalResults"] = total_results

        return JSONResponse(content=response_content, status_code=code)

    @staticmethod
    def send_error(
        *,
        data: any,
        message: str,
        code: int,
    ) -> JSONResponse:
        """
        Send an error response, customizing the message based on the environment.

        Args:
            data (any): The data to include in the response (typically None).
            message (str): The error message.
            code (int): The HTTP status code.

        Returns:
            JSONResponse: A structured JSON response.
        """
   

    
        env = config["app"]["env"]

        # Mask internal server errors in non-development environments
        response_message = (
            "Internal Server Error" if env != "development" and code == 500 else message
        )

        response_content = {
            "status": "error",
            "message": response_message,
            "data": data,
            "code": code,
        }

        return JSONResponse(content=response_content, status_code=code)
