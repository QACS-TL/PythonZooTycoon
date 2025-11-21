from animal import Animal
from bird import Bird
from cat import Cat
from dog import Dog


def animal_from_dict(data):
    animal_type = data["type"]
    if animal_type.upper() == "DOG":
        return Dog(**data)
    elif animal_type.upper() == "CAT":
        return Cat(**data)
    elif animal_type.upper() == "BIRD":
        return Bird(**data)
    else:
        return Animal(**data)