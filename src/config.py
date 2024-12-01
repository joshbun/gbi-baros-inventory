from dotenv import load_dotenv
import os

load_dotenv()

# Load environment variables
API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")