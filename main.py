import sys

def main_menu():
    animals = []
    # csv animal values in string
    # name, colour, limb_count, type
    count = 0
    animals.append("Fido,BLACK,4,Dog")
    count += 1
    animals.append("Fifi,WHITE,5,Cat")
    count += 1
    animals.append("Oscar,ORANGE,3,Bird")
    count += 1
    animals.append("Boris,PURPLE,3,Animal")
    count += 1

    print(animals)

    print(f"My count variable tells me there are {count} animals.")
    print(f"My animals collection tells me there are {len(animals)} animals.")

    print("Add a new animal")

    animal = input("Enter Animal Details (in form '{name},{type},{colour},{limb_count}': ").strip()

    animals.append(animal)
    count += 1

    print(animals)
    print(f"My count variable tells me there are {count} animals.")
    print(f"My animals collection tells me there are {len(animals)} animals.")

main_menu()
