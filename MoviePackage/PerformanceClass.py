'''
#Name: Seth Medlin, Addyson Stansel, Ryan Lupton, Tyra __
#email: medlinsh@mail.uc.edu
#Assignment: Assignment 09
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can work together in a group to produce modular code
#Citations: 
#Anything else thats relevant: N/A
'''


#Dictionary containing box office profits (in Millions)
boxOfficeProfits = {'Shrek': "$488 Million",
                    'Shrek2': "$929 Million",
                    'ShrekTheThird': "$814 Million",
                    'ShrekForeverAfter': "$753 Million",
                    'PussinBoots': "$555 Million"
                    }
#Variable defining if the box office performance has been checked
movieInfo = 0

class boxPerformance():
    
    def movieCheck(self,film):
        #check that the film in in the dictionary
        if film in boxOfficeProfits:
                self.film = film
                movieInfo = 1
        else:
                print("That film is not in the repository.")
                
                
        if movieInfo == 1:    
            print("Movie information has been checked. Tickets can now be purchased.")
        else:
            print("Could not very movie information. Tickets cannot be purchased.")


    # Defining film repository
    def __init__(self,film):
        self.movieCheck(film) #checking if the movie information is in the repository
        self.film = film #store the film name in the current object
        
        
        
    def __repr__(self):
        # Returns a string representation of the project
        return "Film = " + self.film
    
    
    def __str__(self):
        return "The film's box office profits were: " + boxOfficeProfits['Shrek']



##Test Code
#print(boxPerformance('Shrek').__str__())

