from random import randint

class Animal:
    def Eat(self):
        print("Eating...")

    def Speak(self):
        pass

class Dog:
    def Eat(self):
        print("Chomping")
        
class Bird:
    def Eat(self):
        print("Pecking")
        
class Cow:
    pass
    # def Eat(self):
    #     print("Munching")
        

#-----------------------

def Ingest(obj:Animal):
    obj.Eat()

#-----------------------

# o1:Animal = Dog()
# o1.Eat()

o1:Animal
match randint(1, 3):
    case 1:
        o1 = Dog()
    case 2:
        o1 = Bird()
    case 3:
        o1 = Cow()

Ingest(o1)
