def updateDropOffs(queue):
    for time, guest in queue:
        guest.dropoffFlag = int(input(f'Has {guest.name} been dropped off? '))
        if guest.dropoffFlag == 1:
            queue.remove([time, guest])
    return queue