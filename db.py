from replit import db


def get_list_of_users():
    """return a list of users"""
    return print(f"Usuarios: {list(db.keys())}")


def add_user(user):
    """add a user to the list of users"""
    db[user.get_username()] = {
        'username': user.get_username(),
        'password': user.get_password(),
        'role': user.get_role()
    }


def validate(username, password):
    """checks if we have a username and password correct"""
    user = db.get(username)
    if user and user['password'] == password:
        return True
    return False


def edit_user(user, new_user):
    """checks if the user is already in the list of users and edits it with the new user"""
    if user in db.keys() and user == new_user.get_username():
        delete_user(user)
        add_user(new_user)
        print(f"User {db[user.get_username()]['username']} update.")
    else:
        print('el usuario no esta en la base de datos')


def delete_user(username):
    """Deletes a user from the database"""
    try:
        del db[username]
        print(f"User {username} deleted.")
    except:
        print("the user is not in database")
