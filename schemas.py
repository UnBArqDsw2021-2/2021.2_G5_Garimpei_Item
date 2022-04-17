from pydantic import BaseModel


class AnswerSchema(BaseModel):
    title: str
    description: str
    status: str

    class Config():
        orm_mode = True


class ShowAnswerSchema(BaseModel):
    id: int
    title: str
    description: str
    status: str

    class Config():
        orm_mode = True