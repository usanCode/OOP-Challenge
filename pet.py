
class Pet:
    def __init__(self, name: str, hunger: int, energy:int, happiness: int):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness

    def eat(self,hunger,happiness):
        # reduces hunger by 3 points (but not below 0), and increases happiness by 1.
        
        if self.hunger > 0:
            self.hunger -=3
        else:
            self.hunger = 0
        self.happiness +=1

    def sleep(self, energy):  

        # increases energy by 5 points (but not above 10).
        if self.energy <10:
            self.energy +=5
        else:
            self.energy = 0
        

    def play(self,energy,hunger,happiness):

        #decreases energy by 2, increases happiness by 2, and increases hunger by 1.
       
        if self.energy >=2: 
            self.energy -=2
        else:
            self.energy = 0
        self.happiness +=2  
        self.hunger +=1

        #prints the current state of the pet.


    def get_status(self):
        # returns a string with the pet's name, hunger, energy, and happiness levels.
        
        return f"Name: {self.name}, Hunger:{self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}  "
    
    

    
    

