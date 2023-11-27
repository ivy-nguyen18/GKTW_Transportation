import sqlite3
import pandas as pd

'''
Usage of sqlite database. 
Database to connect to: GKTWTransportationDataRes.db
Full path to database: GKTW_Transportation/database/GKTWTransportationDataRes.db
Table: transportationTable2
'''
conn = sqlite3.connect('database/GKTWTransportationDataRes.db')
c = conn.cursor()

# creating table if not existed on database
def createTable():
    c.execute('''CREATE TABLE IF NOT EXISTS 
              transportationTable2(name TEXT, 
                                    res_date TEXT,
                                    res_time TEXT,
                                    pickupLoc TEXT,
                                    dropoffLoc TEXT,
                                    ADA TEXT,
                                    numOfPeople TEXT
                                    )''')

#Depending on the reservation date, repopulate the dashboard with reservation time of current day
def repopulateTable(day, is_ada):
    query = c.execute('''SELECT * FROM transportationTable2 t WHERE t.res_date = (?) AND t.ADA = (?)''', (day,is_ada))
    return pd.DataFrame(query.fetchall(), columns = ['name', 'res_date', 'res_time','pickup', 'dropoff', 'numOfPeople', 'ADA' ])

#Add data to table
def addData(name, res_date, res_time, pickupLoc, dropoffLoc, ADA, numOfPeople):
    c.execute('INSERT INTO transportationTable2(name, res_date, res_time, pickupLoc, dropoffLoc, ADA, numOfPeople) VALUES (?,?,?,?,?,?,?)', (name, res_date, res_time, pickupLoc, dropoffLoc, ADA, numOfPeople))
    conn.commit()

#All other queries, ran through python code
def getQuery(string):
    c.execute(string)
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.commit()