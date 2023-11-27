import guest
import datetime

'''
Get guest info and return as Guest object
'''
def getInputs(name, reservation, numOfPeople, pickup, dropoff, ADA, date):
    date = datetime.datetime.strptime(str(date), "%Y-%m-%d").strftime("%m/%d/%Y")
    return guest.Guest(name, pickup, dropoff, reservation, ADA, numOfPeople, date)