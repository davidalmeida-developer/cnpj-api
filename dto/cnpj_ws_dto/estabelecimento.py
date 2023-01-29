from pydantic import BaseModel
from typing import Dict, List, Optional


class Estabelecimento(BaseModel):
    cnpj:str
    nome_fantasia:Optional[str]
    data_inicio_atividade:Optional[str]
    tipo_logradouro:str
    logradouro:str
    numero:str
    complemento:str
    bairro:str
    cep:str
    ddd1:str
    telefone1:str
    email:str
    atualizado_em:Optional[str]
    atividade_principal:Dict
    pais:Dict
    estado:Dict
    cidade:Dict
    inscricoes_estaduais:List
