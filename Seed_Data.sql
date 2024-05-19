-- Insert data into Victims Table
INSERT INTO Victims (VictimID, FirstName, LastName, DateOfBirth, Gender, ContactInformation) VALUES
(1, 'Arjun', 'Patel', '1985-04-23', 'Male', '1234 Elm St, Mumbai, +91-9876543210'),
(2, 'Priya', 'Sharma', '1990-08-17', 'Female', '5678 Maple Ave, Delhi, +91-8765432109'),
(3, 'Vijay', 'Singh', '1978-02-11', 'Male', '9101 Oak Blvd, Bangalore, +91-7654321098'),
(4, 'Anjali', 'Nair', '1982-12-30', 'Female', '2345 Pine St, Chennai, +91-6543210987'),
(5, 'Ravi', 'Kumar', '1995-06-21', 'Male', '6789 Birch Rd, Kolkata, +91-5432109876');

-- Insert data into Suspects Table
INSERT INTO Suspects (SuspectID, FirstName, LastName, DateOfBirth, Gender, ContactInformation) VALUES
(1, 'Rahul', 'Mehta', '1983-05-19', 'Male', '4321 Cedar Ave, Pune, +91-4321098765'),
(2, 'Sunita', 'Joshi', '1992-03-14', 'Female', '8765 Walnut St, Ahmedabad, +91-3210987654'),
(3, 'Amit', 'Gupta', '1976-11-29', 'Male', '1098 Fir Ln, Hyderabad, +91-2109876543'),
(4, 'Neha', 'Kapoor', '1988-07-07', 'Female', '5432 Spruce Dr, Jaipur, +91-1098765432'),
(5, 'Suresh', 'Verma', '1993-09-25', 'Male', '7890 Ash Ct, Lucknow, +91-0987654321');

-- Insert data into LawEnforcementAgency Table
INSERT INTO LawEnforcementAgency (AgencyID, AgencyName, Jurisdiction, ContactInformation, Officer) VALUES
(1, 'Mumbai Police', 'Mumbai', 'Mumbai, +91-9876543210', 'Inspector'),
(2, 'Delhi Police', 'Delhi', 'Delhi, +91-8765432109', 'Inspector'),
(3, 'Bangalore Police', 'Bangalore', 'Bangalore, +91-7654321098', 'Inspector');

-- Insert data into Officers Table
INSERT INTO Officers (OfficerID, FirstName, LastName, BadgeNumber, Rank, ContactInformation, AgencyID) VALUES
(1, 'Raj', 'Singh', 101, 'Inspector', 'Mumbai, +91-9876543210', 1),
(2, 'Amit', 'Kumar', 102, 'Inspector', 'Delhi, +91-8765432109', 2),
(3, 'Suresh', 'Reddy', 103, 'Inspector', 'Bangalore, +91-7654321098', 3);

-- Insert data into Incidents Table
INSERT INTO Incidents (IncidentID, IncidentType, IncidentDate, Location_Longitude, Location_Latitude, Description, Status, VictimID, SuspectID) VALUES
(1, 'Robbery', '2024-05-01', 72.8777, 19.0760, 'Armed robbery at a bank.', 'Open', 1, 1),
(2, 'Burglary', '2024-05-02', 77.1025, 28.7041, 'Burglary at a residential house.', 'Closed', 2, 2),
(3, 'Assault', '2024-05-03', 77.5946, 12.9716, 'Physical assault in a parking lot.', 'Investigating', 3, 3);

-- Insert data into Evidence Table
INSERT INTO Evidence (EvidenceID, Description, LocationFound, IncidentID) VALUES
(1, 'Knife', 'Bank', 1),
(2, 'Gloves', 'House', 2),
(3, 'CCTV Footage', 'Parking Lot', 3);

-- Insert data into Reports Table
INSERT INTO Reports (ReportID, IncidentID, ReportingOfficer, ReportDate, ReportDetails, Status) VALUES
(1, 1, 1, '2024-05-02', 'Initial report on the bank robbery.', 'Submitted'),
(2, 2, 2, '2024-05-03', 'Initial report on the house burglary.', 'Reviewed'),
(3, 3, 3, '2024-05-04', 'Initial report on the parking lot assault.', 'Submitted');

-- Insert data into Case Table
INSERT INTO [Case] (caseID, caseDescription, incidentIDs) VALUES
(1, 'Case involving multiple incidents related to theft.', '1,2'),
(2, 'Case involving violent crimes.', '3');
