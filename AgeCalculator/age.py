from datetime import date


class AgeCalc(object):

    @staticmethod
    def calculate_age_from_dob(dob):
        # This function is hard to test as we have no way to control what our dependency (the datetime object) will
        # return when we call it's methods. Our Tests may pass now, but eventually they will start to fail because
        # the result of calling our dependency means our expected results are no longer correct....in this case,
        # we expect the person to be younger than the calculate method is returning.

        # We have no way to control the dependency because it is Implicit (created within this class, rather than
        # outside and passed in) and we are tightly coupled to an specific implementation of datetime
        today = date.today()

        difference_in_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        return int(difference_in_years)


class AgeCalc2(object):
    # This class no longer takes an Implicit dependency on the datetime object
    # Instead it has an Explicit dependency on an abstraction (datetime_provider)
    # It is Explict because it needs to be supplied in order to create an instance of the class
    def __init__(self, datetime_provider):
        self.datetime_provider = datetime_provider

    def calculate_age_from_dob(self, dob):
        # The datetime_provider abstraction still allows us to get the the current date
        # But this class no longer has responsibility of managing the dependency
        today = self.datetime_provider.today()

        difference_in_years = today.year - dob.year - \
                              ((today.month, today.day) < (dob.month, dob.day))

        return int(difference_in_years)


class AgeCalc3(object):

    # This solution takes a more Functional approach to 'Dependency Injection' by supplying the
    # current date as an argument
    # This makes the dependency Explicit (as you can't use this function without it), and moves the responsibility to
    # managing the datetime object out of AgeCalc3's list of concerns
    @staticmethod
    def calculate_age_from_dob(dob, today):
        difference_in_years = today.year - dob.year - \
                              ((today.month, today.day) < (dob.month, dob.day))

        return int(difference_in_years)
