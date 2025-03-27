from fastapi import Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from api.utils.token_manager import TokenManager

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def verify_token(request: Request, token: str = Depends(oauth2_scheme)):
    try:
        # Validate the access token
        decoded_payload = TokenManager.validate_token(token)
        request.state.user = decoded_payload
    except ValueError as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
