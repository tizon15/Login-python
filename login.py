import getpass
import db

class User:
  def __init__(self, name, password, email, rol):
    self.name = name
    self.password = password
    self.email = email
    self.rol = rol
    
    def validateUser(newUser):
        adminUser = User("pepe", "pepe", "pepe@gmail.com", "admin")
        newUser.name = self.name
    

loginOrNot = input("Quieres crear un nuevo usuario?")
def login(loginOrNot):
    if(loginOrNot == "yes" or loginOrNot == "si"):
        username = input("Cual va a ser el nombre de usuario: ")
        password = getpass.getpass(prompt="Cual va a ser la contraseña de usuario: ")
        email = input("Cual va a ser el email de usuario: ")
        rol = input("Cual va a ser el rol del usuario: ")
        newUser = User(username, password, email, rol)
        print(newUser.name, newUser.email, newUser.rol)
    else :
        username = input("Enter your username: ")
        password = getpass.getpass(prompt="Enter your password: ")
        user = db.validar_usuario(username, password)
        print(user)
login(loginOrNot)
