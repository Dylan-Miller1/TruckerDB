CREATE TABLE DriverPersonal (
	DriverID INT PRIMARY KEY,
	FirstName VARCHAR(50),
	LastName VARCHAR(50),
	DateOfBirth DATE,
	DriversLicenseNum VARCHAR(20),
	Email VARCHAR(100),
	DistrictID INT,
	TruckID INT,
	TruckTypeID INT
	);