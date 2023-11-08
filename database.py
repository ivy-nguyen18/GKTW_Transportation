import sqlite3

conn = sqlite3.connect('transportationData.db')
c = conn.cursor()

# Database
def createTable():
    c.execute('''CREATE TABLE IF NOT EXISTS 
              transportationTable(name TEXT, 
                                    pickupLoc TEXT,
                                    dropoffLoc TEXT,
                                    reservation DATETIME,
                                    ADA INT,
                                    waitTime TEXT,
                                    numOfPeople INT
                                    )''')

def addData(name, pickupLoc, dropoffLoc, reservation, ADA, waitTime, numOfPeople):
    c.execute('INSERT INTO transportationTable(name, pickupLoc, dropoffLoc, reservation, ADA, waitTime, numOfPeople) VALUES (?,?,?,?,?,?,?)', (name, pickupLoc, dropoffLoc, reservation, ADA, waitTime, numOfPeople))
    conn.commit()
    conn.close()

def getData():
    c.execute('SELECT * FROM transportationTable')
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()