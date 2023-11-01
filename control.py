import time
import guest
import write
import algorithm
import zones
import queueManager

metaGuestQ = []
activeQ = []
adaQ = []
queue = []

def getInputs():
    travelTime = 0
    waitTime = 0
    name = input('Guest: ')
    pickup = input("Input pick up location: ")
    dropoff = input("Input drop off destination: ")
    ADA = int(input("Is ADA (1 = True/ 0 = False)? "))
    dropoffFlag = 0
    reservation = time.ctime()
    travelTime = zones.zoneLookUp(pickup, dropoff)
    return guest.Guest(name, pickup, dropoff, dropoffFlag, reservation, ADA, travelTime, waitTime)
        

def getGuestInfo(guest, queue):
    timeFromPrev = 0
    queue = queueManager.updateDropOffs(queue)
    if len(queue) == 0:
        guest.waitTime = zones.zoneLookUp("Towne Hall", guest.pickup)
        timeFromPrev = guest.waitTime
    else:
        driver = int(input('Is the driver picking up (0) or dropping off (1) first person in queue? '))
        guest.waitTime = algorithm.getWaitTime(queue, driver)
        timeFromPrev = zones.zoneLookUp(guest.pickup, queue[-1][1].dropoff)
        guest.waitTime += timeFromPrev
    return [timeFromPrev, guest]

def controller(): 
    i = 0
    queue = []
    while (i<4):
        guest = getInputs()
        if guest.ADA == 1:
            queue = adaQ
        else:
            queue = activeQ
        travelInfo = getGuestInfo(guest, queue)
        queue.append(travelInfo)
        metaGuestQ.append(travelInfo)
        print('Guest Information')
        write.getGuestInformation(travelInfo[1])
        i+=1
        
    write.printAllQs(activeQ, adaQ, metaGuestQ)
