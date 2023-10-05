import requests

response = requests.get('https://contas.tcu.gov.br/pesquisaJurisprudencia/#/detalhamento/11/%252a/NUMACORDAO%253A1771%2520ANOACORDAO%253A2022%2520COLEGIADO%253A%2522Plen%25C3%25A1rio%2522/DTRELEVANCIA%2520desc/false/1')
print(response.content)
