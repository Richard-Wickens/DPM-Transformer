from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv(override=True)
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# import models 
from api.models import mTableCell, mHierarchy, mHierarchyNode

def init_db():
    SQLModel.metadata.create_all(engine)
    print("✅ Tables created")

if __name__ == "__main__":
    init_db()