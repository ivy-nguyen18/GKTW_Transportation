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
        self.bump = 0
    
     def __repr__(self):
        return f'''Guest: {self.name}
                    \tpickup: {self.pickup}
                    \tdropoff: {self.dropoff}
                    \treseration: {self.reservation}
                    \tADA: {self.ADA}
                    \ttravel time = {self.travelTime}
                    \twait time = {self.waitTime})
                    -------------------------------------------------\n'''