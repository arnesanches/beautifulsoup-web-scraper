Beautiful Soup Web Scraper

Este projeto é um exemplo simples de web scraping desenvolvido em Python. Ele realiza requisições ao site da BBC para extrair os títulos dos artigos encontrados na página inicial. Após a extração, os títulos são salvos em um arquivo de texto para consulta ou uso posterior.

O script foi projetado para realizar a requisição HTTP e obter o conteúdo HTML da página, analisar o HTML com a biblioteca BeautifulSoup, localizar os títulos de interesse e salvar os dados extraídos em um arquivo de texto no formato UTF-8. Todas as etapas do processo são automatizadas e organizadas em funções específicas para facilitar a manutenção e a reutilização do código.

Para executar o código, é necessário ter Python 3.7 ou superior instalado, além das bibliotecas requests e beautifulsoup4. Caso ainda não estejam instaladas, elas podem ser adicionadas ao ambiente por meio do comando pip. Recomenda-se executar o script em um terminal, fornecendo a URL desejada e verificando o arquivo gerado no diretório do projeto.

Ao ser executado, o script acessa o site da BBC, analisa o conteúdo HTML retornado e extrai os títulos encontrados. Esses títulos são salvos em um arquivo chamado "bbc_titles.txt", localizado no mesmo diretório do script. O arquivo gerado organiza os títulos extraídos, cada um em uma linha.

Este projeto foi criado com fins educacionais, para demonstrar como estruturar um web scraper básico em Python. É importante revisar os termos de uso do site antes de realizar web scraping, pois algumas práticas podem ser consideradas inadequadas ou violar as políticas de determinados sites.
