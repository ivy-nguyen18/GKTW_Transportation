import zones

def getWaitTime(queue, driver):
    totalWaitTime = 0
    for i, row in queue.iterrows():
        if i == 0 and driver == 1:
            totalWaitTime += row['travelTime'] 

        else:
            totalWaitTime += row['travelTime'] + row['timeFromPrev']  
    return totalWaitTime


def optimizeWaitTime(queue):
    times = []
    for i in range(len(queue)-1):
        times.append(zones.zoneLookUp(queue[-1][1].pickup, queue[i][1].pickup))
    minI = min(times)
    recentlyAdded = queue.pop()
    queue.insert(minI+1, recentlyAdded)
    return queue

