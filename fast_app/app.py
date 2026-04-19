from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fast_app.schemas import (
    DbUserSchema,
    Message,
    UserPublicSchema,
    UserSchema,
    UsersList,
)

app = FastAPI()

database = []


# Por padrão, o FastAPI já retorna o status code 200 para requisições GET
# Para o response_class o padrão é json
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
# Retorno explicito do status code, response_model é a class doS
# pydantic que define o formato do retorno
def read_root():
    return Message(text='Ola Mundo!')


@app.get('/hello/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_hello():
    return """<html>
                <head>
                    <title>Hello World</title>
                </head>
                <body>
                    <h1>Hello World!</h1>
                </body>
        </html>"""


@app.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema
)
def create_user(user: UserSchema):
    user_with_id = DbUserSchema(id=len(database) + 1, **user.model_dump())
    print(len(database))
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UsersList)
def list_users():
    return {'users': database}


@app.put(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserPublicSchema,
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = DbUserSchema(id=user_id, **user.model_dump())

    if user_id < 1 or user_id > len(database):
        raise HTTPException(HTTPStatus.NOT_FOUND, detail='Usuário não existe.')

    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=Message,
)
def delete_user(user_id: int):

    if user_id < 1 or user_id > len(database):
        raise HTTPException(HTTPStatus.NOT_FOUND, detail='Usuário não existe.')

    del database[user_id - 1]
    return Message(text='User deleted')
