class LawEnforcementAgency:
    def __init__(self, agencyID, agencyName, jurisdiction, contactInformation, officers):
        self.__agencyID = agencyID
        self.__agencyName = agencyName
        self.__jurisdiction = jurisdiction
        self.__contactInformation = contactInformation
        self.__officers = officers

  # Getter for agencyID
    def get_agencyID(self):
        return self.__agencyID

    # Getter for agencyName
    def get_agencyName(self):
        return self.__agencyName

    # Getter for jurisdiction
    def get_jurisdiction(self):
        return self.__jurisdiction

    # Getter for contactInformation
    def get_contactInformation(self):
        return self.__contactInformation

    # Getter for officers
    def get_officers(self):
        return self.__officers

 #Setter   
   # Setter for agencyID
    def set_agencyID(self, agencyID):
        self.__agencyID = agencyID
    # Setter for agencyName
    def set_agencyName(self, agencyName):
        self.__agencyName = agencyName

    # Setter for jurisdiction
    def set_jurisdiction(self, jurisdiction):
        self.__jurisdiction = jurisdiction


    # Setter for contactInformation
    def set_contactInformation(self, contactInformation):
        self.__contactInformation = contactInformation


    # Setter for officers
    def set_officers(self, officers):
        self.__officers = officers