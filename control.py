import guest
import algorithm
import zones

metaGuestQ = []
activeQ = []
adaQ = []
queue = []

def getInputs(name, reservation, numOfPeople, pickup, dropoff, ADA):
    travelTime = 0
    waitTime = 0
    dropoffFlag = 'Picking Up'
    timeFromPrev = 0
    travelTime = zones.zoneLookUp(pickup, dropoff)
    return guest.Guest(name, pickup, dropoff, dropoffFlag, reservation, ADA, travelTime, waitTime, numOfPeople, timeFromPrev)
        

def getGuestInfo(guest, queue):
    
    if len(queue) == 0:
        guest.waitTime = zones.zoneLookUp("Towne Hall", guest.pickup)
        guest.timeFromPrev = guest.waitTime
    else:
        #driver = int(input('Is the driver picking up (0) or dropping off (1) first person in queue? '))
        driver = 0 if queue.iloc[0]['status'] == 'Picking up' else 1
        guest.waitTime = algorithm.getWaitTime(queue, driver)
        guest.timeFromPrev = zones.zoneLookUp(guest.pickup, queue.iloc[-1]['dropoff'])
        guest.waitTime += guest.timeFromPrev
    return guest

def controller(name, reservation, numOfPeople, pickup, dropoff, ADA, queue):
    guest = getInputs(name, reservation, numOfPeople, pickup, dropoff, ADA)
    return getGuestInfo(guest, queue)