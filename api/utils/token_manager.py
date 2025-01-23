from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Union, Dict, Any
from api.config.config import config


class TokenManager:
    """
    Utility class for managing JWT access and refresh tokens using python-jose.
    """

    @staticmethod
    def generate_access_token(payload: Union[str, Dict[str, Any]]) -> str:
        """
        Generate a JWT access token with a given payload.

        Args:
            payload (Union[str, Dict[str, Any]]): The payload for the token.

        Returns:
            str: The generated JWT access token.
        """
        secret = config["key"]["secret"]
        expires_in = int(config["key"]["expiresIn"])  # Token expiration in seconds
        expiration = datetime.utcnow() + timedelta(seconds=expires_in)

        # Add expiration time to payload
        if isinstance(payload, dict):
            payload["exp"] = expiration
        else:
            payload = {"exp": expiration, "data": payload}

        return jwt.encode(payload, secret, algorithm="HS256")

    @staticmethod
    def generate_refresh_token(payload: Union[str, Dict[str, Any]]) -> str:
        """
        Generate a JWT refresh token with a given payload.

        Args:
            payload (Union[str, Dict[str, Any]]): The payload for the token.

        Returns:
            str: The generated JWT refresh token.
        """
        secret = config["key"]["refreshSecret"]
        expires_in = int(config["key"]["refreshExpiresIn"])  # Token expiration in seconds
        expiration = datetime.utcnow() + timedelta(seconds=expires_in)

        # Add expiration time to payload
        if isinstance(payload, dict):
            payload["exp"] = expiration
        else:
            payload = {"exp": expiration, "data": payload}

        return jwt.encode(payload, secret, algorithm="HS256")

    @staticmethod
    def validate_token(token: str) -> Dict[str, Any]:
        """
        Validate and decode an access token.

        Args:
            token (str): The JWT access token to validate.

        Returns:
            Dict[str, Any]: The decoded payload.

        Raises:
            ValueError: If the token is invalid or expired.
        """
        secret = config["key"]["secret"]
        try:
            return jwt.decode(token, secret, algorithms=["HS256"])
        except JWTError as e:
            raise ValueError(f"Access token validation failed: {str(e)}")

    @staticmethod
    def validate_refresh_token(token: str) -> Dict[str, Any]:
        """
        Validate and decode a refresh token.

        Args:
            token (str): The JWT refresh token to validate.

        Returns:
            Dict[str, Any]: The decoded payload.

        Raises:
            ValueError: If the token is invalid or expired.
        """
        secret = config["key"]["refreshSecret"]
        try:
            return jwt.decode(token, secret, algorithms=["HS256"])
        except JWTError as e:
            raise ValueError(f"Refresh token validation failed: {str(e)}")
