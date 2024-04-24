from replit import db


# C = CRUD
def add_user(user):
  # key = user.get_username()
  db[user.get_username()] = {
      'username': user.get_username(),
      'password': user.get_password(),
      'role': user.get_role(),
      'notes': user.get_notes(),
      'scheadule': user.get_scheadule()
    
  }


# R = READ
def get_user(username):
  return db.get(username)


def get_list_of_users():
  return print(f"Usuarios: {list(db.keys())}\n")


# U = UPDATE
def edit_user(username, new_user):
  if username in db:
    delete_user(username)
    add_user(new_user)
    print(f"User {db[new_user.get_username()]['username']} update.")
  else:
    print('el usuario no esta en la base de datos')


# D = DELETE
def delete_user(username):
  try:
    del db[username]
  except:
    print("the user is not in database")


def validate_user(username, password):
  # TODO EXCEPCION SI EL USUARIO NO EXISTE
  user = db[username]
  if user and user['password'] == password:
    return True
  return False
