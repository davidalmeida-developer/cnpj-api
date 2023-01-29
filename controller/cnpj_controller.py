import jsonpickle
from settings import app
from service.cnpj_service import CnpjService
from flask import request
import json


URL = '/cnpj_api'

@app.route(URL, methods=["GET"])
def get_dados():
    try:    
        cnpj = request.args.get('cnpj')
        service = CnpjService()

        dados = service.getDados(cnpj)

        return (jsonpickle.encode(dados, unpicklable=False), 200, '')
    except Exception as e:
        return ({'Erro': e.args[0]}, 400, '')