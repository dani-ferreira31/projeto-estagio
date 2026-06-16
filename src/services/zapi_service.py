import requests
from src.config.settings import ZAPI_INSTANCE, ZAPI_TOKEN
from src.utils.logger import get_logger

logger = get_logger(__name__)

def send_message(phone: str, message: str) -> bool:
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"
    payload = {
        "phone": phone,
        "message": message
    }
    
    try:
        logger.info(f"Enviando mensagem via Z-API para {phone}...")
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"Mensagem enviada com sucesso para {phone}.")
        return True
    except requests.exceptions.Timeout:
        logger.error(f"Timeout ao tentar enviar mensagem para {phone}.")
        return False
    except requests.exceptions.HTTPError as err:
        logger.error(f"Erro HTTP na Z-API para {phone}: {err}")
        return False
    except requests.exceptions.RequestException as e:
        logger.error(f"Falha na comunicação com a Z-API para {phone}: {e}")
        return False
