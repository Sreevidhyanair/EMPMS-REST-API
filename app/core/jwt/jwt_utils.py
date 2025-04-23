#generate/ create the token
from datetime import datetime, timedelta
from jose import jwt, JWTError  

#constants
SECRET_KEY="your_secret_key"  # Replace with your actual secret key
ALGORITHM="HS256"  # Algorithm used for encoding the JWT
ACCESS_TOKEN_EXPIRE_MINUTES=30  # Token expiration time in minutes

def create_access_token(data: dict, expires_delta: timedelta|None=None):
    """
    Create a JWT access token with an expiration time. 
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
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
