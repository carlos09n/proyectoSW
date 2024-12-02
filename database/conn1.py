# import pyodbc

# # Configuración de conexión a la base de datos
# DB_CONFIG = {
#     'driver': '{SQL Server}',
#     'server': 'LAPTOP-HIA2CC4G\\SQLEXPRESS',
#     'database': 'BANCO',
#     'trusted_connection': 'yes'
# }

# def get_db_connection():
#     """Establece y devuelve una conexión a la base de datos."""
#     try:
#         connection = pyodbc.connect(
#             f"DRIVER={DB_CONFIG['driver']};"
#             f"SERVER={DB_CONFIG['server']};"
#             f"DATABASE={DB_CONFIG['database']};"
#             f"Trusted_Connection={DB_CONFIG['trusted_connection']};"
#         )
#         return connection
#     except Exception as ex:
#         print(f"Error al conectar a la base de datos: {ex}")
#         return None
