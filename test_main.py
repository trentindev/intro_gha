from main import add, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, -1) == 0