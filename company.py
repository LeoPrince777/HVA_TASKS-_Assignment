# Creates class Company
class Company:
    # attributes
    name = "XYZ Bank"
    turnover = 5000
    revenue = 1000
    no_of_employees = 100
    
    # method
    def productivity(self):
        return Company.revenue/Company.no_of_employees
   ### Attributes which are defined outside of method can be extracted without creating object.
print(Company.name)
print(Company.turnover)
print(Company.no_of_employees)
print(Company().productivity())

print("*********************************************************")

class person:
        def __init__(self,firstname,lastname):
            self.first = firstname
            self.last = lastname

myname = person("Deepanshu","Bhalla")
print(myname.first,myname.last)


print("*********************************************************")
class MyCompany:
    # methods
    def __init__(self, compname, revenue, employeesize):
        self.name = compname
        self.revenue = revenue
        self.no_of_employees = employeesize

    def productivity(self):
        return self.revenue/self.no_of_employees

Bank = MyCompany('ABC Bank', 5000,200)
print(MyCompany.productivity(Bank))  # Model -1 
print(Bank.productivity())           # Model -2



#c = Company()
#c.productivity()