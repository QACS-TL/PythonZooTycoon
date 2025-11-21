from animal import Animal
from bird import Bird
from cat import Cat
from dog import Dog
from factory import animal_from_dict
import sys
import json

ANIMALS_FILE = "animals.json"

def save_animals(animals):
    try:
        data = [animal.to_dict() for animal in animals]
        with open(ANIMALS_FILE, "w") as fh_animals:
            # writer = csv.writer(fh_animals)
            #
            # # write header
            # cols = "name,species,colour,limb_count,id".split(",")
            # writer.writerow(cols)
            #
            # for animal in animals:
            #     writer.writerow(animal.__dict__.values())
            json.dump(data, fh_animals, indent=4)
    except IOError:
        sys.exit("IO Error")

def load_animals():
    # zoo = []
    # zoo.append(Dog(name="Fido", colour="Black", limb_count=4, tail_length=1, type="DOG"))
    # zoo.append(Cat(name="Fifi", colour="White", limb_count=5, whisker_count=12, type="CAT"))
    # zoo.append(Bird(name="Boris", colour="Purple", limb_count=3, wingspan=20, type="BIRD"))
    # zoo.append(Animal(name="Boris", species="Bird", colour="Purple", limb_count=3, type="ANIMAL"))
    # return zoo
    try:
        with open(ANIMALS_FILE, "r") as fh_animals:
            data = json.load(fh_animals)
        return [animal_from_dict(item) for item in data]

    except FileNotFoundError:
        #print("File not found")
        sys.exit("File not found")
    except IOError:
        #print("File not found")
        sys.exit("IO Error")
    except ValueError as ex:
        sys.exit(f"Value Error: animals.csv has a row with a corrupt id: {ex.__str__()}")

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

    #animal_id = get_and_validate_property(lambda a_id:  not re.search("^[0-9]{3}-ZOO-[A-Z]{3}-(19|20)[0-9]{2}$", a_id), "animal_id",)

    # animal_id = input("Enter animal's id: ")
    # while not re.search("^[0-9]{3}-ZOO-[A-Z]{3}-(19|20)[0-9]{2}$", animal_id):
    #     print("Invalid id, please try again")
    #     animal_id = input("Enter animal's id: ")

    name = get_and_validate_property(lambda n: len(n) < 2, "name")
    # name = input_detail("Name")
    # while len(name) < 2:
    #     print("Invalid name, please try again.")
    #     name = input_detail("Name")

    species = get_and_validate_property(lambda s: s.upper() not in ("CAT", "DOG", "BIRD", "APE", "UNKNOWN"), "species").upper()

    colour = get_and_validate_property(lambda c: c.upper() not in ("BROWN", "BLACK", "WHITE", "ORANGE", "PURPLE", "PINK"), "colour").upper()
    # colour = input_detail("Colour")
    # while colour.upper not in ("BROWN", "BLACK", "WHITE", "ORANGE", "PURPLE", "PINK"):
    #     print("Invalid colour, please try again.")
    #     colour = input_detail("Colour")

    limb_count = get_and_validate_property(lambda lc: not lc.isnumeric() or int(lc) < 0, "limb_count")
    # limb_count = input_detail("Limb Count")
    # while not limb_count.isnumeric() or int(limb_count) < 0:
    #     print("Invalid limb count, please try again.")
    #     limb_count = input_detail("Limb Count")

    # Additional type specific props
    ani=None
    try:
        match species:
            case "CAT":
                whisker_count = get_and_validate_property(lambda wc: not wc.isnumeric() or int(wc) < 6, "whisker_count")
                ani = Cat(name=name, colour=colour, limb_count=int(limb_count), whisker_count=int(whisker_count))
            case "DOG":
                tail_length = get_and_validate_property(lambda tl: not tl.isnumeric() or int(tl) < 5, "tail_length")
                ani = Dog(name=name, colour=colour, limb_count=int(limb_count), tail_length=int(tail_length))
            case "BIRD":
                wingspan = get_and_validate_property(lambda ws: not ws.isnumeric() or int(ws) < 10, "wingspan")
                ani = Bird(name=name, colour=colour, limb_count=int(limb_count), wingspan=int(wingspan))
            case _:
                ani = Animal(name=name, colour=colour, limb_count=int(limb_count))

        animals.append(ani)
        save_animals(animals)
    except ValueError as ex:
        print(f"ERROR: {ex}. Animal not added to collection")

def choose_index(max_n):
    try:
        raw = input_detail("Choose number (or blank to cancel)")
        if raw == "":
            print("Cancelled.")
            return None
        n = int(raw)
        if 1 <= n <= max_n:
            return n - 1
        print("Invalid selection")
    except ValueError:
        print("Please enter a number.")
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

    ani.name = get_and_validate_property(lambda n: len(n) < 2, "name", ani.name)
    ani.colour = get_and_validate_property(lambda c: c.upper() not in ("BROWN", "BLACK", "WHITE", "ORANGE", "PURPLE", "PINK"), "colour", ani.colour)
    ani.limb_count = int(get_and_validate_property(lambda lc: not lc.isnumeric() or int(lc) < 0, "limb_count", ani.limb_count))

    match ani.type.upper():
        case "CAT":
            ani.whisker_count = int(get_and_validate_property(lambda wc: not wc.isnumeric() or int(wc) < 6, "whisker_count", ani.whisker_count))
        case "DOG":
            ani.tail_length = int(get_and_validate_property(lambda tl: not tl.isnumeric() or int(tl) < 5, "tail_length", ani.tail_length))
        case "BIRD":
            ani.wingspan = int(get_and_validate_property(lambda ws: not ws.isnumeric() or int(ws) < 10, "wingspan", ani.wingspan))

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
    print(f"Removed {ani.name}")

def feed_animal(animals):
    message_mode = "feed"
    quit_flag = False
    ani, quit_flag = animal_selector(animals, message_mode, quit_flag)
    if quit_flag:
        return

    food = ""
    match ani.type:
        case "CAT":
            food = "fish"
        case "DOG":
            food = "biscuits"
        case "BIRD":
            food = "seeds"
        case _:
            food = "sandwiches"

    msg = ani.eat(food)

    msg += f" You fed the {ani.type} called {ani.name}."

    if ani.type == "DOG":
        msg += " It's wagging its tail happily!"
    elif ani.type =="CAT":
        msg += " It purrs contentedly."
    elif ani.type == "BIRD":
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
