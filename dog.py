from animal import Animal

class Dog(Animal):
    _tail_length = 0.2
    def __init__(self, id=None, name="Anonymous", colour="Brown", limb_count=4, tail_length=0.25, type="Dog"):
        super().__init__(id=id, name=name, colour=colour, limb_count=limb_count, type=type)
        self.tail_length = tail_length

    @property
    def tail_length(self):
        return self._tail_length

    @tail_length.setter
    def tail_length(self, value):
        if value < 0.05:
            value = 0.05
        self._tail_length = value

    def eat(self, food):
        return super().eat(food) + " Gobble Gobble Slobber"

    def bark(self, number_of_woofs):
        return f"{'woof ' * number_of_woofs}"

    def __str__(self):
        #base = super().__str__()
        return f"{super().__str__()}, Tail Length: {self.tail_length}"
