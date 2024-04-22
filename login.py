import getpass
from user import User
import db


def login():
    """ function to start the process of login"""
    print("Bienvenido al sistema de registro de usuarios")
    if input("¿Tiene usuario? (s/n)").lower() == "s":
        usuario = input("Ingrese el nombre de usuario: ")
        contraseña = getpass.getpass(prompt="Ingrese la contraseña: ")
        if db.validate(usuario, contraseña):
            print("¡Bienvenido! ¿Qué desea hacer?")
            match int(
                input(
                    '1. Agregar usuario\n2. Editar usuario\n3. Eliminar usuario\n4. Ver usuarios\n5. Salir\n'
                )):
                case 1:
                    agregar_usuario()
                case 2:
                    print("que valor quieres editar")
                    editar_usuario(usuario, contraseña)
                case 3:
                    username = input("Ingrese el nombre de usuario a eliminar: ")
                    db.delete_user(username)
                case 4:
                    db.get_list_of_users()
                case _:
                    print("Hasta pronto")
        else:
            print("Usuario o contraseña incorrectos")
    else:
        if input("¿Desea registrarse? (s/n)").lower() == "s":
            agregar_usuario()
        else:
            print("Hasta pronto")


def agregar_usuario():
    """create the inputs of the consoles and with the retrun create the new user"""
    # Creamos los inputs en una funcion para que quede mas limpio el codigo
    nombre = input("Ingrese el nombre del usuario: ")
    password = getpass.getpass(prompt="Ingrese la contraseña: ")
    rol = input("Ingrese el rol del usuario: ")
    user = User(nombre, password, rol)
    db.add_user(user)
    print(f"User {user.get_username()} added to the database.")

def editar_usuario(usuario, password):
    """"We ask the user which parameter wants to edit"""
    match int(
        input(
            "1. nombre usuario\n2. cambiar contraseña\n3. cambiar rol\n")
    ):
        case "1":
            new_username = input("Ingrese el nuevo de usuario: ")
            new_user = User(new_username, password,
                            db.db.get(usuario)['role'])
            db.edit_user(usuario, new_user)
        case "2":
            new_password = input("Ingrese la nueva contraseña: ")
            new_user = User(usuario, new_password,
                            db.db.get(usuario)['role'])
            db.edit_user(usuario, new_user)
        case "3":
            new_role = input("Ingrese el nuevo rol: ")
            new_user = User(usuario, password, new_role)
            db.edit_user(usuario, new_user)

# Ejemplo de uso en la terminal
if __name__ == "__main__":
    login()
