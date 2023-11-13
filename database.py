import sqlite3
import pandas as pd

conn = sqlite3.connect('GKTWTransportationDataRes.db')
c = conn.cursor()

# Database
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

def repopulateTable(day, is_ada):
    query = c.execute('''SELECT * FROM transportationTable2 t WHERE t.res_date = (?) AND t.ADA = (?)''', (day,is_ada))
    return pd.DataFrame(query.fetchall(), columns = ['name', 'res_date', 'res_time','pickup', 'dropoff', 'numOfPeople', 'ADA' ])

def addData(name, res_date, res_time, pickupLoc, dropoffLoc, ADA, numOfPeople):
    c.execute('INSERT INTO transportationTable2(name, res_date, res_time, pickupLoc, dropoffLoc, ADA, numOfPeople) VALUES (?,?,?,?,?,?,?)', (name, res_date, res_time, pickupLoc, dropoffLoc, ADA, numOfPeople))
    conn.commit()

def getQuery(string):
    c.execute(string)
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.commit()