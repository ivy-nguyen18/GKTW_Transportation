import zones
def getWaitTime(queue, driver):
    totalWaitTime = 0
    for i, (timeFromPrev, guest) in enumerate(queue):
        if i == 0 and driver == 1:
            totalWaitTime += (guest.travelTime)
        else:
            totalWaitTime += (guest.travelTime + timeFromPrev)
    
    return totalWaitTime

def optimizeWaitTime(queue):
    times = []
    for i in range(len(queue)-1):
        times.append(zones.zoneLookUp(queue[-1][1].pickup, queue[i][1].pickup))
    minI = min(times)
    recentlyAdded = queue.pop()
    queue.insert(minI+1, recentlyAdded)
    return queue

