from flask import render_template, request, redirect, url_for
from models import db, Consulta, Medico, Paciente
from datetime import datetime

def obtener_consultas(fecha_filtro=None):
    """Obtiene consultas, opcionalmente filtradas por fecha"""
    if fecha_filtro:
        fecha_obj = datetime.strptime(fecha_filtro, '%Y-%m-%d').date()
        return Consulta.query.filter_by(fecha=fecha_obj).all()
    return Consulta.query.all()

def crear_consulta(fecha_str, diagnostico, tratamiento, id_medico, id_paciente):
    """Crea una nueva consulta"""
    if fecha_str and diagnostico and tratamiento and id_medico and id_paciente:
        fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        nueva_consulta = Consulta(
            fecha=fecha_obj, diagnostico=diagnostico, tratamiento=tratamiento,
            id_medico=id_medico, id_paciente=id_paciente
        )
        db.session.add(nueva_consulta)
        db.session.commit()
        return True
    return False

def eliminar_consulta(id):
    """Elimina una consulta por ID"""
    consulta = Consulta.query.get_or_404(id)
    db.session.delete(consulta)
    db.session.commit()

def gestionar_consultas():
    """Vista para gestionar consultas"""
    if request.method == 'POST':
        fecha_str = request.form.get('fecha')
        diagnostico = request.form.get('diagnostico')
        tratamiento = request.form.get('tratamiento')
        id_medico = request.form.get('id_medico')
        id_paciente = request.form.get('id_paciente')
        crear_consulta(fecha_str, diagnostico, tratamiento, id_medico, id_paciente)
        return redirect(url_for('consultas'))
    
    fecha_filtro = request.args.get('filtro_fecha')
    consultas = obtener_consultas(fecha_filtro)
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return render_template('consultas/consultas.html', consultas=consultas, medicos=medicos, pacientes=pacientes)

def eliminar_consulta_route(id):
    """Ruta para eliminar consulta"""
    eliminar_consulta(id)
    return redirect(url_for('consultas'))
