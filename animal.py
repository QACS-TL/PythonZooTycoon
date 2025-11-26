import re
import datetime
import json

class Animal:
    _limb_count = 0
    _colour = "Brown"
    _id = None
    #count = 4

    def generate_new_id(self):
        high_val = 0
        with open("animals.json") as f:
            for animal in json.load(f):
                high_val = max(high_val, int(animal["id"][:3]))
        high_val += 1
        return f"{high_val:03d}-ZOO-{self.type[:3].upper()}-{datetime.datetime.now().strftime('%Y')}"

    def __init__(self, id=None, name="Anonymous", colour="Brown", limb_count=4, type="Animal"):
        self.name = name
        self.colour = colour
        self.limb_count = limb_count
        self.type = type
        if id is None:
            self.id = Animal.generate_new_id(self)
        else:
            self.id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not re.search("^[0-9]{3}-ZOO-[A-Z]{3}-(19|20)[0-9]{2}$", value):
            raise ValueError("id must be of the form: 999-ZOO-AAA-YYYY")
        self._id = value

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        if not value.upper() in ("BROWN", "BLACK", "WHITE", "ORANGE", "PURPLE", "PINK"):
            value = "Brown"
        self._colour = value.upper()

    @property
    def limb_count(self):
        return self._limb_count

    @limb_count.setter
    def limb_count(self, value):
        if value < 0:
            value = 0
        self._limb_count = value

    def eat(self, food):
        return f"I'm a {self.type} called {self.name} using some of my {self._limb_count} limbs to eat {food}."

    def move(self, direction, distance):
        return f"I'm an {self.type} called {self.name} moving {direction} for {distance} metres."

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, Species: {self.type}, Colour: {self.colour}, Limb Count: {self.limb_count}"


    def to_dict(self):
        return {
            "type": self.type,
            "id": self.id,
            "name": self.name,
            "colour": self.colour,
            "limb_count": self.limb_count
        }
