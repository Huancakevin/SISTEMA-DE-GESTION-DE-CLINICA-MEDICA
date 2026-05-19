from flask import render_template, request, redirect, url_for
from models import db, Medico

def obtener_medicos():
    """Obtiene todos los médicos"""
    return Medico.query.all()

def crear_medico(nombre, especialidad, telefono, correo):
    """Crea un nuevo médico"""
    if nombre and especialidad and telefono and correo:
        nuevo_medico = Medico(nombre=nombre, especialidad=especialidad, telefono=telefono, correo=correo)
        db.session.add(nuevo_medico)
        db.session.commit()
        return True
    return False

def eliminar_medico(id):
    """Elimina un médico por ID"""
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()

def gestionar_medicos():
    """Vista para gestionar médicos"""
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        especialidad = request.form.get('especialidad')
        telefono = request.form.get('telefono')
        correo = request.form.get('correo')
        crear_medico(nombre, especialidad, telefono, correo)
        return redirect(url_for('medicos'))
    
    medicos = obtener_medicos()
    return render_template('medicos/medicos.html', medicos=medicos)

def eliminar_medico_route(id):
    """Ruta para eliminar médico"""
    eliminar_medico(id)
    return redirect(url_for('medicos'))
