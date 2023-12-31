from day_01 import sum_of_calibration_values


def test_sum_of_calibration_values():
    lines = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""
    assert sum_of_calibration_values(lines.split()) == 142
