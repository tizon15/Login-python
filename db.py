import psycopg2

def conectar_db():
    conexion = psycopg2.connect(
        host="localhost",
        database="nombre_base_datos",
        user="usuario_db",
        password="contrasena_db"
    )
    return conexion

def validar_usuario(user, contrasena):
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, rol
        FROM usuarios
        WHERE user = %s AND contrasena = %s
    """, (user, contrasena))

    usuario = cursor.fetchone()

    conexion.close()
    return usuario