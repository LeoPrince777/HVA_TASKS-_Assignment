class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def details(self):
        print(f"vname: {self.name} ------ speed of max: {self.max_speed}")
#v= Vehicle("BUS",180,56)
#v. details()

class Bus(Vehicle):
    def b_details(self,bname, rate):
        print(f"bname: {bname} ------- Bus_rate: {rate}")
v= Bus("BUS",180,56)
v.details()
v.b_details("Volovo",2000000)