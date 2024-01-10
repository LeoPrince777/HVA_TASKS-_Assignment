class Animal:
    name=''
    def eat(self, name):
        print( f"{name} can eat!")
        print( f"{self.name} can eat! checking checking") ### when we used self. name then result ==> can eat!
        print( name+ " can eat!")
    def sleep(self):
        print("I can sleep!")
    def speak(self):
        print("hooo hello")
# derived class
class Dog(Animal):
    def bark(self):
        print("I can bark! Woof woof!!")
# Create object of the Dog class
dog1 = Dog()
# Calling members of the base class
dog1.eat("Ram")
dog1.sleep()
# Calling member of the derived class
dog1.bark()
dog1.speak()  ### with out using self on speak(), We got the TypeError: speak() takes 0 positional arguments but 1 was given