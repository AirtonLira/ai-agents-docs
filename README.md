# AI Agents

Um projeto que implementa agentes de IA para auxiliar em tarefas pesquisa de documentos web e responder o usuário de acordo com a pergunta relevante, utilizando LangChain e OpenAI.

### Sobre o Projeto

Este projeto implementa um assistente de programação que pode ajudar desenvolvedores com duas tarefas principais:
- Consultar e explicar documentações técnicas de forma simplificada
- Formatar código Python automaticamente usando o Black

### Estrutura do Projeto

O projeto é construído usando Poetry para gerenciamento de dependências e possui a seguinte estrutura:

```
ai-agents/
├── agents.py        # Implementação principal dos agentes
├── pyproject.toml   # Configuração do projeto e dependências
└── poetry.lock      # Lock file com versões específicas das dependências
```

### Funcionalidades

O sistema possui duas ferramentas principais:

1. **Documentation Tool**: Recebe uma URL de documentação e uma pergunta, e retorna explicações simplificadas sobre o conteúdo da documentação.

2. **Black Formatter Tool**: Recebe o caminho de um arquivo Python e aplica a formatação Black automaticamente.

### Como Usar

1. Instale as dependências:
```bash
poetry install
```

2. Configure suas variáveis de ambiente (crie um arquivo .env):
```
OPENAI_API_KEY=sua_chave_aqui
```

3. Execute o programa:
```bash
poetry run python agents.py
```

4. Faça perguntas ao agente. Por exemplo:
- "Pode formatar o arquivo main.py usando o Black?"
- "Pode explicar como funciona a função create_engine do SQLAlchemy?"

### Dependências Principais

- langchain: Framework para construção de aplicações com LLMs
- openai: Integração com modelos GPT da OpenAI
- black: Formatador de código Python
- python-dotenv: Gerenciamento de variáveis de ambiente
- beautifulsoup4: Parsing de HTML para extração de documentação


### Notas

- O projeto utiliza o modelo GPT-3.5-turbo da OpenAI
- É necessário ter uma chave de API válida da OpenAI
- O formatador Black precisa estar instalado no ambiente Poetry

---

Desenvolvido por Airton Lira (@airtonlira)
Linkedln: https://www.linkedin.com/in/airton-lira-junior-6b81a661/