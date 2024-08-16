from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

database = []  # Lista que simula momentâneo Banco de Dados
app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


# Endpoint para criar o Usuário considerando o schema User
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())

    database.append(user_with_id)  # Adiciona o usuário criado na lista

    return user_with_id


# Endpoint para retornar todos os usuários cadadastrados no Banco de Dados
@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}
