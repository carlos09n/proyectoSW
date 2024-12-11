from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base  # Asegúrate de usar la versión moderna

# Configura la URL de conexión de la base de datos
DATABASE_URL = "mssql+pyodbc://LAPTOP-HIA2CC4G\\SQLEXPRESS/BANCO?driver=SQL+Server+Native+Client+11.0"

# Motor de la base de datos
engine = create_engine(DATABASE_URL)

# Sesión
Session = sessionmaker(bind=engine)

# Declarative Base
Base = declarative_base()  # Define aquí `Base`

# Inicialización de la base de datos
def init_db():
    from models.models import Base  # Usa imports absolutos para evitar conflictos
    Base.metadata.create_all(engine)
