# inspect_env.py
from dotenv import dotenv_values
import os

# This reads the file directly without touching os.environ
parsed = dotenv_values('.env')
print("Parsed from .env:", parsed)

# Now load into os.environ
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env', override=True)
print("After load_dotenv, os.environ['DPM_DB_URL']:", os.getenv("DPM_DB_URL"))