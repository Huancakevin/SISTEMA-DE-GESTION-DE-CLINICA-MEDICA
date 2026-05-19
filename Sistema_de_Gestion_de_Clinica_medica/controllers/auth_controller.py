from flask import render_template, request, redirect, url_for, session
from models import db, Usuario

def login():
    """Mostrar página de login"""
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')
        
        # Validar credenciales contra la base de datos
        usuario_obj = Usuario.query.filter_by(usuario=usuario, contraseña=contraseña).first()
        
        if usuario_obj:
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Usuario o contraseña incorrectos')
    
    # Si ya está logueado, redirigir al inicio
    if 'usuario' in session:
        return redirect(url_for('index'))
    
    return render_template('login.html')

def logout():
    """Cerrar sesión"""
    session.pop('usuario', None)
    return redirect(url_for('ruta_login'))
