#create engine performing ddl worlk or complete db structure creation
#sessionmaker
#declarative base

#to create the engine : db_url
#to form db_url : dialect+driver://username:password@host:port/dbname
from sqlalchemy import create_engine
from core.config.db_config import load_env_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
db_config = load_env_config()

#validate keys
required_keys = ["DB_HOST", "DB_PORT", "DB_NAME", "DB_USERNAME", "DB_PASSWORD"]
missing_keys = [key for key in required_keys if not db_config.get(key)]
if missing_keys:
    raise ValueError(f"Missing environment variables: {', '.join(missing_keys)}")

#build db url
db_url = f"postgresql://{db_config['DB_HOST']}:{db_config['DB_PORT']}/{db_config['DB_NAME']}?user={db_config['DB_USERNAME']}&password={db_config['DB_PASSWORD']}"
engine = create_engine("".join(db_url), echo=True)
#create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#declarative base
Base = declarative_base() 





