from dotenv import load_dotenv
import os

print("CWD =", os.getcwd())
print("Files in CWD:", os.listdir(os.getcwd()))

# Load .env from current directory explicitly
load_dotenv(dotenv_path=os.path.join(os.getcwd(), '.env'))

print("DATABASE_URL =", os.getenv("DATABASE_URL"))
print("API_HOST  =", os.getenv("API_HOST"))
print("API_PORT  =", os.getenv("API_PORT"))