from functions import adding, multiplying

def test_add_zeros():
    result = adding(0,0)
    assert result == 0

def test_add_two():
    result = adding(4,5)
    assert result == 9

def test_add_negatives():
    result = adding(-1,-1)
    assert result == -2

def test_add_multiples():
    result = adding(1,2,3,4)
    assert result == 10

def test_multiply_two():
    result = multiplying(1,2)
    assert result == 2

def test_multiply_multiples():
    result = multiplying(1,2,3,4)
    assert result == 24
