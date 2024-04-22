from replit import db


def get_list_of_users():
  return print(f"Usuarios: {list(db.keys())}\n")


def get_user(username):
  return db.get(username)


def add_user(user):
  db[user.get_username()] = {
      'username': user.get_username(),
      'password': user.get_password(),
      'role': user.get_role()
  }


def validate(username, password):
  user = db[username]
  print(user)
  if user and user['password'] == password:
    return True
  return False


def edit_user(username, new_user):
  if username in db:
    delete_user(username)
    add_user(new_user)
    print(f"User {db[new_user.get_username()]['username']} update.")
  else:
    print('el usuario no esta en la base de datos')


def delete_user(username):
  try:
    del db[username]
  except:
    print("the user is not in database")
