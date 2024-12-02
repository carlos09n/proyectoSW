from flask import Flask
from controladores.cliente.cliente import get_clientes, get_cliente, create_cliente, update_cliente, delete_cliente
from controladores.auditor.auditor import get_auditores, get_auditor, create_auditor, update_auditor, delete_auditor
from controladores.administrador.administrador import get_administradores, get_administrador, create_administrador, update_administrador, delete_administrador
from controladores.actividad.actividad import get_actividades, get_actividad, create_actividad, update_actividad, delete_actividad

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor API corriendo con Flask!"

# Rutas para CLIENTE
@app.route('/clientes', methods=['GET'])
def clientes():
    return get_clientes()

@app.route('/cliente/<int:id>', methods=['GET'])
def cliente(id):
    return get_cliente(id)

@app.route('/cliente', methods=['POST'])
def add_cliente():
    return create_cliente()

@app.route('/cliente/<int:id>', methods=['PUT'])
def edit_cliente(id):
    return update_cliente(id)

@app.route('/cliente/<int:id>', methods=['DELETE'])
def remove_cliente(id):
    return delete_cliente(id)

# Rutas para AUDITOR
@app.route('/auditores', methods=['GET'])
def auditores():
    return get_auditores()

@app.route('/auditor/<int:id>', methods=['GET'])
def auditor(id):
    return get_auditor(id)

@app.route('/auditor', methods=['POST'])
def add_auditor():
    return create_auditor()

@app.route('/auditor/<int:id>', methods=['PUT'])
def edit_auditor(id):
    return update_auditor(id)

@app.route('/auditor/<int:id>', methods=['DELETE'])
def remove_auditor(id):
    return delete_auditor(id)

# Rutas para ADMINISTRADOR
@app.route('/administradores', methods=['GET'])
def administradores():
    return get_administradores()

@app.route('/administrador/<int:id>', methods=['GET'])
def administrador(id):
    return get_administrador(id)

@app.route('/administrador', methods=['POST'])
def add_administrador():
    return create_administrador()

@app.route('/administrador/<int:id>', methods=['PUT'])
def edit_administrador(id):
    return update_administrador(id)

@app.route('/administrador/<int:id>', methods=['DELETE'])
def remove_administrador(id):
    return delete_administrador(id)

# Rutas para ACTIVIDAD
@app.route('/actividades', methods=['GET'])
def actividades():
    return get_actividades()

@app.route('/actividad/<int:id>', methods=['GET'])
def actividad(id):
    return get_actividad(id)

@app.route('/actividad', methods=['POST'])
def add_actividad():
    return create_actividad()

@app.route('/actividad/<int:id>', methods=['PUT'])
def edit_actividad(id):
    return update_actividad(id)

@app.route('/actividad/<int:id>', methods=['DELETE'])
def remove_actividad(id):
    return delete_actividad(id)

if __name__ == '__main__':
    app.run(debug=True)
