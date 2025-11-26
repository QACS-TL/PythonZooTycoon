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

    while True:
        # Menu
        print()
        print("Animals App - Menu")
        print("1) List animals")
        print("2) Add animal")
        print("3) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            i = 0
            for a in animals:
                i+=1
                print(str(i) + ") Animal details: " + a)

            print(f"My count variable tells me there are {count} animals.")
            print(f"My animals collection tells me there are {len(animals)} animals.")

        elif choice == "2":
            print("Add a new animal")

            animal = input("Enter Animal Details (in form '{name},{type},{colour},{limb_count}': ").strip()
            while len(animal) < 12: # minimum length of details string
                print("Invalid details, please try again.")
                animal = input("Enter Animal Details (in form '{name},{type},{colour},{limb_count}': ").strip()

            animals.append(animal)
            count += 1


        elif choice == "3" or choice.lower() in ("exit", "quit"):
            print("Goodbye — saving and exiting.")
            # save_animals(animals)
            break
        else:
            print("Unknown option. Please try again.")

main_menu()
