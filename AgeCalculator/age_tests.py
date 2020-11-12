from datetime import date
from AgeCalculator.age import AgeCalc2, AgeCalc3
from dateProviders import FakeDateProvider


def test_calculate_age_from_dob_constructor_injection():
    # ARRANGE
    fake_current_date_provider = FakeDateProvider(date(2020, 11, 5))

    calc = AgeCalc2(fake_current_date_provider)
    dob = date(2000, 1, 1)
    # ACT
    actual_age = calc.calculate_age_from_dob(dob)

    # ASSERT
    assert actual_age == 20


def test_calculate_age_from_dob_method_injection():
    # ARRANGE
    effective_current_date = date(2020, 11, 5)
    dob = date(2000, 1, 1)

    # ACT
    actual_age = AgeCalc3.calculate_age_from_dob(dob, effective_current_date)

    # ASSERT
    assert actual_age == 20
