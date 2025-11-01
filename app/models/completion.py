from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class User:
    id: int
    name: str


class DataInputModel(BaseModel):
    prompt: str


class DataOutputModel(BaseModel):
    response: str
