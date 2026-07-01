import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load variables from the .env file
load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or Key missing. Check your .env file!")

supabase: Client = create_client(url, key)