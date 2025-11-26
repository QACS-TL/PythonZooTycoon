import unittest
import animal
import dog
import json

class AnimalTests(unittest.TestCase):

    def Calc_numerical_part_of_id(self):
        high_val = 0
        with open("animals.json") as f:
            for animal in json.load(f):
                high_val = max(high_val, int(animal["id"][:3]))
        high_val += 1
        high_val = f"{high_val:03d}"
        return high_val


    def test_string(self):
        # Arrange
        high_val = self.Calc_numerical_part_of_id()
        expected_result = f"Id: {high_val}-ZOO-CAT-2025, Name: Felix, Species: Cat, Colour: BROWN, Limb Count: 4"
        animal.Animal.count = 0
        ani = animal.Animal(name="Felix", type="Cat", colour="Brown", limb_count=4)

        # Act
        result = ani.__str__()

        # Assert
        self.assertEqual(expected_result, result)


    def test_eat(self):
        # Arrange
        expected_result = "I'm a Cat called Felix using some of my 4 limbs to eat fish."
        ani = animal.Animal(name="Felix", type="Cat", colour="Brown", limb_count=4)
        result = ani.__str__()

        # Act
        result = ani.eat("fish")

        # Assert
        self.assertEqual(expected_result, result)


    def test_Illegal_limb_count(self):
        # Arrange
        expected_result = 0

        # Act
        ani = animal.Animal(name="Felix", type="Cat", colour="Brown", limb_count=-14)

        # Assert
        self.assertEqual(expected_result, ani.limb_count)

    def test_dog_initialiser(self):
        # Arrange
        high_val = 0
        high_val = self.Calc_numerical_part_of_id()
        expected_result = f"Id: {high_val}-ZOO-DOG-2025, Name: Felix, Species: Dog, Colour: ORANGE, Limb Count: 4, Tail Length: 0.75"

        d = dog.Dog(name="Felix", colour="Orange", limb_count = 4, tail_length=0.75)

        # Act
        result = d.__str__()

        # Assert
        self.assertEqual(expected_result, result)

    def test_id_validation_with_good_id(self):
        expected_result = "Id: 001-ZOO-CAT-2025, Name: Felix, Species: Dog, Colour: ORANGE, Limb Count: 4, Tail Length: 0.75"
        d = dog.Dog(id="001-ZOO-CAT-2025", name="Felix", colour="Orange", limb_count = 4, tail_length=0.75)

        # Act
        result = d.__str__()

        # Assert
        self.assertEqual(expected_result, result)
