from typing import Generator
from sqlalchemy.orm import Session
from database.session import SessionLocal

def get_db()-> Generator[Session, None, None]:
    db = SessionLocal() #create a new session
    try:
        yield db #yield the session to the caller
    finally:
        db.close() #close the session when done
    """
    # -> Generator[Session, None, None] -type hint that this function returns a 
    # generator that yields a Session object and does not return anything when it is done.
    """