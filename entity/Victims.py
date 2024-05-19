class victim:
    def __init__(self, VictimID , FirstName, LastName, DateOfBirth, Gender ,ContactInformation ): 
        self.__FirstName =  FirstName
        self.__VictimID = VictimID
        self.__LastName =LastName
        self.__DateOfBirth = DateOfBirth
        self.__Gender = Gender
        self.__ContactInformation = ContactInformation


    # Getters
    def get_VictimID(self):
        return self.__VictimID
    
    def get_FirstName(self):
        return self.__FirstName
    
    def get_LastName(self):
        return self.__LastName
    
    def get_DateOfBirth(self):
        return self.__DateOfBirth
    
    def get_Gender(self):
        return self.__Gender
    
    def get_ContactInformation(self):
        return self.__ContactInformation

# Setters
    def set_VictimID(self, VictimID):
        self.__VictimID = VictimID
    
    def set_FirstName(self, FirstName):
        self.__FirstName = FirstName
    
    def set_LastName(self, LastName):
        self.__LastName = LastName
    
    def set_DateOfBirth(self, DateOfBirth):
        self.__DateOfBirth = DateOfBirth
    
    def set_Gender(self, Gender):
        self.__Gender = Gender
    
    def set_ContactInformation(self, ContactInformation):
        self.__ContactInformation = ContactInformation