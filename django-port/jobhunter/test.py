class Myclass:
    def __init__(self, name):
        self.__name=name
        self.__type='Myclass'
        self.__number=420
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name=value
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self,value):
        self.__number=value
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, value):
        self.__type=value
