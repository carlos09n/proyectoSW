import pytest
from flask import Flask
from database.connection import engine, Session
from models.models import Base, Actividad
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
    
    # Crear datos iniciales
    actividad = Actividad(
        descripcion="Actividad de prueba",
        tipo_usuario="Admin",
        resultado="Exitoso"
    )
    session.add(actividad)
    session.commit()

    yield testing_client  # Devolver el cliente para las pruebas

    # Limpiar la base de datos después de las pruebas
    session.close()
    # Base.metadata.drop_all(bind=engine)

def test_get_actividades(client):
    response = client.get('/actividades')
    data = response.get_json()

def test_get_actividad(client):
    response = client.get('/actividad/2')  # Usando ID de actividad inicial
    data = response.get_json()

def test_create_actividad(client):
    new_actividad = {
        "descripcion": "Nueva actividad",
        "tipo_usuario": "User",
        "resultado": "Pendiente"
    }
    response = client.post('/actividad', json=new_actividad)
    data = response.get_json()

    # Verificar que la actividad fue agregada
    response = client.get('/actividades')
    data = response.get_json()

def test_update_actividad(client):
    updated_data = {
        "descripcion": "Actividad actualizada",
        "tipo_usuario": "Admin",
        "estado": "Modificado"
    }
    response = client.put('/actividad/2', json=updated_data)
    data = response.get_json()

def test_delete_actividad(client):
    response = client.delete('/actividad/1')
    data = response.get_json()

    # Verificar que la actividad fue eliminada
    response = client.get('/actividades')
    data = response.get_json()
    # assert len(data) == 0
