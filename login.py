import getpass
from user import User
import db

def set_user(user, usuario):
  user.set_username(db.get_user(usuario)['username'])
  user.set_password(db.get_user(usuario)['password'])
  user.set_role(db.get_user(usuario)['role'])
  user.set_notes(db.get_user(usuario)['notes'])
  user.set_scheadule(db.get_user(usuario)['scheadule'])
  return user

def login():
  user = User("", "", "", "", "")
  # Pedir al usuario que ingrese los datos del nuevo usuario
  print("Bienvenido al sistema de registro de usuarios")
  if (input("¿Tiene usuario? (s/n): ").lower() == "s"):
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = getpass.getpass(prompt="Ingrese la contraseña: ")
    if (db.validate_user(usuario, contraseña)):
      user = set_user(user, usuario)
      print(f"¡Bienvenido! {user.get_username()} ¿Qué desea hacer?")
      if user.get_role() == "profesor":
        display_menu_profesor(user)
      elif user.get_role() == "alumno":
        display_menu_alumno(user)
    else:
      print("Usuario o contraseña incorrectos")
  else:
    if (input("¿Desea registrarse? (s/n): ").lower() == "s"):
      user = agregar_usuario()
      print(f"Bienvenido! {user.get_username()} ")
      if user.get_role() == "profesor":
        display_menu_profesor(user)
      else:
        display_menu_alumno(user)
    else:
      print("Hasta pronto")



  
def display_menu_profesor(user):
  while True:
        try:
          choice = int(input(
              "1. Agregar usuario\n2. Editar usuario\n3. Eliminar usuario\n4. Ver usuarios\n5. Salir\n"
          ))
          if choice == 1:
              agregar_usuario()
          elif choice == 2:
              print("¿Qué valor quieres editar?")
              editar_usuario(user)
          elif choice == 3:
              username = input("Ingrese el nombre de usuario a eliminar: ")
              db.delete_user(username)
              print(f"Usuario {username} eliminado.")
          elif choice == 4:
              db.get_list_of_users()
          elif choice == 5:
              print("Hasta pronto")
              break
          else:
              print("Opción inválida")
        except ValueError:
          print("Por favor, ingresa un número válido.")


def display_menu_alumno(user):
  while True:
    match int(
        input("1. Editar usuario\n2. Ver notas\n3. Ver horario\n5. Salir\n")):
      case 1:
        print("que valor quieres editar")
        editar_usuario(user)
      case 2:
        notes = db.get_user(user.get_username())
        print(f"tus notas son {notes['notes']}")
      case 4:
        scheadule = db.get_user(user.get_username())
        print(f"tus horario es {scheadule['scheadule']}")
      case 5:
        print("Hasta pronto")
        break
      case _:
        print('Opcion inválida')


def agregar_usuario():
  # Creamos los inputs en una funcion para que quede mas limpio el codigo
  new_user = User("", "", "", "", "")
  new_user.set_username(input("Ingrese el nombre del usuario: "))
  new_user.set_password(getpass.getpass(prompt="Ingrese la contraseña: "))
  new_user.set_role(input("Ingrese el rol del usuario: "))
  db.add_user(new_user)
  print(f"Usuario {new_user.get_username()} añadido.\n")
  print("¿Quieres gestionar algo más?\n")
  return new_user


def editar_usuario(user):
  match int(
      input(
          "1. nombre usuario\n2. cambiar contraseña\n3. cambiar rol\n4. cambiar nota\n5. cambiar horario\n"
      )):
    case 1:
      username = input("Ingrese el nombre del usuario que quiere editar: ")
      get_user = db.get_user(username)
      new_user = User(get_user['username'], get_user['password'],
                      get_user['role'], get_user['notes'],
                      get_user['scheadule'])
      new_user.set_username(input("Ingrese el nuevo nombre de usuario: "))
      db.edit_user(username, new_user)
    case 2:
      username = input("Ingrese el nombre del usuario que quiere editar: ")
      get_user = db.get_user(username)
      new_user = User(get_user['username'], get_user['password'],
                      get_user['role'], get_user['notes'],
                      get_user['scheadule'])
      new_user.set_username(
          getpass.getpass(prompt="Ingrese la nueva contraseña: "))
      db.edit_user(username, new_user)
    case 3:
      if (user.get_role() == "profesor"):
        username = input("Ingrese el nombre del usuario que quiere editar: ")
        get_user = db.get_user(username)
        new_user = User(get_user['username'], get_user['password'],
                        get_user['role'], get_user['notes'],
                        get_user['scheadule'])
        new_user.set_role(input("Ingrese el nuevo rol: "))
        db.edit_user(username, new_user)
      else:
        print("No tienes permisos para editar roles")
    case 4:
      if (user.get_role() == "profesor"):
        username = input("Ingrese el nombre del usuario que quiere editar: ")
        get_user = db.get_user(username)
        new_user = User(get_user['username'], get_user['password'],
                        get_user['role'], get_user['notes'],
                        get_user['scheadule'])
        new_user.set_notes(input("Ingrese la nueva nota: "))
        db.edit_user(username, new_user)
      else:
        print("No tienes permisos para editar las notas")
    case 5:
      if (user.get_role() == "profesor"):
        username = input("Ingrese el nombre del usuario que quiere editar: ")
        get_user = db.get_user(username)
        new_user = User(get_user['username'], get_user['password'],
                        get_user['role'], get_user['notes'],
                        get_user['scheadule'])
        new_user.set_role(input("Ingrese el nuevo horario: "))

        db.edit_user(username, new_user)
      else:
        print("No tienes permisos para editar el horario")

def main():
  """Entry point for the application."""
  login()


# Ejemplo de uso en la terminal
if __name__ == "__main__":
  main()
