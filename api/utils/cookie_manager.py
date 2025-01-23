from fastapi import Response, Request
from typing import Optional
from api.config.config import config


class CookieManager:
    """
    A utility class for managing HTTP cookies in FastAPI applications.
    Provides methods for setting, retrieving, and deleting cookies.
    """

    @staticmethod
    def set_cookie(
        response: Response,
        key: str,
        value: str,
        max_age: int = 60 * 60 * 24 * 7,  # Default to 7 days
        httponly: bool = True,
        samesite: str = "Strict",
        secure: Optional[bool] = None,
    ):
        """
        Set a cookie in the HTTP response.

        Args:
            response (Response): The FastAPI response object.
            key (str): The name of the cookie.
            value (str): The value of the cookie.
            max_age (int, optional): The maximum age of the cookie in seconds. Defaults to 7 days.
            httponly (bool, optional): Whether the cookie is HTTP-only. Defaults to True.
            samesite (str, optional): The SameSite policy for the cookie ('Strict', 'Lax', or 'None'). Defaults to 'Strict'.
            secure (bool, optional): Whether the cookie is secure. Defaults to True in production environments.
        """
        if secure is None:
            secure = config["app"]["env"] == "production"

        response.set_cookie(
            key=key,
            value=value,
            max_age=max_age,
            httponly=httponly,
            samesite=samesite,
            secure=secure,
        )

    @staticmethod
    def get_cookie(request: Request, key: str) -> Optional[str]:
        """
        Retrieve the value of a cookie from the HTTP request.

        Args:
            request (Request): The FastAPI request object.
            key (str): The name of the cookie to retrieve.

        Returns:
            Optional[str]: The value of the cookie if it exists, or None if it does not.
        """
        return request.cookies.get(key) or None

    @staticmethod
    def delete_cookie(
        response: Response,
        key: str,
        httponly: bool = True,
        samesite: str = "Strict",
        secure: Optional[bool] = None,
    ):
        """
        Delete a cookie from the HTTP response.

        Args:
            response (Response): The FastAPI response object.
            key (str): The name of the cookie to delete.
            httponly (bool, optional): Whether the cookie is HTTP-only. Defaults to True.
            samesite (str, optional): The SameSite policy for the cookie ('Strict', 'Lax', or 'None'). Defaults to 'Strict'.
            secure (bool, optional): Whether the cookie is secure. Defaults to True in production environments.
        """
        if secure is None:
            secure = config["app"]["env"] == "production"

        response.delete_cookie(
            key=key,
            httponly=httponly,
            samesite=samesite,
            secure=secure,
        )
