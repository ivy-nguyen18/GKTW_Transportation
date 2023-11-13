import guest
import datetime


def getInputs(name, reservation, numOfPeople, pickup, dropoff, ADA, date):
    date = datetime.datetime.strptime(str(date), "%Y-%m-%d").strftime("%m/%d/%Y")
    return guest.Guest(name, pickup, dropoff, reservation, ADA, numOfPeople, date)