import sqlite3

conn = sqlite3.connect('GKTWTransportationData.db')
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
                                    numOfPeople TEXT
                                    )''')

def addData(name, pickupLoc, dropoffLoc, reservation, ADA, waitTime, numOfPeople):
    c.execute('INSERT INTO transportationTable(name, pickupLoc, dropoffLoc, reservation, ADA, waitTime, numOfPeople) VALUES (?,?,?,?,?,?,?)', [name, pickupLoc, dropoffLoc, reservation, ADA, waitTime, numOfPeople])
    conn.commit()

def getQuery(string):
    c.execute(string)
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.commit()