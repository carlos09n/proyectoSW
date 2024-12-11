from flask import jsonify, request
from database.connection import Session
from models.models import Administrador

# Obtener todos los administradores (GET)
def get_administradores():
    session = Session()
    try:
        administradores = session.query(Administrador).all()
        result = [{"id": a.id_admin, "nombre": a.nombre, "correo": a.correo, "estado": a.estado} for a in administradores]
        return jsonify(result)
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Obtener un administrador por ID (GET)
def get_administrador(id):
    session = Session()
    try:
        administrador = session.query(Administrador).filter_by(id_admin=id).first()
        if administrador:
            return jsonify({
                "id": administrador.id_admin,
                "nombre": administrador.nombre,
                "correo": administrador.correo,
                "estado": administrador.estado
            })
        else:
            return jsonify({"error": "Administrador no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Crear un nuevo administrador (POST)
def create_administrador():
    session = Session()
    try:
        data = request.get_json()
        new_administrador = Administrador(
            nombre=data['nombre'],
            correo=data['correo'],
            estado=data.get('estado', 'Activo')  # Valor predeterminado 'Activo'
        )
        session.add(new_administrador)
        session.commit()
        return jsonify({"message": "Administrador creado exitosamente", "id": new_administrador.id_admin}), 201
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Actualizar un administrador (PUT)
def update_administrador(id):
    session = Session()
    try:
        data = request.get_json()
        administrador = session.query(Administrador).filter_by(id_admin=id).first()
        if administrador:
            administrador.nombre = data.get('nombre', administrador.nombre)
            administrador.correo = data.get('correo', administrador.correo)
            administrador.estado = data.get('estado', administrador.estado)

            session.commit()
            return jsonify({"message": "Administrador actualizado exitosamente"})
        else:
            return jsonify({"error": "Administrador no encontrado"}), 404
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Eliminar un administrador (DELETE)
def delete_administrador(id):
    session = Session()
    try:
        administrador = session.query(Administrador).filter_by(id_admin=id).first()
        if administrador:
            session.delete(administrador)
            session.commit()
            return jsonify({"message": "Administrador eliminado exitosamente"})
        else:
            return jsonify({"error": "Administrador no encontrado"}), 404
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()
