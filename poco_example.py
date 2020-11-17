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

    # Don't do this...You are basically testing the Python works. That's not your job, that's the job of the people that work on Python!
    # If you are doing TDD correctly, you will be using these properties in your code anyway.
    # And that code will be making a previously failing test pass
    # So it should be tested implicitly, without the need to explicitly write this sort of test....
    # which you will need to maintain........FOREVER!
    assert person._firstname == first_name
    assert person._surname == surname
    assert person._dob == dob
    assert person._height == height
    assert person._weight == weight
