import sys

def save_animals(animals):
    pass


def load_animals():
    animals = []
    animals.append({"name": "Fido", "colour": "Black", "limb_count": 4, "type": "Dog"})
    animals.append({"name": "Fifi", "colour": "White", "limb_count": 5, "type": "Cat"})
    animals.append({"name": "Oscar", "colour": "Orange", "limb_count": 3, "type": "Bird"})
    animals.append({"name": "Boris", "colour": "Purple", "limb_count": 3, "type": "Animal"})
    return animals


def list_animals(animals):
    for i, a in enumerate(animals, start=1):
        print(f"{i}: {a}")


def add_animal(animals):
    print("Add a new animal")

    name = input_detail("Name")
    while len(name) < 2:
        print("Invalid name, please try again.")
        name = input_detail("Name")

    species = input_detail("Species")
    while species.title() not in ("Cat", "Dog", "Bird", "Ape", "Unknown"):
        print("Invalid type, please try again.")
        species = input_detail("Type")

    colour = input_detail("Colour")
    while colour.upper() not in ("BROWN", "BLACK", "WHITE", "ORANGE", "PURPLE", "PINK"):
        print("Invalid colour, please try again.")
        colour = input_detail("Colour")

    limb_count = input_detail("Limb Count")
    while not limb_count.isnumeric() or int(limb_count) < 0:
        print("Invalid limb count, please try again.")
        limb_count = input_detail("Limb Count")

    ani = None
    ani = {"name": name.title(), "colour": colour.upper(), "limb_count": int(limb_count), "type": species.title()}

    animals.append(ani)
    save_animals(animals)


def choose_index(max_n):
    raw = input_detail("Choose number (or blank to cancel)")
    if raw == "":
        print("Cancelled.")
        return None
    n = int(raw)
    if 1 <= n <= max_n:
        return n - 1
    print("Invalid selection")
    return None


def animal_selector(animals, message_mode, quit_flag):
    print(f"{message_mode.title()} animals")
    if not animals:
        print(f"No animals to {message_mode}.")
        quit_flag = True
    list_animals(animals)
    idx = choose_index(len(animals))
    if idx is None:
        quit_flag = True
        return None, quit_flag
    ani = animals[idx]
    return ani, quit_flag

def edit_animal(animals):
    message_mode = "edit"
    quit_flag = False
    ani, quit_flag = animal_selector(animals, message_mode, quit_flag)
    if quit_flag:
        return
    print("Current attributes (leave blank to keep):")

    name= "-1"
    while name == "-1" or len(name) < 2:
        if name != "-1":
            print("Invalid name, please try again.")
        name = input_detail(f"Enter animal Name (currently: {ani['name']}): ")
        if name == "":
            name = ani["name"]
            break
    ani["name"] = name.title()

    colour= "-1"
    while colour == "-1" or colour.upper() not in ("BROWN", "BLACK", "WHITE", "ORANGE", "PURPLE", "PINK"):
        if colour != "-1":
            print("Invalid colour, please try again.")
        colour = input_detail(f"Enter animal Colour (currently: {ani['colour']}): ")
        if colour == "":
            colour = ani["colour"]
            break
    ani["colour"] = colour.upper()

    limb_count = "-1"
    while limb_count == "-1" or not limb_count.isnumeric() or int(limb_count) < 0:
        if limb_count != "-1":
            print("Invalid limb count, please try again.")
        limb_count = input_detail(f"Enter animal limb count (currently: {ani['limb_count']}): ")
        if limb_count == "":
            limb_count = ani["limb_count"]
            break
    ani["limb_count"] = int(limb_count)

    save_animals(animals)
    print("Saved changes.")


def remove_animal(animals):
    message_mode = "remove"
    quit_flag = False
    ani, quit_flag = animal_selector(animals, message_mode, quit_flag)
    if quit_flag:
        return

    animals.remove(ani)
    save_animals(animals)
    print(f"Removed {ani["name"]}")


def feed_animal(animals):
    message_mode = "feed"
    quit_flag = False
    ani, quit_flag = animal_selector(animals, message_mode, quit_flag)
    if quit_flag:
        return

    food = ""
    match ani["type"]:
        case "Cat":
            food = "fish"
        case "Dog":
            food = "biscuits"
        case "Bird":
            food = "seeds"
        case _:
            food = "sandwiches"

    msg = f"I'm a {ani["type"]} called {ani["name"]} using some of my {ani["limb_count"]} limbs to eat {food}."

    msg += f" You fed the {ani["type"]} called {ani["name"]}."

    if ani["type"] == "Dog":
        msg += " It's wagging its tail happily!"
    elif ani["type"] == "Cat":
        msg += " It purrs contentedly."
    elif ani["type"] == "Bird":
        msg += " It chirps sweetly."
    else:
        msg += " It seems satisfied."
    print(msg)


def input_detail(prompt, default=None):
    return input(f"{prompt}: ").strip()


def print_menu():
    print()
    print("Animals App - Menu")
    print("1) List animals")
    print("2) Add animal")
    print("3) Edit animal")
    print("4) Remove animal")
    print("5) Feed animal")
    print("6) Exit")


def main_menu():
    animals = load_animals()
    while True:
        print_menu()
        choice = input_detail("Choose an option")
        if choice == "1":
            list_animals(animals)
        elif choice == "2":
            add_animal(animals)
        elif choice == "3":
            edit_animal(animals)
        elif choice == "4":
            remove_animal(animals)
        elif choice == "5":
            feed_animal(animals)
        elif choice == "6" or choice.lower() in ("exit", "quit"):
            print("Goodbye — saving and exiting.")
            # save_animals(animals)
            break
        else:
            print("Unknown option. Please try again.")

main_menu()
