'''
#Name: Seth Medlin, Addyson Stansel, Ryan Lupton, Tyra Crandell
#email: crandete@mail.uc.edu
#Assignment: Assignment 09
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can work together in a group to produce modular code
#Citations: 
#Anything else thats relevant: N/A
'''

from MoviePackage.CastClass import *
from MoviePackage.PerformanceClass import *
from MoviePackage.RatingClass import *


movieCast = Cast("Shrek") #Instantiate Cast

movieBox = boxPerformance("Shrek")  #Instantiate boxPerformance
print(movieBox.__str__())

movieRating = Rating("Shrek", 88)   #Instantiate Rating
print(movieRating.__str__())
movieRating.setRating(-5)