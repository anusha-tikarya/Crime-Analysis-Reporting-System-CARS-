import unittest

from dao.crime_analysis_service_impl import crime_analysis_service_impl

from entity.Incidents import Incidents

from exception.incident_numbernot_found_exception import incident_number_not_found_exception

class Testcrime_analysis_service_impl(unittest.TestCase):
    def setUp(self):
        self.service = crime_analysis_service_impl()
        self.test_incident = Incidents("Initial incidence", "2024-04-23", 23.65, 23.66, "Stolen", "Open", "23", "23")
        self.test_incidentID = self.service.create_incident(self.test_incident)

        self.assertIsNotNone(self.test_incidentID)

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