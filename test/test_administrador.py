import pytest
from flask import Flask
from database.connection import engine, Session
from models.models import Base, Administrador
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
    administrador = Administrador(
        nombre="Admin Prueba",
        correo="admin@prueba.com",
        estado="Activo"
    )
    session.add(administrador)
    session.commit()

    yield testing_client  # Devolver el cliente para las pruebas

    # Limpiar la base de datos después de las pruebas
    session.close()
    # Base.metadata.drop_all(bind=engine)

# Test para obtener todos los administradores
def test_get_administradores(client):
    response = client.get('/administradores')
    data = response.get_json()

# Test para obtener un administrador por ID
def test_get_administrador(client):
    response = client.get('/administrador/1')  # ID del administrador inicial
    data = response.get_json()

# Test para crear un nuevo administrador
def test_create_administrador(client):
    new_administrador = {
        "nombre": "Nuevo Admin",
        "correo": "nuevo@admin.com",
        "estado": "Activo"
    }
    response = client.post('/administrador', json=new_administrador)
    data = response.get_json()

    # Verificar que el administrador fue agregado
    response = client.get('/administradores')
    data = response.get_json()

# Test para actualizar un administrador
def test_update_administrador(client):
    updated_data = {
        "nombre": "Admin Actualizado",
        "correo": "actualizado@admin.com",
        "estado": "Inactivo"
    }
    response = client.put('/administrador/1', json=updated_data)
    data = response.get_json()

    # Verificar los cambios
    response = client.get('/administrador/1')
    data = response.get_json()

# Test para eliminar un administrador
def test_delete_administrador(client):
    response = client.delete('/administrador/2')
    # assert response.status_code == 200
    data = response.get_json()

    # Verificar que el administrador fue eliminado
    response = client.get('/administradores')
    data = response.get_json()

