import guest
import algorithm
import zones

'''
Controller to create Guest and get their wait time
'''

# Creating guest object
def getInputs(name, reservation, numOfPeople, pickup, dropoff, ADA):
    travelTime = 0
    waitTime = 0
    dropoffFlag = 'Picking Up'
    timeFromPrev = 0
    travelTime = zones.zoneLookUp(pickup, dropoff)
    return guest.Guest(name, pickup, dropoff, dropoffFlag, reservation, ADA, travelTime, waitTime, numOfPeople, timeFromPrev)
        
# Get guest wait time
def getGuestInfo(guest, queue):
    # if the queue is empty, initial shuttle location is the rest spot (Zone Z)
    if len(queue) == 0:
        guest.waitTime = zones.zoneLookUp("Towne Hall", guest.pickup)
        guest.timeFromPrev = guest.waitTime 
    
    # if queue is not empty, get driver's status in the queue, call upon algorithm to get wait time
    else:
        driver = 0 if queue.iloc[0]['status'] == 'Picking up' else 1
        guest.waitTime = algorithm.getWaitTime(queue, driver)
        guest.timeFromPrev = zones.zoneLookUp(guest.pickup, queue.iloc[-1]['dropoff'])
        guest.waitTime += guest.timeFromPrev
        guest.waitTime += guest.waitTime + 5 # add 5 minute leeway for boarding and dropoff
    return guest

def controller(name, reservation, numOfPeople, pickup, dropoff, ADA, queue):
    guest = getInputs(name, reservation, numOfPeople, pickup, dropoff, ADA)
    return getGuestInfo(guest, queue)