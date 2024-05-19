import unittest

from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl

from entity.Incidents import Incidents

from exception.IncidentNumberNotFoundException import IncidentNumberNotFoundException

class TestCrimeAnalysisServiceImpl(unittest.TestCase):
    def setUp(self):
        self.service = CrimeAnalysisServiceImpl()
        self.test_incident = Incidents("Initial incidence", "2024-04-23", 23.65, 23.66, "Stolen", "Open", "23", "23")
        self.test_incidentID = self.service.create_incident(self.test_incident)

        self.assertIsNotNone(self.test_incident_id)

    def test_create_incident(self):
        incidentType = "Robbery"
        incidentDate = '2024-08-23'
        locationLongitude = 24.6
        locationLatitude = 52.36
        description = "Stolen"
        status = "Open"
        victimID = 2
        suspectID = 2

if __name__ == "__main__":
    unittest.main()