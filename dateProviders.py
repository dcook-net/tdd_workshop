from datetime import date


class RealDateProvider(object):

    # RealDateProvider has a dependency on the datetime object, and uses it to provide the actual date to callers/consumers
    # It's not deterministic, just like when you take a direct dependency on the datetime object
    # However, RealDateProvider puts the datetime behaviour behind a facade or contract

    def get_current_date(self):
        return date.today()


class FakeDateProvider(object):

    # FakeDateProvider implements all the behaviour outlined by the RealDateProvider: it fullfils the contractual obligations
    # But it IS deterministic, and therefore more useful for testing.
    # It also provides default values and helper functions that make consuming it in tests more convenient/easier

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
