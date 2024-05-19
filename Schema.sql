CREATE TABLE Victims(
	VictimID INT,
	FirstName VARCHAR(50),
	LastName VARCHAR(50),
	DateOfBirth DATE,
	Gender VARCHAR(20),
	ContactInformation VARCHAR(200),
	PRIMARY KEY(VictimID)
);



CREATE TABLE Suspects(
	SuspectID INT,
	FirstName VARCHAR(50),
	LastName VARCHAR(50),
	DateOfBirth DATE,
	Gender VARCHAR(20),
	ContactInformation VARCHAR(200)
	PRIMARY KEY(SuspectID)
);


CREATE TABLE Incidents(
	IncidentID INT,
	IncidentType VARCHAR(50),
	IncidentDate DATE,
	Location_Longitude DECIMAL(10, 8),
	Location_Latitude DECIMAL(10, 8),
	Description VARCHAR(200),
	Status VARCHAR(50),
	VictimID INT,
	SuspectID INT
	PRIMARY KEY (IncidentID),
	FOREIGN KEY (VictimID) References Victims(VictimID),
	FOREIGN KEY (SuspectID) References Suspects(SuspectID)
);



CREATE TABLE LawEnforcementAgency(
	AgencyID INT,
	AgencyName VARCHAR(50),
	Jurisdiction VARCHAR(50),
	ContactInformation VARCHAR(200),
	Officer VARCHAR(30),
	PRIMARY KEY(AgencyID)
);


CREATE TABLE Officers(
	OfficerID INT,
	FirstName VARCHAR(50),
	LastName VARCHAR(50),
	BadgeNumber INT,
	Rank VARCHAR(20),
	ContactInformation VARCHAR(200),
	AgencyID INT
	PRIMARY KEY (OfficerID),
	FOREIGN KEY (AgencyID) References LawEnforcementAgency(AgencyID) 
);



CREATE TABLE Evidence(
	EvidenceID INT,
	Description VARCHAR(200),
	LocationFound VARCHAR(50),
	IncidentID INT
	PRIMARY KEY (EvidenceID),
	FOREIGN KEY (IncidentID) References Incidents (IncidentID)
);



CREATE TABLE Reports(
	ReportID INT,
	IncidentID INT,
	ReportingOfficer INT,
	ReportDate DATE,
	ReportDetails VARCHAR(500),
	Status VARCHAR(20),
	PRIMARY KEY (ReportID),
	FOREIGN KEY (IncidentID) References Incidents (IncidentID),
	FOREIGN KEY (ReportingOfficer) References Officers (OfficerID)
);


select * from Incidents;
select * from Victims;
select * from Suspects;
select * from LawEnforcementAgency;
select * from Officers;
select * from Evidence;
select * from Reports;

SELECT *
            FROM Incidents
            WHERE incidentType='Robbery';

SELECT *
            FROM Incidents
            WHERE incidentID=1;

CREATE TABLE [Case] (
    caseID INT PRIMARY KEY,
    caseDescription NVARCHAR(MAX),
    incidentIDs NVARCHAR(MAX)
);