from flask import render_template, request, redirect, url_for
from models import db, Paciente

def obtener_pacientes():
    """Obtiene todos los pacientes"""
    return Paciente.query.all()

def crear_paciente(nombre, edad, direccion, telefono):
    """Crea un nuevo paciente"""
    if nombre and edad and direccion and telefono:
        nuevo_paciente = Paciente(nombre=nombre, edad=int(edad), direccion=direccion, telefono=telefono)
        db.session.add(nuevo_paciente)
        db.session.commit()
        return True
    return False

def eliminar_paciente(id):
    """Elimina un paciente por ID"""
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()

def gestionar_pacientes():
    """Vista para gestionar pacientes"""
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        crear_paciente(nombre, edad, direccion, telefono)
        return redirect(url_for('pacientes'))
    
    pacientes = obtener_pacientes()
    return render_template('pacientes/pacientes.html', pacientes=pacientes)

def eliminar_paciente_route(id):
    """Ruta para eliminar paciente"""
    eliminar_paciente(id)
    return redirect(url_for('pacientes'))
