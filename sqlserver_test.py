import pyodbc 
connection = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};Server=10.10.20.45;Database=BankPagesDb_Islami;User ID=sa;Password=lemon.2023;')

if(connection):
    print("connected!")
else:
    print("connection failed")

cursor = connection.cursor()	
cursor.execute("SELECT * FROM EMP") 
row = cursor.fetchone() 
while row:
    print (row) 
    row = cursor.fetchone()