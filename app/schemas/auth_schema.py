from pydantic import BaseModel, EmailStr, field_validator

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    def validate_password(cls, value):
        # Password between 6 and 8 characters
        if len(value) <= 6 or len(value) >= 8:
            raise ValueError('Password must be between 6 and 8 characters long')
        return value
    
