import requests
from dto.cnpj_ws_dto.empresa import EmpresaCnpjWs
from settings import URL_CNPJ_WS


class CnpjWsClient:

    def __init__(self) -> None:
        self.url = URL_CNPJ_WS
        self.headers = {'content': 'application/json'}

    def getDadosCnpj(self, cnpj) -> EmpresaCnpjWs:
        url = URL_CNPJ_WS + str(cnpj)
        response = requests.get(url, headers=self.headers)
        return EmpresaCnpjWs(**response.json())
