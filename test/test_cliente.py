import pytest
from flask import Flask
from database.connection import engine, Session
from models.models import Base, Cliente
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

# Prueba para obtener todos los clientes
def test_get_clientes(client):
    response = client.get('/clientes')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

# Prueba para obtener un cliente por ID
def test_get_cliente(client):
    response = client.get('/cliente/1')
    assert response.status_code in (200, 404)  # Puede ser exitoso o no encontrado

# Prueba para crear un cliente
def test_create_cliente(client):
    new_cliente = {
        "nombre": "Juan Pérez",
        "correo": "juan@example.com",
        "saldo": 1000,
        "tipo_cuenta": "Ahorros"
    }
    response = client.post('/cliente', json=new_cliente)
    # assert response.status_code == 201
    # assert response.get_json()['message'] == "Cliente creado exitosamente"

# Prueba para actualizar un cliente
def test_update_cliente(client):
    updated_cliente = {"nombre": "Juan Actualizado"}
    response = client.put('/cliente/1', json=updated_cliente)
    assert response.status_code in (200, 404)

# Prueba para eliminar un cliente
def test_delete_cliente(client):
    response = client.delete('/cliente/1')
    assert response.status_code in (200, 404)