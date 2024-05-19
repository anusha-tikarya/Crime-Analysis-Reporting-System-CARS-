class Incident:
    def __init__(self, incidentID, incidentType, incidentDate, Location_Latitude,Location_Longitude, Description, Status, VictimID , SuspectId):
        self.incidentID = incidentID
        self.incidentType= incidentType
        self.incidentDate=incidentDate
        #self.__Location = Location
        self.Location_Longitude = Location_Longitude
        self.Location_Latitude = Location_Latitude
        self.Description=Description
        self.Status=Status
        self.VictimID=VictimID
        self.SuspectId=SuspectId
        
#  # Getters
#     def get_IncidentID(self):
#         return self.__IncidentID

#     def get_IncidentType(self):
#         return self.__IncidentType

#     def get_IncidentDate(self):
#         return self.__IncidentDate

#     def get_Location_Latitude(self):
#         return self.__Location_Latitude

#     def get_Location_Longitude(self):
#         return self.__Location_Longitude

#     def get_Description(self):
#         return self.__Description

#     def get_Status(self):
#         return self.__Status

#     def get_VictimID(self):
#         return self.__VictimID

#     def get_SuspectId(self):
#         return self.__SuspectId

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