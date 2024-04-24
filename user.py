class User:

  def __init__(self, username, password, role, notes, scheadule):
    self.__username = username
    self.__password = password
    self.__role = role
    self.__notes = notes
    self.__scheadule = scheadule

  def get_username(self):
    return self.__username

  def get_password(self):
    return self.__password

  def get_role(self):
    return self.__role

  def get_notes(self):
    return self.__notes

  def get_scheadule(self):
    return self.__scheadule

  def set_username(self, username):
    self.__username = username

  def set_password(self, password):
    self.__password = password

  def set_role(self, role):
    self.__role = role

  def set_notes(self, notes):
    self.__notes = notes

  def set_scheadule(self, scheadule):
    self.__scheadule = scheadule
