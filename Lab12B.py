# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab12A.py

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
        self.name = input(f"{self.name} isn’t a very good name. What should they be renamed to: ")
    def eat(self):
        self.weight += float(input(f"{self.name} is hungry, how much should he eat: "))

age = input("You are about to create a dog.\nHow old is the dog: ")
weight = float(input("How much does the dog weigh: "))
name = input("What is the dog’s name: ")
color = input("What color is the dog: ")
breed = input("What breed is the dog: ")
dog1 = dog(age, weight, name, color, breed)
print(f"{dog1.name} is a {dog1.age} year old {dog1.furColor} {dog1.breed} that weighs {dog1.weight} lbs.")
dog1.bark()
dog1.eat()
dog1.rename()
print(f"{dog1.name} is a {dog1.age} year old {dog1.furColor} {dog1.breed} that weighs {dog1.weight} lbs.")