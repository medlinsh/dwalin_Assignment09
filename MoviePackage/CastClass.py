CastNames = { "Shrek": 'Shrek: Mike Myers, Donkey: Eddie Murphy, Princess Fiona: Cameron Diaz, Lord Farquaad: John Lithgow',
        "Shrek2": 'Queen: Julie Andrews, Puss In Boots: Antonio Banderas, King: John Cleese, Prince Charming: Rupert Everett',
        "ShrekTheThird": 'Merlin: Eric Idle, Artie: Justin Timberlake, Evil Queen: Susanne Blakeslee, Pinocchio: Cody Cameron',
        "ShrekForeverAfter": 'Brogan: John Hamm, Patrol Witch: Lake Bell, Dancing Witch: Kathy Griffin, Guard Witch: Mary Kay Place',
        "PussInBoots": 'Puss in Boots: Antonio Banderas, Kitty Softpaws: Salma Hayek, Jack: Billy Bob Thornton, Jill: Amy Sedaris'
            }   

class Cast():
    
    def CastCheck(self,name):
        if CastNames["Shrek"] == 'Shrek: Mike Myers, Donkey: Eddie Murphy, Princess Fiona: Cameron Diaz, Lord Farquaad: John Lithgow':
            print("These names are in the repository.")
        else:
            print("That name is not in the repository. Only " + str(CastNames) + " are available.")
    
    def __init__(self, name):
       self.CastCheck(name)  
       self.name = name
    
    def __repr__(self):
        return "Actors = " + self.name
    
    def __str__(self):
       return "The following actors were featured in this film: " + CastNames["Shrek"] in CastNames.values()
        
