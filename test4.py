"""
Unit test
"""


# content of test_sample.py
def inc(number):
    """
    This function increment a number
    """
    return number + 1


def test_answer():
    """
    Unit test of inc function
    """
    assert inc(3) == 4