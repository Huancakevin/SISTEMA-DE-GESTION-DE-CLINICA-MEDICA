from functools import wraps
from flask import session, redirect, url_for

def requerir_login(f):
    """Decorador para proteger rutas que requieren autenticación"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect(url_for('ruta_login'))
        return f(*args, **kwargs)
    return decorated_function
