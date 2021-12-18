from app import app
from flask import render_template, request
import requests


api_access_key = "1b7ea67363e09e5c571cc1fad4ae7d77" 
url = "http://data.fixer.io/api/latest?access_key="+api_access_key



@app.route("/index" , methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("first")                   #'pega' o primeiro valor dado pelo usuário no HTML.
        secondCurrency = request.form.get("second")                 #'pega' o segundo valor dado pelo usuário no HTML. 
        amount = request.form.get("amount")                         #'pega' o valor digitado pelo usuário.
        response = requests.get(url)                                #faz a requisição da URL que foi passada --> http://data.fixer.io/api/latest?access_key="
        info = response.json()                                      #pega o fluxo de respostas da API e mostra o resultado do texto como um JSON.
        firstValue = info["rates"][firstCurrency]                   #[rates] Retorna dados de taxa de câmbio para as moedas que você solicitou.
        secondValue = info["rates"][secondCurrency]                      
        result = (secondValue / firstValue) * float(amount)         #variavel result recebe o segundo valor e divide pelo primeiro e multiplicando pelo valor.
        currencyInfo = dict()                                       #funcao que cria um dicionario           
        currencyInfo["first"]  = firstCurrency                      #Atribui o primeiro escolhido do usuario com o select cujo nome é first
        currencyInfo["second"] = secondCurrency                     #Atribui o segundo escolhido do usuario com o select cujo nome é second
        currencyInfo["amount"] = amount                             #Armazena o valor escolhido pelo usuario e atribui com input cuja class é amount         
        currencyInfo["result"] = result                             #Armazena o valor do resultado              
        return render_template("index.html", info = currencyInfo)   #Imprime na mesma tela do index a taxa de cambio com o metodo info
    else:
        return render_template("index.html")   

