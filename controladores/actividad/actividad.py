from flask import jsonify, request
from database.connection import Session
from models.models import Actividad

# Obtener todas las actividades (GET)
def get_actividades():
    session = Session()
    try:
        actividades = session.query(Actividad).all()
        result = [{"id": a.id_actividad, "descripcion": a.descripcion, "tipo_usuario": a.tipo_usuario, "estado": a.estado} for a in actividades]
        return jsonify(result)
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Obtener una actividad por ID (GET)
def get_actividad(id):
    session = Session()
    try:
        actividad = session.query(Actividad).filter_by(id_actividad=id).first()
        if actividad:
            return jsonify({
                "id": actividad.id_actividad,
                "descripcion": actividad.descripcion,
                "tipo_usuario": actividad.tipo_usuario,
                "estado": actividad.estado
            })
        else:
            return jsonify({"error": "Actividad no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Crear una nueva actividad (POST)
def create_actividad():
    session = Session()
    try:
        data = request.get_json()
        new_actividad = Actividad(
            descripcion=data['descripcion'],
            tipo_usuario=data['tipo_usuario'],
            estado=data.get('estado', 'Pendiente')  # Valor predeterminado 'Pendiente'
        )
        session.add(new_actividad)
        session.commit()
        return jsonify({"message": "Actividad creada exitosamente", "id": new_actividad.id_actividad}), 201
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Actualizar una actividad (PUT)
def update_actividad(id):
    session = Session()
    try:
        data = request.get_json()
        actividad = session.query(Actividad).filter_by(id_actividad=id).first()
        if actividad:
            actividad.descripcion = data.get('descripcion', actividad.descripcion)
            actividad.tipo_usuario = data.get('tipo_usuario', actividad.tipo_usuario)
            actividad.estado = data.get('estado', actividad.estado)

            session.commit()
            return jsonify({"message": "Actividad actualizada exitosamente"})
        else:
            return jsonify({"error": "Actividad no encontrada"}), 404
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()

# Eliminar una actividad (DELETE)
def delete_actividad(id):
    session = Session()
    try:
        actividad = session.query(Actividad).filter_by(id_actividad=id).first()
        if actividad:
            session.delete(actividad)
            session.commit()
            return jsonify({"message": "Actividad eliminada exitosamente"})
        else:
            return jsonify({"error": "Actividad no encontrada"}), 404
    except Exception as ex:
        session.rollback()  # En caso de error, revertir los cambios
        return jsonify({"error": str(ex)}), 500
    finally:
        session.close()
