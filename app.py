from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
import os
from Pacientes import Paciente
from Medicamentos import Medicamento
from Doctores import Doctor
from Enfermeras import Enfermera

app = Flask(__name__)
CORS(app)

#Almacenamiento
administrador = {
    "nombre":"ludwin",
    "apellido":"Tello",
    "nombre_usuario":"admin",
    "contrasena":"1234"
}

pacientes = []
medicamentos = []
doctores = []
enfermeras = []
@app.route('/', methods=['GET'])
def principal():
    return "Api Taller 1"

# Metodos pacientes
@app.route('/registro_paciente', methods=['POST'])
def registro_paciente():
    cuerpo = request.get_json()
    nombre = cuerpo['nombre'] 
    apellido = cuerpo['apellido']
    fecha_nacimiento = cuerpo['fecha_nacimiento']
    sexo = cuerpo['sexo']
    nombre_usuario = cuerpo['nombre_usuario']
    if(existe_usuario(nombre_usuario)):
        return jsonify({'agregado':0,'mensaje':'Ya existe un usuario con este nombre'})
    contrasena = cuerpo['contraseña']
    telefono = cuerpo['telefono']
    nuevo_paciente = Paciente(nombre,apellido,fecha_nacimiento,sexo,nombre_usuario,contrasena,telefono)
    global pacientes
    pacientes.append(nuevo_paciente)
    return jsonify({'agregado':1,'mensaje':'Registro exitoso'})

@app.route('/obtener_pacientes', methods=['GET'])
def obtener_pacientes():
    json_pacientes = []
    global pacientes
    for paciente in pacientes:
        json_pacientes.append(paciente.get_json())
    return jsonify(json_pacientes)


#metodos doctores
@app.route('/registro_doctor', methods=['POST'])
def registro_doctor():
    cuerpo = request.get_json()
    nombre = cuerpo['nombre'] 
    apellido = cuerpo['apellido']
    fecha_nacimiento = cuerpo['fecha_nacimiento']
    sexo = cuerpo['sexo']
    nombre_usuario = cuerpo['nombre_usuario']
    if(existe_usuario(nombre_usuario)):
        return jsonify({'agregado':0,'mensaje':'Ya existe un usuario con este nombre'})
    contrasena = cuerpo['contrasena']
    especialidad = cuerpo['especialidad']
    telefono = cuerpo['telefono']
    nuevo_doctor = Doctor(nombre,apellido,fecha_nacimiento,sexo,nombre_usuario,contrasena,especialidad,telefono)
    global doctores
    doctores.append(nuevo_doctor)
    return jsonify({'agregado':1,'mensaje':'Registro exitoso'})

@app.route('/obtener_doctores', methods=['GET'])
def obtener_doctores():
    json_doctores = []
    global doctores
    for doctor in doctores:
        json_doctores.append(doctor.get_json())
    return jsonify(json_doctores)


#metodos enfermeras
@app.route('/registro_enfermera', methods=['POST'])
def registro_enfermera():
    cuerpo = request.get_json()
    nombre = cuerpo['nombre'] #nombre = ingrid
    apellido = cuerpo['apellido']
    fecha_nacimiento = cuerpo['fecha_nacimiento']
    sexo = cuerpo['sexo']
    nombre_usuario = cuerpo['nombre_usuario']
    if(existe_usuario(nombre_usuario)):
        return jsonify({'agregado':0,'mensaje':'Ya existe un usuario con este nombre'})
    contrasena = cuerpo['contraseña']
    telefono = cuerpo['telefono']
    nuevo_enfermera = Enfermera(nombre,apellido,fecha_nacimiento,sexo,nombre_usuario,contrasena,telefono)
    global enfermeras
    enfermeras.append(nuevo_enfermera)
    return jsonify({'agregado':1,'mensaje':'Registro exitoso'})

@app.route('/obtener_enfermeras', methods=['GET'])
def obtener_enfermeras():
    json_enfermeras = []
    global enfermeras
    for enfermera in enfermeras:
        json_enfermeras.append(enfermera.get_json())
    return jsonify(json_enfermeras)


#log

