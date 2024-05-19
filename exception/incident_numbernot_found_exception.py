class incident_number_not_found_exception(Exception):
    def __init__(self):
        super().__init__("IncidentNumberNotFound")