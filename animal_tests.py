import unittest
import animal
import dog


class AnimalTests(unittest.TestCase):
    def test_string(self):
        # Arrange
        expected_result = "Id: 001-ZOO-ANI-2025, Name: Felix, Species: Cat, Colour: BROWN, Limb Count: 4"
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
        expected_result = "Id: 006-ZOO-DOG-2025, Name: Felix, Species: Dog, Colour: ORANGE, Limb Count: 4, Tail Length: 0.75"
        animal.Animal.count = 5
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
