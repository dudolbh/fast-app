from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_app.app import app


@pytest.fixture
def client():
    return TestClient(app)  # Arrange


def test_read_root(client):
    response = client.get('/')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.text == '{"text":"Ola Mundo!"}'  # Assert


def test_read_hello(client):
    response = client.get('/hello')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    assert (
        response.text
        == """<html>
                <head>
                    <title>Hello World</title>
                </head>
                <body>
                    <h1>Hello World!</h1>
                </body>
        </html>"""
    )  # Assert


def test_create_user(client):
    user_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'securepass',
    }
    response = client.post('/users/', json=user_data)
    assert response.status_code == HTTPStatus.CREATED
    data = response.json()
    assert data['username'] == 'testuser'
    assert data['email'] == 'test@example.com'
    assert 'password' not in data  # Password should not be in response


def teste_update_user(client):
    user_data = {
        'username': 'useralt',
        'email': 'useralt@example.com',
        'password': 'securepass',
    }
    response = client.put('users/1', json=user_data)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'useralt',
        'email': 'useralt@example.com',
        'id': 1,
    }


def test_update_not_found(client):
    user_data = {
        'username': 'useralt',
        'email': 'useralt@example.com',
        'password': 'securepass',
    }
    response = client.put('users/2', json=user_data)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete(client):
    response = client.delete('users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'text': 'User deleted'}
