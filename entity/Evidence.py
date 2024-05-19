class Evidence:
    def __init__(self, evidenceID, description, locationFound, incidentID):
        self.__evidenceID = evidenceID
        self.__description = description
        self.__locationFound = locationFound
        self.__incidentID = incidentID

# Getters
    def get_evidenceID(self):
        return self.__evidenceID

    def get_description(self):
        return self.__description

    def get_locationFound(self):
        return self.__locationFound

    def get_incidentID(self):
        return self.__incidentID

# Setters
    def set_evidenceID(self, evidenceID):
        self.__evidenceID = evidenceID

    def set_description(self, description):
        self.__description = description

    def set_locationFound(self, locationFound):
        self.__locationFound = locationFound

    def set_incidentID(self, incidentID):
        self.__incidentID = incidentID