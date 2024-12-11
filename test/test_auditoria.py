import pytest
from flask import Flask
from database.connection import engine, Session
from models.models import Base, Auditor
from main import app

@pytest.fixture
def client():
    # Configurar Flask en modo de prueba
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    testing_client = app.test_client()

    # Crear las tablas en la base de datos en memoria
    Base.metadata.create_all(bind=engine)
    session = Session()
    
    yield testing_client  # Devolver el cliente para las pruebas

    # Limpiar la base de datos después de las pruebas
    session.close()
    # Base.metadata.drop_all(bind=engine)

# Mock para la base de datos
@pytest.fixture
def mock_db(monkeypatch):
    # Sesión de prueba simulada
    class MockSession:
        def _init_(self):
            self.data = [
                Auditor(id_auditor=2, nombre="Auditor 1", correo="auditor1@example.com", estado="Activo"),
                Auditor(id_auditor=3, nombre="Auditor 2", correo="auditor2@example.com", estado="Inactivo"),
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

def test_get_auditores(client):
    response = client.get('/auditores')
    assert response.status_code == 200
    data = response.get_json()
    # assert isinstance(data, list)
    # assert len(data) == 2
    # assert data[0]['nombre'] == "Auditor 1"

def test_get_auditor(client):
    response = client.get('/auditor/2')
    assert response.status_code == 200
    data = response.get_json()
    # assert data['nombre'] == "Auditor 1"

def test_create_auditor(client):
    new_auditor = {"nombre": "Auditor Nuevo", "correo": "nuevo@example.com", "estado": "Activo"}
    response = client.post('/auditor', json=new_auditor)
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == "Auditor creado exitosamente"

def test_update_auditor(client):
    updated_auditor = {"nombre": "Auditor Actualizado"}
    response = client.put('/auditor/2', json=updated_auditor)
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Auditor actualizado exitosamente"

def test_delete_auditor(client):
    response = client.delete('/auditor/2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Auditor eliminado exitosamente"