@app.route('/login', methods=['GET'])
def login():
    nombre_usuario = request.args.get("nombre_usuario")
    contrasena = request.args.get("contrasena")
    if not existe_usuario(nombre_usuario):
        return jsonify({'estado': 0, 'mensaje':'No existe este usuario'})
    if verificar_contrasena(nombre_usuario,contrasena) == 1:
        return jsonify({'estado': 1, 'mensaje':'Login exitoso'})
    return jsonify({'estado': 0, 'mensaje':'La contraseña es incorrecta'})
    if verificar_contrasena(nombre_usuario,contrasena) == 2:
        return jsonify({'estado': 2, 'mensaje':'Login exitoso'})
    return jsonify({'estado': 0, 'mensaje':'La contraseña es incorrecta'})
    if verificar_contrasena(nombre_usuario,contrasena) == 3:
        return jsonify({'estado': 3, 'mensaje':'Login exitoso'})
    return jsonify({'estado': 0, 'mensaje':'La contraseña es incorrecta'})
    if verificar_contrasena(nombre_usuario,contrasena) == 4:
        return jsonify({'estado': 4, 'mensaje':'Login exitoso'})
    return jsonify({'estado': 0, 'mensaje':'La contraseña es incorrecta'})
    

def verificar_contrasena(nombre_usuario, contrasena):
    if nombre_usuario == administrador['nombre_usuario'] and contrasena == administrador['contrasena']:
        return 1
    global pacientes
    for paciente in pacientes:
        if paciente.nombre_usuario == nombre_usuario and paciente.contrasena == contrasena:
            return 2
    global enfermeras
    for enfermera in enfermeras:
        if enfermera.nombre_usuario == nombre_usuario and enfermera.contrasena == contrasena:
            return 3

    global doctores
    for doctor in doctores:
        if doctor.nombre_usuario == nombre_usuario and doctor.contrasena == contrasena:
            return 4

    
    return False

def existe_usuario(nombre_usuario):
    if nombre_usuario == administrador['nombre_usuario']:
        return True
    global pacientes
    for paciente in pacientes:
        if paciente.nombre_usuario == nombre_usuario:
            return True
    global enfermeras
    for enfermera in enfermeras
        if enfermera.nombre_usuario == nombre_usuario
            return True
    global doctores
    for doctor in doctores:
        if doctor.nombre_usuario == nombre_usuario:
            return True
    return False

#INICIO CRUD MEDICAMENTOS
@app.route('/cargar_medicamentos', methods=['POST'])
def cargar_medicamentos():
    cuerpo = request.get_json()
    contenido = cuerpo['contenido']
    filas = contenido.split("\r\n")
    global medicamentos
    for fila in filas:
        print(fila)
        columnas = fila.split(",")
        medicamento = Medicamento(columnas[0],columnas[1],columnas[2],columnas[3])
        medicamentos.append(medicamento)
    return jsonify({"mensaje":"Carga masiva exitosa"})

@app.route('/obtener_medicamentos', methods=['GET'])
def obtener_medicamentos():
    json_medicamentos = []
    global medicamentos
    for medicamento in medicamentos:
        json_medicamentos.append(medicamento.get_json())
    return jsonify(json_medicamentos)

@app.route('/eliminar_medicamento', methods=['POST'])
def eliminar_medicamento():
    cuerpo = request.get_json()
    indice = cuerpo['indice']
    i = int(indice)
    global medicamentos
    medicamentos.pop(i)
    return jsonify({"mensaje":"Eliminado exitosamente"})

@app.route('/editar_medicamento', methods=['POST'])
def editar_medicamento():
    cuerpo = request.get_json()
    indice = cuerpo['indice']
    nombre = cuerpo['nombre']
    precio = cuerpo['precio']
    descripcion = cuerpo['descripcion']
    cantidad = cuerpo['cantidad']
    i = int(indice)
    global medicamentos
    medicamentos[i].editar(nombre,precio,descripcion,cantidad)
    return jsonify(medicamentos[i].get_json())

#FIN CRUD MEDICAMENTOS  

if __name__ == '__main__':
    puerto = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0',port=puerto)

