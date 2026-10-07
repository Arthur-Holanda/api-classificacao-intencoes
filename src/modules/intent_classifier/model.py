from typing import Dict
from pydantic import BaseModel

class Dados(BaseModel):
    id: str
    nome: str
    text: str
    timestamp: int 
    predicao: Optional[Predicao] = None

class Predicao(BaseModel):
    probs: Dict[str, float]




