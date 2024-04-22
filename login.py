import getpass
import db
from user import User


def login():
  user = User("", "", "")
  # Pedir al usuario que ingrese los datos del nuevo usuario
  print("Bienvenido al sistema de registro de usuarios")
  if (input("¿Tiene usuario? (s/n): ").lower() == "s"):
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = getpass.getpass(prompt="Ingrese la contraseña: ")
    if (db.validate(usuario, contraseña)):
      user.set_username(db.get_user(usuario)['username'])
      user.set_password(db.get_user(usuario)['password'])
      user.set_role(db.get_user(usuario)['role'])
      print("¡Bienvenido! ¿Qué desea hacer?")
      display_menu(user)
    else:
      print("Usuario o contraseña incorrectos")
  else:
    if (input("¿Desea registrarse? (s/n): ").lower() == "s"):
      agregar_usuario()
      display_menu(user)
    else:
      print("Hasta pronto")


def display_menu(user):
  while True:
    match int(
        input(
            "1. Agregar usuario\n2. Editar usuario\n3. Eliminar usuario\n4. Ver usuarios\n5. Salir\n"
        )):
      case 1:
        agregar_usuario()
      case 2:
        print("que valor quieres editar")
        editar_usuario()
      case 3:
        username = input("Ingrese el nombre de usuario a eliminar: ")
        db.delete_user(username)
        print(f"User {username} deleted.")
      case 4:
        db.get_list_of_users()
      case 5:
        print("Hasta pronto")
        break
      case _:
        print('Opcion inválida')


def agregar_usuario():
  # Creamos los inputs en una funcion para que quede mas limpio el codigo
  new_user = User("", "", "")
  new_user.set_username(input("Ingrese el nombre del usuario: "))
  new_user.set_password(getpass.getpass(prompt="Ingrese la contraseña: "))
  new_user.set_role(input("Ingrese el rol del usuario: "))
  db.add_user(new_user)
  print(f"Usuario {new_user.get_username()} añadido.\n")
  print("¿Quieres gestionar algo más?\n")


def editar_usuario():
  match int(
      input("1. nombre usuario\n2. cambiar contraseña\n3. cambiar rol\n")):
    case 1:
      username = input("Ingrese el nombre del usuario que quiere editar: ")
      get_user = db.get_user(username)
      new_user = User(get_user['username'], get_user['password'],
                      get_user['role'])
      new_user.set_username(input("Ingrese el nuevo nombre de usuario: "))
      db.edit_user(username, new_user)
    case 2:
      username = input("Ingrese el nombre del usuario que quiere editar: ")
      get_user = db.get_user(username)
      new_user = User(get_user['username'], get_user['password'],
                      get_user['role'])
      new_user.set_username(
          getpass.getpass(prompt="Ingrese la nueva contraseña: "))
      db.edit_user(username, new_user)
    case 3:
      username = input("Ingrese el nombre del usuario que quiere editar: ")
      get_user = db.get_user(username)
      new_user = User(get_user['username'], get_user['password'],
                      get_user['role'])
      new_user.set_role(input("Ingrese el nuevo rol: "))

      db.edit_user(username, new_user)


def main():
  """Entry point for the application."""
  login()


# Ejemplo de uso en la terminal
if __name__ == "__main__":
  main()
