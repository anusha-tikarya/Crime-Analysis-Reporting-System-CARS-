class Incident:
    def __init__(self, IncidentID, IncidentType, IncidentDate, Location_Latitude,Location_Longitude, Description, Status, VictimID , SuspectId):
        self.__IncidentID = IncidentID
        self.__IncidentType= IncidentType
        self.__IncidentDate=IncidentDate
        #self.__Location = Location
        self.Location_Longitude = Location_Longitude
        self.Location_Latitude = Location_Latitude
        self.__Description=Description
        self.__Status=Status
        self.__VictimID=VictimID
        self.__SuspectId=SuspectId
        
 # Getters
    def get_IncidentID(self):
        return self.__IncidentID

    def get_IncidentType(self):
        return self.__IncidentType

    def get_IncidentDate(self):
        return self.__IncidentDate

    def get_Location_Latitude(self):
        return self.__Location_Latitude

    def get_Location_Longitude(self):
        return self.__Location_Longitude

    def get_Description(self):
        return self.__Description

    def get_Status(self):
        return self.__Status

    def get_VictimID(self):
        return self.__VictimID

    def get_SuspectId(self):
        return self.__SuspectId

# Setters
    def set_IncidentID(self, IncidentID):
        self.__IncidentID = IncidentID

    def set_IncidentType(self, IncidentType):
        self.__IncidentType = IncidentType

    def set_IncidentDate(self, IncidentDate):
        self.__IncidentDate = IncidentDate

    def set_Location_Latitude(self, Location_Latitude):
        self.__Location_Latitude = Location_Latitude

    def set_Location_Longitude(self, Location_Longitude):
        self.__Location_Longitude = Location_Longitude

    def set_Description(self, Description):
        self.__Description = Description

    def set_Status(self, Status):
        self.__Status = Status

    def set_VictimID(self, VictimID):
        self.__VictimID = VictimID

    def set_SuspectId(self, SuspectId):
        self.__SuspectId = SuspectId