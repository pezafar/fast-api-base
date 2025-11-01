from pydantic import BaseModel


class ItemInput(BaseModel):
    data: str


class ItemOutput(BaseModel):
    result: str
