import requests
from bs4 import BeautifulSoup

def get_text_from_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parse")

        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()
        

        text = soup.get_text()

        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
        text = "\n".join(chunk for chunk in chunks if chunk)

        return text 
    else:
        return f"Erro ao acessar a página: {response.status_code}"