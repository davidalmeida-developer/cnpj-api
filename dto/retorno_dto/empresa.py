from datetime import date, datetime
from typing import List
from dto.retorno_dto.endereco import Endereco
from dto.retorno_dto.inscricao_estadual import InscricaoEstadual


class Empresa:
    def __init__(self) -> None:
        self.cnpj:str = None
        self.razao_social: str = None
        self.nome_fantasia: str = None
        self.inicio_atividades: date = None
        self.atualizado_em: datetime = None
        self.atividade: str = None
        self.email: str = None
        self.ddd: str = None
        self.telefone: str = None
        self.endereco: Endereco = None
        self.inscricoes_estaduais: List[InscricaoEstadual] = []
