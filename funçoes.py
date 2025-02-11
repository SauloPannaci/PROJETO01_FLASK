import requests

def lista_Cidades(): # Esta função foi criada para extrair json() da api
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos" #url que será extraido meu arquivo json
    resposta = requests.get(url) #variavel 'resposta' armazena minha requisição na url do ibge
    return resposta.json() #o retorno e tranformado em formato json



def sigla(UF): # Está função foi criada como parametro
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{UF}/distritos"#Url que pede um parametro que no caso é o parametro UF que falta
    resposta = requests.get(url)  #variavel 'resposta' armazena minha requisição na url do ibge
    return resposta.json()  #o retorno e tranformado em formato json


def ordenar_cidades(cidades): # Esta função é  para ordenar
    nomes_cidades = [] # uma lista vazia que vai ser adicionada as cidades
    for cidade in cidades: #Para cada 'cidade' na lista cidades
        nomes_cidades.append(cidade['nome']) #A lista que está vazia vai adicionar apenas o nome de cada cidade nela
    nomes_cidades.sort() #A lista que esta apenas com os nomes da cidade usa o metodo sort() para ordenação
    return nomes_cidades # Esta retorna minha lista