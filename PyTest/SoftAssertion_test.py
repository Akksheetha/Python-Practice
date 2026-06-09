import pytest_check as check

def test_soft():
    print("Start")
    check.equal(1, 2)
    check.equal(2, 3)
    check.equal(3, 4)
    print("End")