'''
#Name: Seth Medlin, Addyson Stansel, Ryan Lupton, Tyra Crandell
#email: stansean@mail.uc.edu
#Assignment: Assignment 09
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can work together in a group to produce modular code
#Citations: 
#Anything else thats relevant: N/A
'''
#Dictionary containing cast names
CastNames = { "Shrek": "Shrek: Mike Myers, Donkey: Eddie Murphy, Princess Fiona: Cameron Diaz, Lord Farquaad: John Lithgow",
        "Shrek2": "Queen: Julie Andrews, Puss In Boots: Antonio Banderas, King: John Cleese, Prince Charming: Rupert Everett",
        "ShrekTheThird": "Merlin: Eric Idle, Artie: Justin Timberlake, Evil Queen: Susanne Blakeslee, Pinocchio: Cody Cameron",
        "ShrekForeverAfter": "Brogan: John Hamm, Patrol Witch: Lake Bell, Dancing Witch: Kathy Griffin, Guard Witch: Mary Kay Place",
        "PussInBoots": "Puss in Boots: Antonio Banderas, Kitty Softpaws: Salma Hayek, Jack: Billy Bob Thornton, Jill: Amy Sedaris"
            }

class Cast():

    def CastCheck(self, name):
        if name in CastNames:
           print("The following actors were featured in this film: " + CastNames[name])
           
        else:
            print("That name is not in the cast list. Only " + str(CastNames) + " are available.")
       
   
    def __init__(self, name):
       self.CastCheck(name)  
       self.name = name
   
    def __repr__(self):
        return "Actors = " + self.name
   
    def __str__(self):
       return "The following actors were featured in this film: " + CastNames["Shrek"] in CastNames.values()
