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

def get_and_validate_property(func, prop_name, prop=None):
    value = "-1" # Flag to force first attempt into loop
    while value == "-1" or func(value):
        if value != "-1":
            print(f"Invalid {prop_name}, please try again")
        value = input(f"Enter animal {prop_name}{': ' if prop is None else f' (currently: {prop}): '}")
        if prop is not None and value == "":  # i.e. if in "edit" mode where empty string = don't change the property's value
            return prop
    return value

def add_animal(animals):
    print("Add a new animal")
    name = get_and_validate_property(lambda n: len(n) < 2, "name")
    species = get_and_validate_property(lambda s: s.title() not in ("Cat", "Dog", "Bird", "Ape", "Unknown"), "species").title()
    colour = get_and_validate_property(lambda c: c.upper() not in ("BROWN", "BLACK", "WHITE", "ORANGE", "PURPLE", "PINK"), "colour").upper()
    limb_count = get_and_validate_property(lambda lc: not lc.isnumeric() or int(lc) < 0, "limb_count")

    # Additional type specific props
    ani=None
    ani = {"name":name, "colour":colour, "limb_count":int(limb_count), "type":species}

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

    ani["name"] = get_and_validate_property(lambda n: len(n) < 2, "name", ani["name"])
    ani["colour"] = get_and_validate_property(lambda c: c.upper() not in ("BROWN", "BLACK", "WHITE", "ORANGE", "PURPLE", "PINK"), "colour", ani["colour"])
    ani["limb_count"] = int(get_and_validate_property(lambda lc: not lc.isnumeric() or int(lc) < 0, "limb_count", ani["limb_count"]))

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
    elif ani["type"] =="Cat":
        msg += " It purrs contentedly."
    elif ani["type"] == "Bird":
        msg += " It chirps sweetly."
    else:
        msg += " It seems satisfied."
    print(msg)

def input_detail(prompt, default = None):
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
