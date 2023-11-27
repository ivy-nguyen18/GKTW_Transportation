class Guest:
     '''
     Guest object: 
         name: name of guest reserving
         pickup: location of nearest building to pickup
         dropoff: location of nearest building to dropoff
         res_time: time indicated on reservation
         ADA: requirement of ADA shuttle
         numOfPeople: number of people within party
         res_date: date reservation is made
     '''
     def __init__(self, name, pickup, dropoff, reservation, ADA, numOfPeople,date):
        self.name = name
        self.pickup = pickup
        self.dropoff = dropoff
        self.res_time = reservation
        self.ADA = ADA
        self.numOfPeople = numOfPeople
        self.res_date = date
    
     def __repr__(self):
        return f'''Guest: {self.name}
                    \tpickup: {self.pickup}
                    \tdropoff: {self.dropoff}
                    \tdate: {self.res_date}
                    \treseration: {self.res_time}
                    \tADA: {self.ADA}
                    \tnum of people = {self.numOfPeople}
                    -------------------------------------------------\n'''
     
     def to_dict(self):
        return {
            'name': self.name,
            'res_date': self.res_date,
            'res_time': self.res_time,
            'pickup': self.pickup,
            'dropoff': self.dropoff,
            'numOfPeople': self.numOfPeople,
            'ADA': self.ADA
        }