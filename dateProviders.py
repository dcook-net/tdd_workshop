from datetime import date


class RealDateProvider(object):

    def get_current_date(self):
        return date.today()


class FakeDateProvider(object):

    def __init__(self, current_date=None):
        if current_date is None:
            current_date = date(2000, 1, 1)

        self.set_date(current_date)

    def get_current_date(self):
        return self.date

    def today(self):
        return self.date

    def set_date(self, d):
        self.date = d
