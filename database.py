import sqlite3

conn = sqlite3.connect('database/GKTWTransportationData.db', check_same_thread=False)
c = conn.cursor()

# Database
def createTable():
    c.execute('''CREATE TABLE IF NOT EXISTS 
              transportationTable(name TEXT, 
                                    pickupLoc TEXT,
                                    dropoffLoc TEXT,
                                    reservation TEXT,
                                    ADA TEXT,
                                    waitTime TEXT,
                                    numOfPeople TEXT,
                                    date TEXT
                                    )''')

def addData(name, pickupLoc, dropoffLoc, reservation, ADA, waitTime, numOfPeople, date):
    c.execute('INSERT INTO transportationTable(name, pickupLoc, dropoffLoc, reservation, ADA, waitTime, numOfPeople, date) VALUES (?,?,?,?,?,?,?,?)', [name, pickupLoc, dropoffLoc, reservation, ADA, waitTime, numOfPeople, date])
    conn.commit()

def getQuery(string):
    c.execute(string)
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.commit()