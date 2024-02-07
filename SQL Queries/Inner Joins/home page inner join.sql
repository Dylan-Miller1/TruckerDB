select DriverID, FirstName, LastName, DateOfBirth, DriversLicenseNum, Email, DistrictName, TruckClass
from DriverPersonal
inner join Districts
on DriverPersonal.DistrictID = Districts.DistrictID
inner join TruckType
on DriverPersonal.TruckTypeID = TruckType.TruckTypeID