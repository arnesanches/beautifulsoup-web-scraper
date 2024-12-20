import requests

def get_html(url):
    """Faz a requisição HTTP e retorna o conteúdo HTML se bem-sucedida."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Erro ao acessar a página. Código de status: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Ocorreu um erro ao tentar acessar o site: {e}")
        return None
   
# Testando a função de requisição
url = 'https://bbc.com'
html_content = get_html(url)

from bs4 import BeautifulSoup


def analyze_html(html):
    """Analisa o HTML usando BeautifulSoup."""
    return BeautifulSoup(html, 'html.parser')

# Testando a análise do HTML
if html_content:
    soup = analyze_html(html_content)
    print("HTML analisado com sucesso.")


def extract_titles(soup):
    """Extrai os títulos da página definidos na tag <h2>."""
    titles = soup.find_all('h2')
    return [title.get_text().strip() for title in titles]

# Testando a extração de títulos
if soup:
    titles = extract_titles(soup)
    if titles:
        print("Títulos encontrados:")
        for title in titles:
            print(f"- {title}")
    else:
        print("Nenhum título encontrado na página.")


def save_to_file(data, filename):
    """Salva os dados extraídos em um arquivo de texto."""
    try:
        with open(filename, 'w', encoding='utf=8') as file:
            file.write("\n".join(data))
        print(f"Títulos salvos em {filename}.")
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Testando o salvamento em arquivo
if titles:
    save_to_file(titles, 'bbc_titles.txt')


def main(url, filename):
    """Executa o processo completo de Web Scraping."""
    html = get_html(url)
    if html:
        soup = analyze_html(html)
        titles = extract_titles(soup)
        if titles:
            save_to_file(titles, filename)
        else:
            print("Nenhum título foi extraído.")

# Executando o programa completo
if __name__ == "__main__":
    main('https://bbc.com', 'bbc_titles.txt')