from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from api.utils.token_manager import TokenManager

# Use HTTPBearer instead of OAuth2PasswordBearer
auth_scheme = HTTPBearer()

async def verify_token(request: Request, credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    """Middleware to verify the token from Authorization header."""
    if not credentials:
        raise HTTPException(status_code=401, detail="Missing authorization token")

    token = credentials.credentials  # Extract token
    try:
        decoded_payload = TokenManager.validate_token(token)
        request.state.user = decoded_payload  # Attach user to request
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
