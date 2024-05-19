class Officer:
    def __init__(self, officerID, firstName, lastName, badgeNumber, rank, contactInformation, agencyID):
        self.__officerID = officerID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__badgeNumber = badgeNumber
        self.__rank = rank
        self.__contactInformation = contactInformation
        self.__agencyID = agencyID

 # Getters
    def get_officerID(self):
        return self.__officerID
    
    def get_firstName(self):
        return self.__firstName
    
    def get_lastName(self):
        return self.__lastName
    
    def get_badgeNumber(self):
        return self.__badgeNumber
    
    def get_rank(self):
        return self.__rank
    
    def get_contactInformation(self):
        return self.__contactInformation
    
    def get_agencyID(self):
        return self.__agencyID

# Setters
    def set_officerID(self, officerID):
        self.__officerID = officerID
    
    def set_firstName(self, firstName):
        self.__firstName = firstName
    
    def set_lastName(self, lastName):
        self.__lastName = lastName
    
    def set_badgeNumber(self, badgeNumber):
        self.__badgeNumber = badgeNumber
    
    def set_rank(self, rank):
        self.__rank = rank
    
    def set_contactInformation(self, contactInformation):
        self.__contactInformation = contactInformation
    
    def set_agencyID(self, agencyID):
        self.__agencyID = agencyID