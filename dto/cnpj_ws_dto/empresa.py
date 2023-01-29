from datetime import datetime
from pydantic import BaseModel
from typing import Dict, Optional

from dto.cnpj_ws_dto.estabelecimento import Estabelecimento


class EmpresaCnpjWs(BaseModel):
    razao_social: str
    atualizado_em: Optional[datetime]
    natureza_juridica: Dict
    estabelecimento: Estabelecimento
