class Incident:
    def __init__(self, incidentID, incidentType, incidentDate, Location_Latitude,Location_Longitude, description, status, victimID , suspectID):
        self.__incidentID = incidentID
        self.__incidentType= incidentType
        self.__incidentDate=incidentDate
        #self.__Location = Location
        self.__Location_Longitude = Location_Longitude
        self.__Location_Latitude = Location_Latitude
        self.__description=description
        self.__status=status
        self.__victimID=victimID
        self.__suspectID=suspectID
        
 # Getters
    def get_incidentID(self):
        return self.__incidentID

    def get_incidentType(self):
        return self.__incidentType

    def get_incidentDate(self):
        return self.__incidentDate

    def get_Location_Latitude(self):
        return self.__Location_Latitude

    def get_Location_Longitude(self):
        return self.__Location_Longitude

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def get_victimID(self):
        return self.__victimID

    def get_suspectID(self):
        return self.__suspectID

# Setters
    def set_IncidentID(self, incidentID):
        self.incidentID = incidentID

    def set_IncidentType(self, incidentType):
        self.incidentType = incidentType

    def set_IncidentDate(self, IncidentDate):
        self.incidentDate = IncidentDate

    def set_Location_Latitude(self, Location_Latitude):
        self.Location_Latitude = Location_Latitude

    def set_Location_Longitude(self, Location_Longitude):
        self.Location_Longitude = Location_Longitude

    def set_Description(self, Description):
        self.Description = Description

    def set_Status(self, Status):
        self.Status = Status

    def set_VictimID(self, VictimID):
        self.VictimID = VictimID

    def set_SuspectId(self, SuspectId):
        self.SuspectId = SuspectId