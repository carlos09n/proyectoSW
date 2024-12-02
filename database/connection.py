from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cambia la conexión según tu base de datos
DATABASE_URL = "mssql+pyodbc://LAPTOP-HIA2CC4G\\SQLEXPRESS/BANCO?driver=SQL+Server+Native+Client+11.0"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Uso de SQLAlchemy para inicializar la base
def init_db():
    from ..models.models import Base
    Base.metadata.create_all(engine)
