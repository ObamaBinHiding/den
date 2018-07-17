#!/usr/bin/python3
#Classes for side project with Gabe
#Authors:
#   Ariel Lima <ariel.lima@gordon.edu>
#   ...

#imports needed
from random import randint

#classes
class Animal:
    """
        This is the main animal class of the mini-game, all other animal classes come from this one
    """
    def __init__(self):
        #agility attributes
        self.speed = 0
        #damage attributes
        self.attack = 0
        #health attributes
        self.health = 0
        self.defense = 0
        self.defenseFactor = 0
    
    def animalSound(self):
        return ''

    def attackDamage(self):
        #Simple method that returns the total damage this animal will do
        return(self.speed*self.attack)#'*' is times, 3*4=12
    
    def defensePadding(self, damageIn):
        #Simple method that will be run uppon receiving damage, helps negate some of the damage comming in
        return(damageIn-(self.defense+(randint(1, self.defenseFactor))))#Gabe, randint(x, y) gives us a random number in between those two points
    
    def takeDamage(self, damage):
        #Simple method that removes health
        self.health -= damage

"""
TODO - Gabe: 

Create these classes in this file:

class Reptile(Animal): <- the Animal inside the parenthesis means we are inheriting from the Animal class, if you read you know what it means. If you didn't, go read it.
    {...}
class Mammal(Animal):
    {...}
class Bird(Animal):
    {...}

START THESE BY TONIGHT, use the default one I made to help you.
                        add your name to the authors(replace the '...') when you work on it.
"""
