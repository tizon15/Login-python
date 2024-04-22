class User:
    """ Definition of the constructor"""
    def __init__(self, username, password, role):
        self.__username = username
        self.__password = password
        self.__role = role

    def get_username(self):
        """ Public function to return the username """
        return self.__username

    def get_password(self):
        """Public function to return the password"""
        return self.__password

    def get_role(self):
        """Public function to return the role"""
        return self.__role

    def set_username(self, username):
        """Public function to set the username"""
        self.__username = username

    def set_password(self, password):
        """Public function to set the password"""
        self.__password = password

    def set_role(self, role):
        """Public function to set the role"""
        self.__role = role
