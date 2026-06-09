import pytest

def test_sample():

    print("Start")
    pytest.assume(1 == 1)
    pytest.assume(2 == 3)
    pytest.assume(3 == 4)

    print("Test completed")