from flask import Flask, render_template
from models import db, Usuario
from controllers.pacientes_controller import gestionar_pacientes, eliminar_paciente_route
from controllers.medicos_controller import gestionar_medicos, eliminar_medico_route
from controllers.consultas_controller import gestionar_consultas, eliminar_consulta_route
from controllers.auth_controller import login, logout
from controllers.usuarios_controller import registrar_usuario
from controllers.reporte_controller import generar_reporte
from controllers.decoradores import requerir_login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'clave_secreta_para_flash_messages'

db.init_app(app)

with app.app_context():
    try:
        db.create_all()
        usuario_admin = Usuario.query.filter_by(usuario='admin').first()
        if not usuario_admin:
            admin = Usuario(usuario='admin', contraseña='123456', correo='admin@clinica.com')
            db.session.add(admin)
            db.session.commit()
            print("Usuario admin creado automáticamente")
    except Exception as e:
        print(f"Nota: {e}")

@app.route('/login', methods=['GET', 'POST'])
def ruta_login():
    return login()

@app.route('/logout')
def ruta_logout():
    return logout()

@app.route('/registro', methods=['GET', 'POST'])
def ruta_registro():
    return registrar_usuario()

@app.route('/')
@requerir_login
def index():
    return render_template('base.html')

@app.route('/reporte')
@requerir_login
def ruta_reporte():
    return generar_reporte()

@app.route('/pacientes', methods=['GET', 'POST'])
@requerir_login
def pacientes():
    return gestionar_pacientes()

@app.route('/eliminar_paciente/<int:id>')
@requerir_login
def eliminar_paciente(id):
    return eliminar_paciente_route(id)

@app.route('/medicos', methods=['GET', 'POST'])
@requerir_login
def medicos():
    return gestionar_medicos()

@app.route('/eliminar_medico/<int:id>')
@requerir_login
def eliminar_medico(id):
    return eliminar_medico_route(id)

@app.route('/consultas', methods=['GET', 'POST'])
@requerir_login
def consultas():
    return gestionar_consultas()

@app.route('/eliminar_consulta/<int:id>')
@requerir_login
def eliminar_consulta(id):
    return eliminar_consulta_route(id)

if __name__ == '__main__':
    app.run(debug=True)
