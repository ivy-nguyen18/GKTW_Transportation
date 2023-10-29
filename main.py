
# read in matrix
# read in excel
import pandas as pd
import time

metaGuestQ = []

class Guest:
     def __init__(self, name, pickup, dropoff, dropoffFlag, reservation, ADA, travelTime, waitTime):
        self.name = name
        self.pickup = pickup
        self.dropoff = dropoff
        self.dropoffFlag = dropoffFlag
        self.reservation = reservation
        self.ADA = ADA
        self.travelTime = travelTime
        self.waitTime = waitTime
    
     def __repr__(self):
        return f'''Guest: {self.name}
                    \tpickup: {self.pickup}
                    \tdropoff: {self.dropoff}
                    \treseration: {self.reservation}
                    \tADA: {self.ADA}
                    \ttravel time = {self.travelTime}
                    \twait time = {self.waitTime})
                    -------------------------------------------------\n'''

     
def optimizeQueue(queue):
    return queue

def zoneLookUp(start, dest):
    marker = pd.read_excel('GKTW_Markers_2 (1).xlsx')
    distanceMatrix = pd.read_excel('Zone Distance_Time Matrix .xlsx')
    startZone = marker[marker['Name'].str.contains(start)].Zones.item()
    destZone = marker[marker['Name'].str.contains(dest)].Zones.item()
    time = distanceMatrix.loc[distanceMatrix['Zones'] == startZone, destZone].item()
    return time

def getWaitTime(queue, driver):
    totalWaitTime = 0
    for i, (timeFromPrev, guest) in enumerate(queue):
        if i == 0 and driver == 1:
            totalWaitTime += (guest.travelTime)
        else:
            totalWaitTime += (guest.travelTime + timeFromPrev)
    
    return totalWaitTime

def printQueue(queue):
    print('-'*50)
    for time, guest in queue:
        print(f"{guest}Time from Prev: {time}\n")

def getGuestInformation(guest):
    print('*'*100)
    print(guest)

def updateDropOffs(queue):
    for time, guest in queue:
        guest.dropoffFlag = int(input(f'Has {guest.name} been dropped off? '))
        if guest.dropoffFlag == 1:
            queue.remove([time, guest])
    return queue
        

def getInputs(queue):
    timeFromPrev = 0
    travelTime = 0
    waitTime = 0
    name = input('Guest: ')
    pickup = input("Input pick up location: ")
    dropoff = input("Input drop off destination: ")
    ADA = input("Is ADA? ")
    dropoffFlag = 0
    reservation = time.ctime()
    travelTime = zoneLookUp(pickup, dropoff)
    queue = updateDropOffs(queue)
    if len(queue) == 0:
        waitTime = zoneLookUp("Towne Hall", pickup)
        timeFromPrev = waitTime
    else:
        driver = int(input('Is the driver picking up (0) or dropping off (1) first person in queue? '))
        waitTime = getWaitTime(queue, driver)
        timeFromPrev = zoneLookUp(pickup, queue[-1][1].dropoff)
        waitTime += timeFromPrev
    return [timeFromPrev, Guest(name, pickup, dropoff, dropoffFlag, reservation, ADA, travelTime, waitTime)] 
     

if __name__ ==  '__main__':
    activeQueue = []
    i = 0

    while (i<2):
        guest = getInputs(activeQueue)
        activeQueue.append(guest)
        metaGuestQ.append(guest)
        print('Guest Information')
        getGuestInformation(guest[1])
        i+=1
     
    print('CURRENT ACTIVE QUEUE: ')
    printQueue(activeQueue)

    print('META QUEUE: ')
    printQueue(metaGuestQ)
