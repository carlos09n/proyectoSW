from sqlalchemy import Column, Integer, String, Float, Date, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Administrador(Base):
    __tablename__ = 'ADMINISTRADOR'
    id_admin = Column('ID_ADMINISTRADR', Integer, primary_key=True)
    nombre = Column('NOMBRE', String(50), nullable=False)
    correo = Column('CORREO', String(100), nullable=False)
    fecha_registro = Column('FECHA_REGISTRO', Date, default=func.current_date(), nullable=False)
    estado = Column('ESTADO', String(50))

class Cliente(Base):
    __tablename__ = 'CLIENTE'
    id_cliente = Column('ID_CLIENTE', Integer, primary_key=True)
    nombre = Column('NOMBRE', String(50), nullable=False)
    correo = Column('CORREO', String(100))
    fecha_registro = Column('FECHA_REGISTRO', Date, default=func.current_date())
    saldo = Column('SALDO', Float, nullable=False)
    tipo_cuenta = Column('TIPO_CUENTA', String(50))
    estado = Column('ESTADO', String(50))

class Auditor(Base):
    __tablename__ = 'AUDITOR'
    id_auditor = Column('ID_AUDITOR', Integer, primary_key=True)
    nombre = Column('NOMBRE', String(50), nullable=False)
    correo = Column('CORREO', String(100), nullable=False)
    fecha_registro = Column('FECHA_REGISTRO', Date, default=func.current_date(), nullable=False)
    estado = Column('ESTADO', String(50))

class SoporteTecnico(Base):
    __tablename__ = 'SOPORTE_TECNICO'
    id_soporte = Column('ID_SOPORTE_TECNICO', Integer, primary_key=True)
    nombre = Column('NOMBRE', String(50), nullable=False)
    correo = Column('CORREO', String(100), nullable=False)
    fecha_registro = Column('FECHA_REGISTRO', Date, default=func.current_date(), nullable=False)
    estado = Column('ESTADO', String(50))

class Actividad(Base):
    __tablename__ = 'ACTIVIDAD'
    id_actividad = Column('ID_ACTIVIDAD', Integer, primary_key=True)
    descripcion = Column('DESCRIPCION', String(50), nullable=False)
    tipo_usuario = Column('TIPO_USUARIO', String(50), nullable=False)
    fecha_registro = Column('FECHA_REGISTRO', Date, default=func.current_date(), nullable=False)
    resultado = Column('RESULTADO', String(50))
