import getpass
import db

loginOrNot = input("Quieres crear un nuevo usuario?")
def login(loginOrNot):
    if(loginOrNot == "yes" or loginOrNot == "si"):
        username = input("Cual va a ser el nombre de usuario: ")
        password = getpass.getpass(prompt="Cual va a ser la contraseña de usuario: ")
        email = input("Cual va a ser el email de usuario: ")
        rol = input("Cual va a ser el rol del usuario: ")
        newUser = db.newUser(username, password, email, rol)
        print(newUser)
    else :
        username = input("Enter your username: ")
        password = getpass.getpass(prompt="Enter your password: ")
        user = db.validar_usuario(username, password)
        print(user)
login(loginOrNot)
