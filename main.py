import sys

def main_menu():
    animals = []
    # csv animal values in string
    # name, colour, limb_count, type
    animals.append("Fido,BLACK,4,Dog")
    animals.append( "Fifi,WHITE,5,Cat")
    animals.append("Oscar,ORANGE,3,Bird")
    animals.append("Boris,PURPLE,3,Animal")

    while True:
        # Menu
        print()
        print("Animals App - Menu")
        print("1) List animals")
        print("2) Add animal")
        print("3) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            for a in animals:
                name, colour, limb_count, type = a.split(",")
                print(f"Name: {name}, Colour: {colour}, LimbCount: {limb_count}, Type: {type}")
        elif choice == "2":
            print("Add a new animal")

            name = input("Name: ").strip()
            while len(name) < 2:
                print("Invalid name, please try again.")
                name = input("Name: ").strip()

            species = input("Type: ").strip()
            while species.title() not in ("Cat", "Dog", "Bird", "Ape", "Unknown"):
                print("Invalid Type, please try again.")
                species = input("Type: ").strip()

            colour = input("Colour: ").strip()
            while colour.upper() not in ("BROWN", "BLACK", "WHITE", "ORANGE", "PURPLE", "PINK"):
                print("Invalid colour, please try again.")
                colour = input("Colour: ").strip()

            limb_count = input("Limb Count: ").strip()
            while not limb_count.isnumeric() or int(limb_count) < 0:
                print("Invalid limb count, please try again.")
                limb_count = input("Limb Count: ").strip()

            ani = ",".join( (name.title(), colour.upper(), limb_count, species.title()))

            animals.append(ani)


        elif choice == "3" or choice.lower() in ("exit", "quit"):
            print("Goodbye — saving and exiting.")
            # save_animals(animals)
            break
        else:
            print("Unknown option. Please try again.")

main_menu()
