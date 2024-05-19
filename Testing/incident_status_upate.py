import unittest

from dao.crime_analysis_service_impl import crime_analysis_service_impl
from entity.Incidents import Incident

from exception.incident_numbernot_found_exception import incident_number_not_found_exception

class IncidentStatusUpdate(unittest.TestCase):
    def setUp(self):
        self.service = crime_analysis_service_impl()
        self.test_incidents = Incident("Robbery", '2024-08-23', 63.32, 56.32, "Stolen", "Closed", 2, 2)
        self.test_incident_id = self.service.create_incident(self.service)
        self.assertIsNotNone(self.test_incident_id)

    def test_update_incident_status(self):
        updated_status = "Open"
        incidentId = 2
        self.service.update_incident_status(incidentId, updated_status)

        self.service.cursor.execute(
            "SELECT * from Incidents where IncidentId = ?", (self.test_incident_id,)
        )

        incident = self.service.cursor.fetchone()

        self.assertEqual(incident[1], incidentId)
        self.assertEqual(incident[2], updated_status)