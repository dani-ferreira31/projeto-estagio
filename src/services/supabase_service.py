from supabase import create_client, Client
from src.config.settings import SUPABASE_URL, SUPABASE_KEY
from src.utils.logger import get_logger

logger = get_logger(__name__)

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def get_contacts():
    logger.info("Conectando ao Supabase para buscar contatos...")
    try:
        supabase: Client = get_supabase_client()
        response = supabase.table("contacts").select("*").limit(3).execute()
        contacts = response.data
        logger.info(f"{len(contacts)} contatos encontrados.")
        return contacts
    except Exception as e:
        logger.error(f"Falha ao buscar contatos no Supabase: {e}")
        return []
