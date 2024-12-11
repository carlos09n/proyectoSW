import pytest
from flask import Flask
from controladores.auditor.auditor import get_auditores, get_auditor, create_auditor, update_auditor, delete_auditor
from database.connection import Session
from models.models import Auditor

# Crear una aplicación Flask para pruebas
@pytest.fixture
def app():
    app = Flask(__name__)

    # Registrar las rutas de prueba
    app.add_url_rule('/auditores', 'get_auditores', get_auditores, methods=['GET'])
    app.add_url_rule('/auditores/<int:id>', 'get_auditor', get_auditor, methods=['GET'])
    app.add_url_rule('/auditores', 'create_auditor', create_auditor, methods=['POST'])
    app.add_url_rule('/auditores/<int:id>', 'update_auditor', update_auditor, methods=['PUT'])
    app.add_url_rule('/auditores/<int:id>', 'delete_auditor', delete_auditor, methods=['DELETE'])

    yield app

# Cliente para pruebas
@pytest.fixture
def client(app):
    return app.test_client()

# Mock para la base de datos
@pytest.fixture
def mock_db(monkeypatch):
    # Sesión de prueba simulada
    class MockSession:
        def __init__(self):
            self.data = [
                Auditor(id_auditor=1, nombre="Auditor 1", correo="auditor1@example.com", estado="Activo"),
                Auditor(id_auditor=2, nombre="Auditor 2", correo="auditor2@example.com", estado="Inactivo"),
            ]

        def query(self, model):
            return self

        def all(self):
            return self.data

        def filter_by(self, **kwargs):
            for auditor in self.data:
                if all(getattr(auditor, k) == v for k, v in kwargs.items()):
                    return [auditor]
            return []

        def add(self, obj):
            self.data.append(obj)

        def commit(self):
            pass

        def rollback(self):
            pass

        def close(self):
            pass

    mock_session = MockSession()
    monkeypatch.setattr('your_module.Session', lambda: mock_session)

# Pruebas para los endpoints

def test_get_auditores(client, mock_db):
    response = client.get('/auditores')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['nombre'] == "Auditor 1"

def test_get_auditor(client, mock_db):
    response = client.get('/auditores/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['nombre'] == "Auditor 1"

def test_create_auditor(client, mock_db):
    new_auditor = {"nombre": "Auditor Nuevo", "correo": "nuevo@example.com", "estado": "Activo"}
    response = client.post('/auditores', json=new_auditor)
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == "Auditor creado exitosamente"

def test_update_auditor(client, mock_db):
    updated_auditor = {"nombre": "Auditor Actualizado"}
    response = client.put('/auditores/1', json=updated_auditor)
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Auditor actualizado exitosamente"

def test_delete_auditor(client, mock_db):
    response = client.delete('/auditores/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Auditor eliminado exitosamente"