from app import app
from flask import render_template, request
import requests
import json

api_access_key = "3e8018266778321128faa8f686391525" 
url = "http://data.fixer.io/api/latest?access_key="+api_access_key



@app.route("/index2" , methods = ["GET","POST"])
def index2():
    if request.method == "POST":
        coluna1 = request.form.get("firstCurrency")                 #'pega' o primeiro valor dado pelo usuário no HTML.
        coluna2 = request.form.get("secondCurrency")                #'pega' o segundo valor dado pelo usuário no HTML. 
        amount = request.form.get("amount")                         #'pega' o valor digitado pelo usuário.
        response = requests.get(url)                                #faz a requisição da URL que foi passada --> http://data.fixer.io/api/latest?access_key="
        infos = response.json()                                     #pega o fluxo de respostas da API e mostra o resultado do texto como um JSON.
        firstValue = infos["rates"][coluna1]                        #Retorna os dados de cambio que foi solicitado no primeiro valor.
        secondValue = infos["rates"][coluna2]                       #Retorna os dados de cambio que foi solicitado no primeiro valor.
        result = (secondValue / firstValue) * float(amount)
        currencyInfo = dict()
        currencyInfo["coluna1"] = coluna1
        currencyInfo["secondCurrency"] = coluna2
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result
        #app.logger.info(infos)
        return render_template("index2.html",info = currencyInfo)
    else:
        return render_template("index2.html")   

