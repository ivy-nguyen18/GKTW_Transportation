class Guest:
     def __init__(self, name, pickup, dropoff, driverStatus, reservation, ADA, travelTime, waitTime, numOfPeople, timeFromPrev):
        self.name = name
        self.pickup = pickup
        self.dropoff = dropoff
        self.driverStatus = driverStatus
        self.reservation = reservation
        self.ADA = ADA
        self.travelTime = travelTime
        self.waitTime = waitTime
        self.numOfPeople = numOfPeople
        self.timeFromPrev = timeFromPrev
    
     def __repr__(self):
        return f'''Guest: {self.name}
                    \tpickup: {self.pickup}
                    \tdropoff: {self.dropoff}
                    \treseration: {self.reservation}
                    \tADA: {self.ADA}
                    \ttravel time = {self.travelTime}
                    \twait time = {self.waitTime})
                    \tnum of people = {self.numOfPeople}
                    -------------------------------------------------\n'''
     
     def to_dict(self):
        return {
            'name': self.name,
            'waitTime': self.waitTime,
            'reservation': self.reservation,
            'pickup': self.pickup,
            'dropoff': self.dropoff,
            'numOfPeople': self.numOfPeople,
            'status': self.driverStatus,
            'travelTime': self.travelTime,
            'timeFromPrev': self.timeFromPrev
        }