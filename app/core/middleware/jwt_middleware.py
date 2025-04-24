from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from core.jwt.jwt_utils import verify_token

EXCLUDE_PATHS = ["/api/auth/login", "/api/employee/create"]

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Check if the request path is in the excluded paths
        if request.url.path in EXCLUDE_PATHS:
            print("Excluding path:", request.url.path)
            response = await call_next(request)
            return response
        #add jwt token validation logic here
        token = request.headers.get("X-Auth-Token")
        if not token:
            return JSONResponse(status_code=401, content={"message": "Missing token"})
        
        decoded=verify_token(token)
        if not decoded:
            return JSONResponse(status_code=401, content={"message": "Invalid token"})
        response = await call_next(request)
        return response



    