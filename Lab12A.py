# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab12A.py
class chair():
    def __init__(self, legs = 4, rolling = False, material = "Plastic"):
        self.numOfLegs = legs
        self.rolling = rolling
        self.material = material

print("You are about to create a chair.")
legs = int(input("How many legs does your chair have: "))
rolling = True if input("Is your chair rolling (true/false): ").lower() in ("true", "t") else False
print("")
material = input("What is your chair made of: ")
chair1 = chair(legs, rolling, material)
print("")
print(f"Your chair has {chair1.numOfLegs} legs, {'is' if chair1.rolling==True else 'is not'} rolling, and is made of {chair1.material}")
print("This program is going to change that.")
chair1.numOfLegs, chair1.rolling, chair1.material = 4, False, "wood"
print(f"Your chair has {chair1.numOfLegs} legs, {'is' if chair1.rolling==True else 'is not'} rolling, and is made of {chair1.material}")