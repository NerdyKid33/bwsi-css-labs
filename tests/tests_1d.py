import pytest 
from labs.lab_1.lab_1d import two_sum

def test_only_two_integer():
    assert two_sum([1, 2], 3)==[0, 1]
    assert two_sum([-1, -2], -3)==[0, 1]

def test_no_ans():
    assert two_sum([1, 2, 3], 10)==[]
    assert two_sum([], 0)==[]

def test_general(): 
    assert two_sum([2, 5, 10, 643, 32, 12], 655)==[3, 5]
    assert two_sum([-12, 53, -3, 352, 12], 0)==[0, 4]

if __name__=="__main__":
    pytest.main()
 