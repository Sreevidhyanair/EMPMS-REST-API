from pydantic import BaseModel, EmailStr,field_validator
from schemas.role_schema import RolesResponse

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str

    @field_validator('email')
    def validate_email(cls, value):
        if not value.endswith('@ibm.com'):
            print(f"Invalid email domain")
            raise ValueError('Email must end with ibm.com')
        return value
      

    @field_validator('phone')
    def validate_phone(cls, value):
        if not value.isdigit():
            print(f"Invalid phone number")
            
            raise ValueError('Phone number must contain only digits') 
        return value

    class Config:
        orm_mode = True #Enable ORM mode to work with SQLAlchemy models
   
class EmployeeCreate(EmployeeBase):
    password: str
    role_id: int
    department_id: int
    
    
    @field_validator('password')
    def validate_password(cls, value):
        #password between 6 and 8 characters
        if len(value) <=6 or len(value) >= 8:         
            raise ValueError('Password must be 6 to 8 characters long')
        return value



class EmployeeIDResponse(EmployeeBase):
    employee_id: int



    
class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
        # Enable ORM mode to work with SQLAlchemy models

class EmployeeTokenResponse(EmployeeResponse):
    access_token: str
    token_type:str

