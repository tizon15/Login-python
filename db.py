import psycopg2
from pymongo.mongo_client import MongoClient
def get_database():
    # CONNECTION_STRING = "mongodb+srv://tizon15:<2DwUe9wXB9YECCcQ>@cluster.mongodb.net/myFirstDatabase"
    CONNECTION_STRING = "mongodb+srv://tizon15:2DwUe9wXB9YECCcQ@cluster0.uioxur8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    db = client.get_database('Users')
    return db
    # Create the database for our example (we will use the same database throughout the tutorial
    # return client['Users']
  
  
   # Get the database
#    dbname = get_database()
    

# def conectar_db():
#     conexion = client.connect(
#         host="localhost",
#         database="nombre_base_datos",
#         user="usuario_db",
#         password="contrasena_db"
#     )
#     return conexion
def newUser(user, password, email, rol):
    dbname = get_database()
    collection_name = dbname["users"]
    nuevo_usuario = {
        "user": user,
        "email": email,
        "password": password,
        "rol": rol
    }

    collection_name.insert_one(nuevo_usuario)
def validar_usuario(user, password):
    dbname = get_database()
    collection_name = dbname["users"]

    usuario = collection_name.find_one({"correo": user, "contrasena": password})

    return usuario