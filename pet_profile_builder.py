class Pet:
    print("The Pet class has been created!")

pet_object = Pet()

class PetProfile:
    category = "pet"

    def __init__(self, name, animal_type, age, favourite_food):

        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food


pet1 = PetProfile("Buddy", "Dog", 3, "Chicken")
pet2 = PetProfile("Luna", "Cat", 2, "Fish")


print("\nPet 1 Information")
print("Category:", pet1.category)
print("Name:", pet1.name)
print("Animal Type:", pet1.animal_type)
print("Age:", pet1.age)
print("Favourite Food:", pet1.favourite_food)

print("\nPet 2 Information")
print("Category:", pet2.category)
print("Name:", pet2.name)
print("Animal Type:", pet2.animal_type)
print("Age:", pet2.age)
print("Favourite Food:", pet2.favourite_food)