import requests
import re
from bs4 import BeautifulSoup

url = 'http://localhost:8000/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# if parsed_html.title is not None:
#     print(parsed_html.h2.text)

top_jobs_heading = parsed_html.select_one('#intro > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > h2:nth-child(1)')
# print(top_jobs_heading, top_jobs_heading.text)

if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    # print(article)

    if article is not None:
        for p in article.select('p'):
            # print(p.text)
            print(re.sub(r'\s{1,}', ' ', p.text).strip())  # espressão regular(substituir, re.sub(), o \s e para dizer que é espeaço e o numero na {1,} que dizer, os espaços acima de 1 vai ser substituido pelo que vem depois da virgula que é o ' ', do item p.text, .strip() é pra corta os espaços do começo e fim de strings )