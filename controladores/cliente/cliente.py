from flask import jsonify, request
from database.connection import Session
from models.models import Cliente

# Obtener todos los clientes (GET)
def get_clientes():
    session = Session()
    try:
        clientes = session.query(Cliente).all()
        result = [{"id": c.id_cliente, "nombre": c.nombre, "correo": c.correo, "saldo": c.saldo, "tipo_cuenta": c.tipo_cuenta, "estado": c.estado} for c in clientes]
        return jsonify(result)
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Obtener un cliente por ID (GET)
def get_cliente(id):
    session = Session()
    try:
        cliente = session.query(Cliente).filter_by(id_cliente=id).first()
        if cliente:
            return jsonify({
                "id": cliente.id_cliente,
                "nombre": cliente.nombre,
                "correo": cliente.correo,
                "saldo": cliente.saldo,
                "tipo_cuenta": cliente.tipo_cuenta,
                "estado": cliente.estado
            })
        else:
            return jsonify({"error": "Cliente no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Crear un nuevo cliente (POST)
def create_cliente():
    session = Session()
    try:
        data = request.get_json()
        new_cliente = Cliente(
            nombre=data['nombre'],
            correo=data['correo'],
            saldo=data['saldo'],
            tipo_cuenta=data['tipo_cuenta'],
            estado=data.get('estado', 'Activo')  # Valor predeterminado 'Activo'
        )
        session.add(new_cliente)
        session.commit()
        return jsonify({"message": "Cliente creado exitosamente", "id": new_cliente.id_cliente}), 201
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Actualizar un cliente (PUT)
def update_cliente(id):
    session = Session()
    try:
        data = request.get_json()
        cliente = session.query(Cliente).filter_by(id_cliente=id).first()
        if cliente:
            cliente.nombre = data.get('nombre', cliente.nombre)
            cliente.correo = data.get('correo', cliente.correo)
            cliente.saldo = data.get('saldo', cliente.saldo)
            cliente.tipo_cuenta = data.get('tipo_cuenta', cliente.tipo_cuenta)
            cliente.estado = data.get('estado', cliente.estado)

            session.commit()
            return jsonify({"message": "Cliente actualizado exitosamente"})
        else:
            return jsonify({"error": "Cliente no encontrado"}), 404
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Eliminar un cliente (DELETE)
def delete_cliente(id):
    session = Session()
    try:
        cliente = session.query(Cliente).filter_by(id_cliente=id).first()
        if cliente:
            session.delete(cliente)
            session.commit()
            return jsonify({"message": "Cliente eliminado exitosamente"})
        else:
            return jsonify({"error": "Cliente no encontrado"}), 404
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()
