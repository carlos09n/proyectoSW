from flask import jsonify, request
from database.connection import Session
from models.models import Auditor

# Obtener todos los auditores (GET)
def get_auditores():
    session = Session()
    try:
        auditores = session.query(Auditor).all()
        result = [{"id": a.id_auditor, "nombre": a.nombre, "correo": a.correo, "estado": a.estado} for a in auditores]
        return jsonify(result)
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Obtener un auditor por ID (GET)
def get_auditor(id):
    session = Session()
    try:
        auditor = session.query(Auditor).filter_by(id_auditor=id).first()
        if auditor:
            return jsonify({
                "id": auditor.id_auditor,
                "nombre": auditor.nombre,
                "correo": auditor.correo,
                "estado": auditor.estado
            })
        else:
            return jsonify({"error": "Auditor no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Crear un nuevo auditor (POST)
def create_auditor():
    session = Session()
    try:
        data = request.get_json()
        new_auditor = Auditor(
            nombre=data['nombre'],
            correo=data['correo'],
            estado=data.get('estado', 'Activo')  # Valor predeterminado 'Activo'
        )
        session.add(new_auditor)
        session.commit()
        return jsonify({"message": "Auditor creado exitosamente", "id": new_auditor.id_auditor}), 201
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Actualizar un auditor (PUT)
def update_auditor(id):
    session = Session()
    try:
        data = request.get_json()
        auditor = session.query(Auditor).filter_by(id_auditor=id).first()
        if auditor:
            auditor.nombre = data.get('nombre', auditor.nombre)
            auditor.correo = data.get('correo', auditor.correo)
            auditor.estado = data.get('estado', auditor.estado)

            session.commit()
            return jsonify({"message": "Auditor actualizado exitosamente"})
        else:
            return jsonify({"error": "Auditor no encontrado"}), 404
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Eliminar un auditor (DELETE)
def delete_auditor(id):
    session = Session()
    try:
        auditor = session.query(Auditor).filter_by(id_auditor=id).first()
        if auditor:
            session.delete(auditor)
            session.commit()
            return jsonify({"message": "Auditor eliminado exitosamente"})
        else:
            return jsonify({"error": "Auditor no encontrado"}), 404
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()
