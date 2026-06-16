# Projeto Python - Estágio

Este projeto é uma aplicação simples em Python desenvolvida para integrar o **Supabase** (leitura de contatos) e a **Z-API** (envio de mensagens no WhatsApp). O objetivo é demonstrar organização, uso de boas práticas e simplicidade.

## Tecnologias Utilizadas

- Python 3.x
- Supabase (SDK Oficial)
- Requests (Comunicação com a Z-API)
- Python-dotenv (Gerenciamento de variáveis de ambiente)

## Estrutura do Banco de Dados (Supabase)

Antes de rodar a aplicação, crie uma tabela chamada `contacts` no seu projeto do Supabase.

**Esquema SQL:**
```sql
create table contacts (
  id uuid default gen_random_uuid() primary key,
  name text not null,
  phone text not null
);

-- Insira alguns dados de teste
insert into contacts (name, phone) values 
('João Silva', '+55 81 99999-8888'),
('Maria Oliveira', '+55 11 98888-7777');
```

## Instalação e Configuração

1. **Clone ou baixe o projeto**.

2. **Crie um ambiente virtual e ative-o:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configuração de Variáveis de Ambiente:**
Renomeie o arquivo `.env.example` para `.env` e preencha com suas credenciais:
```env
SUPABASE_URL=sua_url_aqui
SUPABASE_KEY=sua_chave_aqui
ZAPI_INSTANCE=sua_instancia_aqui
ZAPI_TOKEN=seu_token_aqui
```

## Execução

Após configurar as variáveis de ambiente e o banco de dados, execute o arquivo principal:

```bash
python main.py
```
