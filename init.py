# Object Oriented Programming

# Turns the world into objects

# Class - blueprint of an object

# Animal class
class Animal:
    def __init__(self, breed, coat_color, sound): # Constructor - which builds the object
        self.breed = breed
        self.coat_color = coat_color
        self.sound = sound
    
    def describe(self):
        return f"This animal is a {self.breed}, with a coat color of {self.coat_color} that says {self.sound}"
    
    def get_sound(self):
        return self.sound
    

animal = Animal("German Shephard", "Brown", "Bark")
print(animal.describe())
animal2 = Animal("Bird", "Blue", "tweet")
print(animal2.describe())
animal = Animal("Pikachu", "Yellow", "Pika pika")
print(animal.get_sound())