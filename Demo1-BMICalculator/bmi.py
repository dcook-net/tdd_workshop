class BodyMassIndex(object):

    @staticmethod
    def calculate(height, weight):
        height_in_metered_squared = (height / 100) ** 2
        bmi = weight / height_in_metered_squared
        return round(bmi, 2)