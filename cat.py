from animal import Animal

class Cat(Animal):
    _whisker_count = 10
    def __init__(self, id=None, name="Anonymous", colour="Brown", limb_count=4, whisker_count=6, type="Cat"):
        super().__init__(id=id, name=name, colour=colour, limb_count=limb_count, type=type)
        self.whisker_count = whisker_count

    @property
    def whisker_count(self):
        return self._whisker_count

    @whisker_count.setter
    def whisker_count(self, value):
        if value < 6:
            value = 6
        self._whisker_count = value

    def eat(self, food):
        return f"I'm a {self.type} called {self.name} ignoring {food}."

    def meow(self, number_of_meows):
        return f"{'meow ' * number_of_meows}"

    def __str__(self):
        #base = super().__str__()
        return f"{super().__str__()}, Whisker Count: {self.whisker_count}"
