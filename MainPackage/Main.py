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


movieCast = Cast("Shrek")

'''
movieBox = boxPerformance("50")
movieBox.movieCheck("Shrek")
'''


movieRating = Rating("Shrek", 42)
print(movieRating.__str__())
movieRating.setRating(-5)