#Class inheritance

#i.e
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal): #Fish inheriting from Animal class
    def __init__(self):
        super().__init__() #get all the attributes and methods from Animal
        #initialize everything that the super class (Animal) can do into Fish class

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)