class Suspect:
    def __init__(self , SuspectID , FirstName, LastName,  DateOfBirth,  Gender, ContactInformation):
        self.__SuspectID =  SuspectID 
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__DateOfBirth = DateOfBirth
        self.__Gender = Gender
        self.__ContactInformation = ContactInformation


        
# Getters
    def get_SuspectID(self):
        return self.__SuspectID
    
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
    def set_SuspectID(self, SuspectID):
        self.__SuspectID = SuspectID
    
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