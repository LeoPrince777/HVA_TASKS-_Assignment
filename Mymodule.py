class Cab:
    
    numberofcabs  = 0

    def __init__(self,driver,kms,pay):
        self.driver = driver
        self.running = kms
        self.bill = pay
        Cab.numberofcabs  =  Cab.numberofcabs + 1
    def rateperkm(self):
        return self.bill/self.running
        
    def noofcabs(cls):
        return cls.numberofcabs


if __name__ == "__main__":
   
    firstcab  = Cab("Ramesh", 80, 1200)

    print(firstcab.driver)
    print(Cab.noofcabs())
