
# read in matrix
# read in excel
import pandas as pd

def zoneLookUp(start, dest):
    marker = pd.read_excel('GKTW_Markers_2 (1).xlsx')
    distanceMatrix = pd.read_excel('Zone Distance_Time Matrix .xlsx')
    startZone = marker[marker['Name'].str.contains(start)].Zones.item()
    destZone = marker[marker['Name'].str.contains(dest)].Zones.item()
    time = distanceMatrix.loc[distanceMatrix['Start'] == startZone, destZone].item()
    return time

queue = []
timeInQueue = 0


while (True):
    # input start, destination....
    name = input('Guest: ')
    start = input("Input pick up location: ")
    dest = input("Input drop off destination: ")
    dropoff = 0 #0 = Not dropped off, 1 = Dropped off, 2 = no show
    time = "current_time/input time"

    travel_time = zoneLookUp(start, dest)

    # add to queue as tuple (start, destination) -> tuple array
    queue.append((start, dest, dropoff, travel_time))
    print(queue)
    break
    # to estimate the following time, only look at drop offs = 0

    # do a look up on the destination of previous and the current pick up loc, applicabable for nonfirst

