class Report:
    def __init__(self, reportID, incidentID, reportingOfficer, reportDate, reportDetails, status):
        self.__reportID = reportID
        self.__incidentID = incidentID
        self.__reportingOfficer = reportingOfficer
        self.__reportDate = reportDate
        self.__reportDetails = reportDetails
        self.__status = status

  # Getters
    def get_reportID(self):
        return self.__reportID
    
    def get_incidentID(self):
        return self.__incidentID
    
    def get_reportingOfficer(self):
        return self.__reportingOfficer
    
    def get_reportDate(self):
        return self.__reportDate
    
    def get_reportDetails(self):
        return self.__reportDetails
    
    def get_status(self):
        return self.__status
    
    # Setters
    def set_reportID(self, reportID):
        self.__reportID = reportID
    
    def set_incidentID(self, incidentID):
        self.__incidentID = incidentID
    
    def set_reportingOfficer(self, reportingOfficer):
        self.__reportingOfficer = reportingOfficer
    
    def set_reportDate(self, reportDate):
        self.__reportDate = reportDate
    
    def set_reportDetails(self, reportDetails):
        self.__reportDetails = reportDetails
    
    def set_status(self, status):
        self.__status = status