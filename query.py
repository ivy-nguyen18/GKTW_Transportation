from database import getQuery


# the table is called transportationTable2, as part of the database: GKTWTransportationDataRes.db
# you can query from here, or DBeaver (or anywhere you have SQLite)

getQuery('DROP TABLE IF EXISTS transportationTable2')
# getQuery('SELECT * FROM transportationTable2')