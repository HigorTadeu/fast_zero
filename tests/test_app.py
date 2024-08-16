from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Essa função retorna o EndPoint # Act (Ação)
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(  # UserSchema - Testando a parte do envio dos dados
        '/users/',
        json={
            'username': 'testeusername',
            'password': 'password',
            'email': 'teste@teste.com',
        },
    )

    # Retornou o status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testeusername',
                'email': 'teste@teste.com',
                'id': 1,
            }
        ]
    }
