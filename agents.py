# Criar uma ferramenta para pesquisar documentações.
# Criar uma ferramenta para formatar o nosso código.
# Criar o nosso agente que vai utilizar essas ferramentas.

import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from scrapper import get_text_from_url
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent


load_dotenv()

def get_response_from_openai(message: str):

    llm = ChatOpenAI(model_name="gpt-3.5-turbo")

    response = llm.invoke(message)

    return response

@tool
def documentation_tool(url: str, question:str) -> str:
    """ This tool receives as input the URL from the documentation and the question about the documentation that the user want to be answered """

    context = get_text_from_url(url)

    message = [
        SystemMessage(content="You're a helpful programming assistant that must explain programming library documentations to users as simples as possible"),
        HumanMessage(content=f"Documentation: {context} \n\n Question: {question}")
    ]


    response = get_response_from_openai(message)

    return response
@tool
def black_formatter_tool(code: str) -> str:
    """ This tool receives as input a file system path to a python script file and runs black formatter to format the file's python code """

    try:
        os.system(f"poetry run black {code}")
        return "Done!"
    except:
        return "Error! formatter"
    
toolkit = [documentation_tool, black_formatter_tool]

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

prompt = ChatPromptTemplate.from_messages([
        (
            "system", """
            You are a programming assistant. Use your tools to answer questions.
            If you do not have a tool to answer the question, say so.

            return only the answers.
            """
        ),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad")

])

agent = create_openai_tools_agent(llm, toolkit, prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=toolkit, verbose=True)


def main():
    while True:
        try:
            pergunta = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")
            
            if pergunta.lower() == 'sair':
                print("Até logo!")
                break
            
            resposta = agent_executor.invoke({"input": pergunta})
            print("\nResposta:", resposta["output"])
            
        except KeyboardInterrupt:
            print("\nPrograma encerrado pelo usuário.")
            break
        except Exception as e:
            print(f"\nOcorreu um erro: {str(e)}")

if __name__ == "__main__":
    main()

