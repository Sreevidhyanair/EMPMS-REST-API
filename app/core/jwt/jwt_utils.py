#generate/ create the token
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError  

#constants
SECRET_KEY="your_secret_key"  # Replace with your actual secret key
ALGORITHM="HS256"  # Algorithm used for encoding the JWT
ACCESS_TOKEN_EXPIRE_MINUTES=5  # Token expiration time in minutes
   

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        print(f"expires_delta: {expires_delta}")
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    else:
        ACCESS_TOKEN_EXPIRE_MINUTES = 1  # Default expiration time
        print(f"ACCESS_TOKEN_EXPIRE_MINUTES: {ACCESS_TOKEN_EXPIRE_MINUTES}")
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def verify_token(token:str):
    """
    Verify the JWT token and return the payload if valid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None  # Token is invalid or expired
    except Exception as e:
        print(f"An error occurred while verifying the token: {e}")
        return None
