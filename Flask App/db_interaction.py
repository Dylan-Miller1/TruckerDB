import pyodbc

def query(db_query):
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-Q24L404;DATABASE=Truckerdb;Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute(db_query)
    data = cursor.fetchall()
    connection.close()
    return data

def query_vals(db_query, vals):
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-Q24L404;DATABASE=Truckerdb;Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute(db_query, vals)
    cursor.commit()
    connection.close()