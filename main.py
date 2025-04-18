

from pet import Pet


my_pet1 = Pet(name="Max", hunger=5, energy=8, happiness=7)
my_pet2 = Pet(name="Indus", hunger=3, energy=6 , happiness=5)
my_pet3 = Pet(name="Meou", hunger=4, energy=7, happiness=6)
my_pet4 = Pet(name="Chui", hunger=2, energy=5, happiness=4)
my_pet5 = Pet(name="Minette", hunger=1, energy=4, happiness=3)

my_pet1.eat(hunger=5, happiness=7)  
my_pet1.play(energy=8, hunger=5, happiness=7)  
my_pet1.sleep(energy=8)  

print(f"{my_pet1.name} is eating...")
print(f"{my_pet2.name} is running towards the people walking behind the compound.")
print(f"I  miss so much {my_pet3.name}")

# Displaying the status of each pet.

print(my_pet1.get_status())
print(my_pet2.get_status())
print(my_pet3.get_status())
print(my_pet4.get_status())
print(my_pet5.get_status())