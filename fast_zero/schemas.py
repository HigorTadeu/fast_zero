from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


"""
    Schema que será retornado de maneira pública com as informações do usuário
    foi retirado o atributo password por questão de segurança
"""


class UserPublic(BaseModel):
    username: str
    email: EmailStr
