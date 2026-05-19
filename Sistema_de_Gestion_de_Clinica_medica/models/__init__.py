from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Medico(db.Model):
    __tablename__ = 'medicos'
    id_medico = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    
    # Relación: Un médico puede tener muchas consultas
    consultas = db.relationship('Consulta', backref='medico', lazy=True, cascade="all, delete-orphan")

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    id_paciente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    
    # Relación: Un paciente puede tener muchas consultas
    consultas = db.relationship('Consulta', backref='paciente', lazy=True, cascade="all, delete-orphan")

class Consulta(db.Model):
    __tablename__ = 'consultas'
    id_consulta = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    diagnostico = db.Column(db.Text, nullable=False)
    tratamiento = db.Column(db.Text, nullable=False)
    
    # Claves foráneas
    id_medico = db.Column(db.Integer, db.ForeignKey('medicos.id_medico'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id_paciente'), nullable=False)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), nullable=False, unique=True)
    contraseña = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
