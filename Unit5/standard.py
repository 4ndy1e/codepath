"""
Problem 1: New Horizons 

Step 1: Copy the following code into your IDE.

Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.
"""

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    # add method from problem 2 
    def greet_player(self, player_name): 
      return f"{self.name}: Hey there, {player_name},! How's it going, {self.catchphrase}!"

# Instantiate your villager here
apollo = Villager("Apollo", "Eagle", "pah")

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 

"""
Problem 2: 
Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:
Step 2: Step 2: Create a second instance of Villager in a variable named bones.
Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.
"""

bones = Villager("Bones", "Dog", "yip yip")

# print(bones.greet_player("Andy"))

"""
Problem 3: Update Catchphrase
In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.
Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".
"""

bones.catchphrase = "ruff it up"

print(bones.greet_player("Andy"))
