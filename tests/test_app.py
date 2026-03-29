from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_app.app import app

client = TestClient(app)  # Arrange


def test_read_root():
    response = client.get('/')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Ola Mundo!'}  # Assert
