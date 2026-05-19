from flask import render_template, request, redirect, url_for, session
from models import db, Usuario

def registrar_usuario():
    """Mostrar página de registro y procesar registro"""
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')
        confirmar = request.form.get('confirmar')
        correo = request.form.get('correo')

        if not usuario or not contraseña or not correo:
            return render_template('registro.html', error='Todos los campos son obligatorios')
        
        if contraseña != confirmar:
            return render_template('registro.html', error='Las contraseñas no coinciden')
        
        if len(contraseña) < 6:
            return render_template('registro.html', error='La contraseña debe tener al menos 6 caracteres')

        usuario_existente = Usuario.query.filter_by(usuario=usuario).first()
        if usuario_existente:
            return render_template('registro.html', error='El usuario ya existe')

        nuevo_usuario = Usuario(usuario=usuario, contraseña=contraseña, correo=correo)
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        return render_template('registro.html', exito='Usuario registrado exitosamente. Redirigiendo al login...')
    
    return render_template('registro.html')

def obtener_usuarios():
    """Obtiene todos los usuarios"""
    return Usuario.query.all()

def eliminar_usuario(id):
    """Elimina un usuario por ID"""
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
