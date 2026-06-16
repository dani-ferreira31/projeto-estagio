import sys
import re
from src.config.settings import validate_settings
from src.utils.logger import get_logger
from src.services.supabase_service import get_contacts
from src.services.zapi_service import send_message

logger = get_logger(__name__)

def clean_phone_number(phone: str) -> str:
    # Remove qualquer caractere que não seja dígito
    return re.sub(r'\D', '', phone)

def main():
    logger.info("Inicializando a aplicação...")
    
    try:
        # 1. Carregar e validar configurações
        validate_settings()
        logger.info("Configurações validadas com sucesso.")
        
        # 2 e 3. Buscar contatos limitando a 3
        contacts = get_contacts()
        
        if not contacts:
            logger.info("Nenhum contato para processar. Encerrando.")
            return

        for contact in contacts:
            # 4. Montar mensagem personalizada
            name = contact.get('name', 'Cliente')
            raw_phone = contact.get('phone', '')
            
            if not raw_phone:
                logger.warning(f"Contato {name} não possui número de telefone. Pulando.")
                continue
                
            clean_phone = clean_phone_number(raw_phone)
            message = f"Olá, {name}! Esta é uma mensagem de teste do nosso sistema integrado."
            
            # 5 e 6. Enviar mensagem e registrar logs
            success = send_message(clean_phone, message)
            if not success:
                logger.warning(f"Falha registrada ao enviar para {name} ({clean_phone}).")
                
        logger.info("Processamento finalizado com sucesso.")
            
    except ValueError as ve:
        logger.error(f"Erro de configuração: {ve}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Erro global inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
