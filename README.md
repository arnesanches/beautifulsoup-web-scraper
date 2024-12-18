### English 

# BeautifulSoup Web Scraper

This project is a simple example of web scraping developed in Python. It makes requests to the BBC website to extract the titles of articles found on the homepage. After extraction, the titles are saved in a text file for later reference or use.

The script is designed to perform an HTTP request to fetch the HTML content of the page, parse the HTML with the BeautifulSoup library, locate the desired titles, and save the extracted data in a UTF-8 formatted text file. All steps of the process are automated and organized into specific functions to facilitate code maintenance and reuse.

To run the code, you need to have Python 3.7 or higher installed, as well as the requests and beautifulsoup4 libraries. If they are not yet installed, they can be added to the environment using the pip command. It is recommended to execute the script in a terminal, providing the desired URL and checking the generated file in the project directory.

When executed, the script accesses the BBC website, analyzes the returned HTML content, and extracts the found titles. These titles are saved in a file named "bbc_titles.txt," located in the same directory as the script. The generated file organizes the extracted titles, each on a new line.

This project was created for educational purposes to demonstrate how to structure a basic web scraper in Python. It is important to review the website's terms of use before performing web scraping, as some practices may be considered inappropriate or violate the policies of certain websites.

---

### Português

# BeautifulSoup Web Scraper

Este projeto é um exemplo simples de web scraping desenvolvido em Python. Ele realiza requisições ao site da BBC para extrair os títulos dos artigos encontrados na página inicial. Após a extração, os títulos são salvos em um arquivo de texto para consulta ou uso posterior.

O script foi projetado para realizar a requisição HTTP e obter o conteúdo HTML da página, analisar o HTML com a biblioteca BeautifulSoup, localizar os títulos de interesse e salvar os dados extraídos em um arquivo de texto no formato UTF-8. Todas as etapas do processo são automatizadas e organizadas em funções específicas para facilitar a manutenção e a reutilização do código.

Para executar o código, é necessário ter Python 3.7 ou superior instalado, além das bibliotecas requests e beautifulsoup4. Caso ainda não estejam instaladas, elas podem ser adicionadas ao ambiente por meio do comando pip. Recomenda-se executar o script em um terminal, fornecendo a URL desejada e verificando o arquivo gerado no diretório do projeto.

Ao ser executado, o script acessa o site da BBC, analisa o conteúdo HTML retornado e extrai os títulos encontrados. Esses títulos são salvos em um arquivo chamado "bbc_titles.txt", localizado no mesmo diretório do script. O arquivo gerado organiza os títulos extraídos, cada um em uma linha.

Este projeto foi criado com fins educacionais, para demonstrar como estruturar um web scraper básico em Python. É importante revisar os termos de uso do site antes de realizar web scraping, pois algumas práticas podem ser consideradas inadequadas ou violar as políticas de determinados sites.
