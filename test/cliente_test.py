import pytest
from flask import Flask
from controladores.cliente.cliente import get_clientes, get_cliente, create_cliente, update_cliente, delete_cliente
from database.connection import Session
from models.models import Cliente

# Crear una aplicación Flask para pruebas
@pytest.fixture
def app():
    app = Flask(__name__)

    # Registrar las rutas de prueba
    app.add_url_rule('/clientes', 'get_clientes', get_clientes, methods=['GET'])
    app.add_url_rule('/clientes/<int:id>', 'get_cliente', get_cliente, methods=['GET'])
    app.add_url_rule('/clientes', 'create_cliente', create_cliente, methods=['POST'])
    app.add_url_rule('/clientes/<int:id>', 'update_cliente', update_cliente, methods=['PUT'])
    app.add_url_rule('/clientes/<int:id>', 'delete_cliente', delete_cliente, methods=['DELETE'])

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# Mock para la base de datos
@pytest.fixture
def mock_db(monkeypatch):
    def mock_session():
        # Crear una sesión simulada
        return Session()

    monkeypatch.setattr('src.database.connection.Session', mock_session)

# Prueba para obtener todos los clientes
def test_get_clientes(client, mock_db):
    response = client.get('/clientes')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

# Prueba para obtener un cliente por ID
def test_get_cliente(client, mock_db):
    response = client.get('/clientes/1')
    assert response.status_code in (200, 404)  # Puede ser exitoso o no encontrado

# Prueba para crear un cliente
def test_create_cliente(client, mock_db):
    new_cliente = {
        "nombre": "Juan Pérez",
        "correo": "juan@example.com",
        "saldo": 1000,
        "tipo_cuenta": "Ahorros"
    }
    response = client.post('/clientes', json=new_cliente)
    assert response.status_code == 201
    assert response.get_json()['message'] == "Cliente creado exitosamente"

# Prueba para actualizar un cliente
def test_update_cliente(client, mock_db):
    updated_cliente = {"nombre": "Juan Actualizado"}
    response = client.put('/clientes/1', json=updated_cliente)
    assert response.status_code in (200, 404)

# Prueba para eliminar un cliente
def test_delete_cliente(client, mock_db):
    response = client.delete('/clientes/1')
    assert response.status_code in (200, 404)