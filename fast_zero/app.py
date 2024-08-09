from fastapi import FastAPI

from fast_zero.schemas import UserPublic, UserSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


# Endpoint para criar o Usuário considerando o schema User
@app.post('/users/', response_model=UserPublic)
def create_user(user: UserSchema):
    return user
