import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

def validate_settings():
    missing_vars = []
    if not SUPABASE_URL: missing_vars.append("SUPABASE_URL")
    if not SUPABASE_KEY: missing_vars.append("SUPABASE_KEY")
    if not ZAPI_INSTANCE: missing_vars.append("ZAPI_INSTANCE")
    if not ZAPI_TOKEN: missing_vars.append("ZAPI_TOKEN")
    
    if missing_vars:
        raise ValueError(f"Variáveis de ambiente ausentes: {', '.join(missing_vars)}. Verifique seu arquivo .env.")
