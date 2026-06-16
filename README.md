# Projeto de Integração Supabase + Z-API

Este repositório contém a solução desenvolvida para o desafio de estágio em Python. O objetivo principal da aplicação é conectar-se a um banco de dados **Supabase**, ler uma lista restrita de contatos e realizar o disparo de mensagens personalizadas via **Z-API** (WhatsApp).

## Decisões Técnicas e Arquitetura

O código foi construído priorizando **simplicidade, legibilidade e organização**, evitando overengineering (como abstrações desnecessárias) e focando em entregar um código limpo e coeso.

* **Separação de Responsabilidades:** A aplicação está modularizada dentro do diretório `src/`. Temos `config/` para o controle de variáveis de ambiente, `services/` para isolar a comunicação com as APIs (Supabase e Z-API), e `utils/` para funções auxiliares de instrumentação.
* **Segurança e Boas Práticas:** Utilização do `python-dotenv` para impedir o acoplamento de credenciais ao código. Todo o fluxo depende de variáveis locais. O código também implementa fail-fast na inicialização caso falte alguma variável obrigatória.
* **Resiliência e Tratamento de Erros:** O envio de mensagens via `requests` possui `timeout` explícito e tratamento de falhas HTTP (`raise_for_status()`). O fluxo principal (`main.py`) engloba um tratamento de erro global para evitar que a aplicação encerre de forma não controlada.
* **Sanitização de Dados:** Mesmo que os telefones estejam armazenados com formatação visual no banco de dados (ex: `+55 11 99999-8888`), a aplicação possui uma camada simples de sanitização usando Regex para enviar apenas dígitos à Z-API, respeitando o padrão esperado pelo provedor.
* **Limitadores:** Respeitando os requisitos do projeto, a consulta ao banco limita ativamente a paginação a 3 registros por vez para evitar gargalos ou custos indesejados.

## Como testar a aplicação

Para executar o orquestrador localmente:

1. Clone o repositório e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows: .\venv\Scripts\activate
   # No Linux/Mac: source venv/bin/activate
   ```

2. Instale as dependências mínimas requeridas:
   ```bash
   pip install -r requirements.txt
   ```

3. Na raiz do projeto, crie o arquivo `.env` contendo suas credenciais de teste para ambas as plataformas:
   ```env
   SUPABASE_URL=sua_url
   SUPABASE_KEY=sua_chave_anon
   ZAPI_INSTANCE=sua_instancia
   ZAPI_TOKEN=seu_token
   ```

4. Execute o script principal:
   ```bash
   python main.py
   ```
*(Nota: O Supabase deve conter uma tabela chamada `contacts` com as colunas textuais `name` e `phone` para que a integração funcione perfeitamente).*
