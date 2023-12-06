from database import getQuery

'''
the table is called transportationTable, as part of the database: GKTWTransportationData.db
you can query from here, or DBeaver (or anywhere you have SQLite)
'''

getQuery('DROP TABLE IF EXISTS transportationTable')
# getQuery('SELECT * FROM GKTWTransportationData.transportationTable')