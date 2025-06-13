from dotenv import load_dotenv
import os

#from dotenv import load_dotenv
import os

DPM_DB_URL = os.getenv("DPM_DB_URL")
API_HOST  = os.getenv("API_HOST", "127.0.0.1")
API_PORT  = int(os.getenv("API_PORT", 8000))