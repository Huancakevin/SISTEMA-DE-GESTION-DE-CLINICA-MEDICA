from flask import render_template
from models import Medico, Paciente, Consulta
from datetime import datetime

def generar_reporte():
    """Genera un reporte con todos los datos"""
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    consultas = Consulta.query.all()
    
    datos = {
        'medicos': medicos,
        'pacientes': pacientes,
        'consultas': consultas,
        'total_medicos': len(medicos),
        'total_pacientes': len(pacientes),
        'total_consultas': len(consultas)
    }
    
    return render_template('reporte.html', datos=datos, now=datetime.now())
