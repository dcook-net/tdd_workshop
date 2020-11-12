import pytest
from bmi import BodyMassIndex


# Problem/Requirement:

# Calculate BMI (Body Mass Index) to 2 decimal places using the formula:
#     BMI = mass (kg) / height2 (m)

# Sample Test Data:
# | Weight | Height | Expected BMI |
# | 74 kg  | 184 cm | 21.86        |
# | 84 kg  | 174 cm | 27.74        |
# | 64 kg  | 194 cm | 17.00        |

# @pytest.mark.parametrize('height, weight , expected_bmi', [
#     (184, 74, 21.86),
#     (174, 84, 27.74),
#     (194, 64, 17.00)
# ])
# def test_calculate_bmi(height, weight, expected_bmi):
#     # ACT
#     actual_bmi = BodyMassIndex.calculate(height, weight)
#
#     # ASSERT
#     assert actual_bmi == expected_bmi


@pytest.mark.parametrize('height, weight , expected_bmi', [(184, 74, 21.86), (174, 84, 27.74), (194, 64, 17.00)])
def test_calculate_bmi(height, weight, expected_bmi):
    # ACT
    actual_bmi = BodyMassIndex.calculate(height, weight)

    # ASSERT
    assert actual_bmi == expected_bmi
