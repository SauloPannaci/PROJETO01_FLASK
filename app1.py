from flask import Flask, request
from funçoes import sigla, ordenar_cidades , lista_Cidades

# Instanciar a aplicação
app = Flask(__name__)

@app.route("/lista_ibge")  # Esta rota é para trazer todas as cidades do pais em ordem alfabética
def Todas_cidades(): # Esta aqui foi criada uma função para trazer as cidades
    cidades = lista_Cidades() # Esta variavel cidades, armazena uma outra função que foi chamada que contem as cidades
    ordenadas = ordenar_cidades(cidades) # Esta variavel ordenadas chama outra função que ordena as cidade em ordem alfabética
    return ordenadas # Esta aqui eu retorno a lista pronta

    

@app.route("/consulta_ibge", methods=['GET'])  # Esta rota para trazer cidades pela "UF" com suas informaçoes
def estado(): # Esta aqui foi criada uma função para compeltar a URL com o parametro que falta("UF")
    UF = request.args.get('UF') # Esta Variavel UF faz uma requisição do valor de 'UF' para ser usado na url
    resposta = sigla(UF) # Esta variavel resposta chama uma função, passando o parametro "UF"
    return resposta # Esta aqui eu retorno a lista de cidade de acordo com a sigla que passei para UF

@app.route("/ordenar_cidades", methods=['GET']) # Esta rota é para ordenar os nomes das cidade pela UF
def ordenar(): # Esta aqui foi criada minha função
    UF = request.args.get('UF') # Esta variavel UF apenas para implementação na resposta
    cidades = estado()  # Esta aqui Obtém todas as cidades pela UF que passei na URL
    cidades_ordenadas = ordenar_cidades(cidades)  # Esta aqui chama uma função que ordena as cidades
    return {f"cidades_ordenadas de {UF}": cidades_ordenadas} # Esta Retorna minha resposta e no lugar de {UF} ele traz a sigla do estado

if __name__ == "__main__":
    app.run(debug=True)