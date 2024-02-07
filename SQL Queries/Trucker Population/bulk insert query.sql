BULK INSERT TruckType
FROM 'C:\Users\Work\Desktop\TruckerDB\SQL Queries\Trucker Population\truck_types.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
	FIRSTROW = 2
);
