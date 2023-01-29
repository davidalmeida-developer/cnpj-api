from flask import Flask
import os


APP_NAME = os.getenv('APP_NAME', 'cnpj_api')
FLASK_HOST = os.getenv('FLASK_HOST','0.0.0.0')
FLASK_PORT = os.getenv('FLASK_PORT', 5000)

URL_CNPJ_WS = 'https://publica.cnpj.ws/cnpj/'

app = Flask(APP_NAME)
