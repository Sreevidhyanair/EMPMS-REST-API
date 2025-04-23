from fastapi import Request,HTTPException
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import HTTP_404_NOT_FOUND


def get_object_or_404(obj, name="Resource"):
    if not obj:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"{name} not found")
    return obj

#Global exception handler for 404s and others
async def not_found_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == HTTP_404_NOT_FOUND:
        path_parts = request.url.path.split("/")
        entity=path_parts[2] if path_parts else "Resource"
        entity_name=entity.replace("-"," ").replace("_"," ").capitalize()

        return JSONResponse(
            status_code=HTTP_404_NOT_FOUND,
            content={
                "status": False,
                "message": f"{entity_name} not found at path {request.url.path}",
                "path": request.url.path
                
            }
        )
        
    