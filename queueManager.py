def updateDropOffs(queue):
    newList = queue.copy()
    for time, guest in newList:
        guest.dropoffFlag = int(input(f'Has {guest.name} been dropped off? '))
        if guest.dropoffFlag == 1:
            queue.remove([time, guest])
    return queue