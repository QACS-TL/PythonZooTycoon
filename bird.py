from animal import Animal

class Bird(Animal):
    _wingspan = 10
    def __init__(self, id=None, name="Anonymous", colour="Brown", limb_count=4, wingspan=10, type="Bird"):
        super().__init__(id=id, name=name, colour=colour, limb_count=limb_count, type=type)
        self.wingspan = wingspan

    @property
    def wingspan(self):
        return self._wingspan

    @wingspan.setter
    def wingspan(self, value):
        if value < 10:
            value = 10
        self._wingspan = value

    def eat(self, food):
        return f"I'm a {self.type} called {self.name} pecking at {food}."

    def tweet(self, number_of_tweets):
        return f"{'tweet ' * number_of_tweets}"

    def __str__(self):
        #base = super().__str__()
        return f"{super().__str__()}, Wingspan: {self.wingspan}"
