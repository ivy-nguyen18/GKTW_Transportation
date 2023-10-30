def printQueue(queue):
    print('-'*50)
    for time, guest in queue:
        print(f"{guest}Time from Prev: {time}\n")

def getGuestInformation(guest):
    print('*'*100)
    print(guest)

def printAllQs(activeQ, adaQ, metaGuestQ):
    print('CURRENT ACTIVE QUEUE: ')
    printQueue(activeQ)

    print('CURRENT ACTIVE ADA QUEUE: ')
    printQueue(adaQ)

    print('META QUEUE: ')
    printQueue(metaGuestQ)