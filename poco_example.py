from datetime import date


class Person(object):
    def __init__(self, firstname, surname, dob, height, weight):
        self._firstname = firstname
        self._surname = surname
        self._dob = dob
        self._height = height
        self._weight = weight


def test_properties_set_correctly():
    first_name = 'Mike'
    surname = 'Place'
    dob = date(2020, 11, 5)
    height = 184
    weight = 78

    person = Person(first_name, surname, dob, height, weight)

    assert person._firstname == first_name
    assert person._surname == surname
    assert person._dob == dob
    assert person._height == height
    assert person._weight == weight
