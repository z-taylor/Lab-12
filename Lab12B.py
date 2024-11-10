# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab12B.py
class dog():
    def __init__(self, age, weight, name, furColor, breed):
        self.age = age
        self.weight = weight
        self.name = name
        self.furColor = furColor
        self.breed = breed
    def bark(self):
        print("Woof! Woof!")
    def rename(self):
        self.name = input(f'{self.name} isn"t a very good name. What should they be renamed to: ')
    def eat(self):
        self.weight += float(input(f"{self.name} is hungry, how much should he eat: "))

print("You are about to create a dog.")
age = int(input("How old is the dog: "))
print("")
weight = float(input("How much does the dog weigh: "))
print("")
name = input('What is the dog"s name: ')
print("")
color = input("What color is the dog: ")
print("")
breed = input("What breed is the dog: ")
print("")
dog1 = dog(age, weight, name, color, breed)
print(f"{dog1.name} is a {dog1.age} year old {dog1.furColor} {dog1.breed} that weighs {dog1.weight} lbs.")
dog1.bark()
dog1.eat()
print("")
dog1.rename()
print("")
print(f"{dog1.name} is a {dog1.age} year old {dog1.furColor} {dog1.breed} that weighs {dog1.weight} lbs.")