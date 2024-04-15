import src.calc as my_calc

def test_add_two_positive_nums():
    assert my_calc.add_two_nums(1,2) == 3

def test_add_positive_and_negative_nums():
    assert my_calc.add_two_nums(-1,2) == 1

def test_subtract_positive_from_negative():
    assert my_calc.subtract_two_nums(-1,2) == -3

