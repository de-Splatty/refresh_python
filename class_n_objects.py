class robot_dog:
    def __init__(self, name_val, breed_val):
       #init ,short for initialize, lets us initialize our objects properties
       #self is always the first parameter of any function in a class. It refers to the object or instance you're creating.
       self.name = name_val
       self.breed = breed_val
    def bark(self):
        print("Woof! Woof!")
       
#Main program
my_dog = robot_dog("Rex", "German Shepherd")
print("My dog's name is", my_dog.name)
print("My dog's breed is", my_dog.breed)
my_dog.bark()