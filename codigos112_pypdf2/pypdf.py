from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
PASTA_ORIGINAL = ROOT_FOLDER/ 'PDF'
PASTA_NOVA = ROOT_FOLDER / 'arquivo_novo'

RELATORIO = PASTA_ORIGINAL / 'R20241004.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO)

# print(len(reader.pages))

#1 aqui e para da prints
# for page in reader.pages:
#     print(page)
#     print()
# page1 = reader.pages[1]
# imagem0 = page1.images[0]

# # 2 essa para seleionar os textos econtar imagens
# print(page1.extract_text())
# print(len(page1.images))

#3 essa parte e pra pega imagens
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)

# 4 esse modo e para pegar paginas de pdf
# writer = PdfWriter()
# writer.add_page(page1)

# with open(PASTA_NOVA / 'page1.pdf', 'wb') as arquivo:
#     writer.write(arquivo)

#esse aqui vai fazer um for e por cada pagina no pdf vai criar um novo pdf com as paginas
# writer = PdfWriter()

# with open(PASTA_NOVA / 'NOVOPDF.pdf', 'wb') as arquivo:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(arquivo)

#esse vai criar  pdf separados com as paginas do pdf selecionado, cuidado pra nao usar um pdf de muitas paginas

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'pagina{i}.pdf', 'wb') as arquivo:
        
        writer.add_page(page)
        writer.write(arquivo)

# esse e para unir arquivos PDF diferentes

files = [
    PASTA_NOVA / 'pagina0.pdf',
    PASTA_NOVA / 'pagina1.pdf',
]
merger = PdfMerger()
# parte 1 esse modo mais complexo ja fecha o arquivo
with open(PASTA_NOVA / 'merged2.pdf', 'wb') as arquivo2:
    for file in files: 
        merger.append(file)
    merger.write(arquivo2)

# parte 2 esse modo é mais simples, mas deve sempre lembrar de fechar
# files = [
#     PASTA_NOVA / 'pagina0.pdf',
#     PASTA_NOVA / 'pagina1.pdf',
# ]
# merger = PdfMerger()

# merger.write(PASTA_NOVA / 'merged.pdf')
# merger.close()
