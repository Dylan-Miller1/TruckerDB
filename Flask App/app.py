from flask import Flask, url_for, render_template, request
import pyodbc
from db_interaction import query, query_vals

app = Flask(__name__)

@app.route("/")
def home():
    #Building the query for the driver table
    data = query("""
        select 
            DriverID, 
            FirstName, 
            LastName, 
            DateOfBirth, 
            DriversLicenseNum, 
            Email,  
            DistrictName,
            TruckClass
        from 
            DriverPersonal
        inner join 
            Districts
        on 
            DriverPersonal.DistrictID = Districts.DistrictID
        inner join 
            TruckType
        on 
            DriverPersonal.TruckTypeID = TruckType.TruckTypeID
    """)
    return render_template("DriverPersonal.html", data=data)

@app.route("/trucks")
def trucks():
    #Building the query for the truck table
    data = query("""
        select 
            Trucks.TruckID, 
            TruckClass, 
            Model, 
            TruckYear, 
            WeightRating,
            FirstName, 
            LastName
        from 
            Trucks
        inner join 
            DriverPersonal
        on 
            DriverPersonal.TruckID = Trucks.TruckID
        inner join 
            TruckType
        on 
            Trucks.TruckTypeID = TruckType.TruckTypeID
    """)
    return render_template("Trucks.html", data=data)

@app.route("/trucktype")
def trucktype():
    data = query("SELECT * FROM TruckType")
    return render_template("TruckType.html", data=data)

@app.route("/districts")
def districts():
    data = query("SELECT * FROM Districts")
    return render_template("Districts.html", data=data)

@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        #Pulling data from the HTML and storing it in variables
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        dob = request.form["dob"]
        license_number = request.form["license_number"]
        email = request.form["email"]
        district = request.form["district"]
        truck_model = request.form["truck_model"]
        truck_year = request.form["truck_year"]
        weight_rating = request.form["weight_rating"]
        truck_class = request.form["truck_class"]

        #Getting the next ID available in our table
        next_id = query("""
            SELECT MAX(DriverID)
            FROM DriverPersonal;
        """)
        next_id = (next_id[0][0])
        next_id += 1
        
        #Building  and executing our submit query for Our DriverPersonal Table
        submit_query = """
            INSERT INTO DriverPersonal (
                DriverID, 
                FirstName, 
                LastName, 
                DateOfBirth, 
                DriversLicenseNum, 
                Email, 
                DistrictID, 
                TruckID, 
                TruckTypeID
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        vals = (next_id, first_name, last_name, dob, license_number, email, district, next_id, truck_class)
        query_vals(submit_query, vals)

        #Building  and executing our submit query for Our Trucks Table
        submit_query = """
            INSERT INTO Trucks (
                TruckID, 
                TruckTypeID, 
                Model, 
                TruckYear, 
                WeightRating 
            )
            VALUES (?, ?, ?, ?, ?);
        """
        vals = (next_id, truck_class, truck_model, truck_year, weight_rating)
        query_vals(submit_query, vals)
       
        return render_template(
            "submitreview.html",
            first_name = first_name,
            last_name = last_name,
            dob = dob,
            license_number = license_number,
            email = email,
            district = district,
            truck_model = truck_model,
            truck_year = truck_year,
            weight_rating = weight_rating,
            truck_class = truck_class
        )
    else:
        return render_template("submit.html")

if __name__ == "__main__":
    app.run()