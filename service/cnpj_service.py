from client.cnpj_ws_client import CnpjWsClient
from validate_docbr import CNPJ
from dto.cnpj_ws_dto.empresa import EmpresaCnpjWs
import re
from dto.retorno_dto.empresa import Empresa
from dto.retorno_dto.endereco import Endereco
from dto.retorno_dto.inscricao_estadual import InscricaoEstadual


class CnpjService:
    def __init__(self) -> None:
        self.cnpj_client = CnpjWsClient()
        self.validador = CNPJ()

    def getDados(self, cnpj:str)-> Empresa:
        
        cnpj = re.sub('[^0-9]',"", cnpj)
        if self.validador.validate(cnpj):
            dados = self.cnpj_client.getDadosCnpj(cnpj)
            retorno =  self.converterDados(dados)
            return retorno
        raise Exception("CNPJ inválido!")

    def converterDados(self, dados:EmpresaCnpjWs) -> Empresa:
        
        empresa = Empresa()

        empresa.cnpj = dados.estabelecimento.cnpj
        empresa.razao_social = dados.razao_social
        empresa.nome_fantasia = dados.estabelecimento.nome_fantasia
        empresa.atividade = dados.estabelecimento.atividade_principal["descricao"]
        empresa.inicio_atividades = dados.estabelecimento.data_inicio_atividade
        empresa.atualizado_em = dados.atualizado_em.strftime('%Y-%m-%dT%H:%M:%s')
        empresa.ddd = dados.estabelecimento.ddd1
        empresa.telefone = dados.estabelecimento.telefone1
        empresa.email = dados.estabelecimento.email

        endereco = Endereco()

        endereco.tipo_logradouro = dados.estabelecimento.tipo_logradouro
        endereco.logradouro = dados.estabelecimento.logradouro
        endereco.numero = dados.estabelecimento.numero
        endereco.bairro = dados.estabelecimento.bairro
        endereco.complemento = dados.estabelecimento.complemento
        endereco.cep = dados.estabelecimento.cep
        endereco.cidade = dados.estabelecimento.cidade["nome"]
        endereco.estado = dados.estabelecimento.estado["nome"]
        endereco.pais = dados.estabelecimento.pais["nome"]
        empresa.endereco = endereco
        
        for inscricao in dados.estabelecimento.inscricoes_estaduais:
            inscricao_estadual = InscricaoEstadual()
            inscricao_estadual.inscricao_estadual = inscricao["inscricao_estadual"]
            inscricao_estadual.estado = inscricao["estado"]["nome"]
            empresa.inscricoes_estaduais.append(inscricao_estadual)

        return empresa