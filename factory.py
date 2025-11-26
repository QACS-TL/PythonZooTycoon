from animal import Animal
from bird import Bird
from cat import Cat
from dog import Dog


def animal_from_dict(data):
    animal_type = data["type"]
    if animal_type.title() == "Dog":
        return Dog(**data)
    elif animal_type.title() == "Cat":
        return Cat(**data)
    elif animal_type.title() == "Bird":
        return Bird(**data)
    else:
        return Animal(**data)