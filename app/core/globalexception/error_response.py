from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import field_validator
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi.exceptions import HTTPException

FIELD_ERROR_MESSAGES = {
    "first_name": "First name is missing",
    "last_name": "Last name is missing",
    "email": "Email address is missing",
    "phone": "Phone number is missing"
}


def format_validation_errors(exc: RequestValidationError):
    error_map = {}
    for err in exc.errors():
        loc = err.get("loc", [])
        if "body" in loc:
            field = loc[-1]
            msg = err["msg"]
            if msg.lower() == "field required":
                error_map[field] = FIELD_ERROR_MESSAGES.get(field, f"{field} is missing")
            else:
                error_map[field] = msg  # <- Custom message from @field_validator
    return error_map

def validation_exception_handler(request:Request, exec: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "status": False,
            "message": "Validation Error",
            "errors": format_validation_errors(exec)
           
        }
    )
   
    