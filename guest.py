class Guest:
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