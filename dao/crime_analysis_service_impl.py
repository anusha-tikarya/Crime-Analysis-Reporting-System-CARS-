# from typing import Collection
from datetime import datetime
from entity.Incidents import Incident
from entity.Cases import Case
from entity.Reports import Report
from dao.i_crime_analysis_service import ICrimeAnalysisService
from datetime import datetime
from util.db_conn import DBConnection
from exception.incident_numbernot_found_exception import incident_number_not_found_exception


class crime_analysis_service_impl(ICrimeAnalysisService,DBConnection):
    def createIncident(self, incident:Incident):
        try:
            self.cursor.execute(
                "INSERT INTO Incidents (incidentID, incidentType, incidentDate,Location_Longitude,Location_Latitude,description,status,victimID,suspectID) VALUES (?, ?, ?,?,?,?,?, ?, ?)",
                (incident.get_incidentID(), incident.get_incidentDate(), incident.get_incidentDate(),incident.get_Location_Longitude(),incident.get_Location_Latitude(),incident.get_description(),incident.get_status(),incident.get_victimID(),incident.get_suspectID()),
            )
            self.conn.commit()
            print("Creating incident")
            return True  
    
        except Exception as error:
            print(error)
        # print("Creating incident")
          #return True
    

    def updateIncidentStatus(self, status, incident_id):
        try:
            self.cursor.execute(
                """
                Update Incidents
                Set status = ?
                where incidentID = ?
                """,
                (status, incident_id),
            )
            self.conn.commit()
            print(f"Updating status for incident {incident_id}")
            return True
        except incident_number_not_found_exception as error1:
            print(error1)
        except Exception as error2:
            print(error2)


    
       

    def getIncidentsInDateRange(self, start_date, end_date):
        
        try:
            self.cursor.execute("SELECT * FROM Incidents WHERE incidentDate >= ? AND incidentDate <= ?;",(start_date,end_date))
            Incidents = self.cursor.fetchall()  
            for Incident in Incidents:
                print(Incident)
        except Exception as e:
            print(e)

        print(f"Getting incidents from {start_date} to {end_date}")
        return Incidents

    def searchIncidents(self, incidentID):
       
        try:
            self.cursor.execute("Select * from Incidents where incidentId=?",(incidentID))
            Incidents = self.cursor.fetchall()  
            return Incidents
        except Exception as e:
            print(e)

        print(f"Searching incidents with criteria {incidentID}")
        return 

    def generateIncidentReport(self, report: Report):
      
        try:
            self.cursor.execute(
                "INSERT INTO Reports (reportID, incidentID, reportingOfficer, reportDate, reportDetails, status) VALUES (?, ?, ?,?,?,?)",
                (report.get_reportID(), report.get_incidentID(), report.get_reportingOfficer(),report.get_reportDate(),report.get_reportDetails(),report.get_status()),

            )
            self.conn.commit() 
            print("Generating incident report")
            return 
            # self.cursor.execute("Select * from Reports") 
            # Report = self.cursor.fetchall()
            # return Report  
            # print("Generating incident report")
            
        except Exception as e:
            print(e)
    

    def createCase(self, caseID, case_description, incidents):

        try:
            incident_ids = [incident[0][0] for incident in incidents]
            # print("*****",incident_ids)
            incident_ids_str = ','.join(map(str, incident_ids))
            self.cursor.execute(
                "INSERT INTO [Case] (caseID, caseDescription, incidentIDs) VALUES (?, ?, ?)",
                (caseID, case_description, incident_ids_str),
            )
            self.conn.commit()  #
            print(f"Case created with ID: {caseID} and associated incidents.")
            return caseID
        except Exception as e:
            print("Failed to create case:", e)
            return None

    def getCaseDetails(self, case_id):
        try:
            self.cursor.execute("Select * from [Case] where caseID=?",(case_id))
            Cases = self.cursor.fetchall() 
            return Cases
        except Exception as e:
            print(e)
        print(f"Getting details for case {case_id}")
        return Case()

    def updateCaseDetails(self, case):
        self.cursor.execute(
            """
            Update [Case]
            Set caseDescription = ?
            where caseID = ?
            """,
            (case.caseDescription, case.caseID),
        )
        self.conn.commit()
        print(f"Updating case details for case {case}")
        return True

    def getAllCases(self):
        try:
            self.cursor.execute("Select * from [Case] ")
            Cases = self.cursor.fetchall()  
            return Cases
        except Exception as e:
            print(e)
        print("Getting all cases")
        return []
