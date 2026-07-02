import os
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client, Client

# Manually find the exact path to your .env file on your Desktop
env_path = Path(r"C:\Users\samir\OneDrive\Desktop\ai-attendance-project-app\.env")

# Force load it
load_dotenv(dotenv_path=env_path)

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError(f"Could not find your .env file at: {env_path}")

supabase: Client = create_client(url, key)