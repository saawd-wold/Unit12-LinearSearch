from linear_search import linear_search
from positives import all_positive
from primes import prime

def test_ls():
    try:
        assert linear_search([1,2,3,4], 4) == 3, "Didn't return correct index when element is present!"
        assert linear_search([1,2,3,4], 5) == -1, "Didn't return -1 when element was not present!"
    except Exception as e:
        assert False, "Got an exception while running gap-filling exercise--fix your code!!!!!!"

def test_prime():
    assert prime(11), "Didn't get that 11 is a prime number!"
    assert not prime(27), "Didn't get that 27 is NOT a prime number!"
    assert prime(2**20-3), "Didn't get that 2^20-3 is prime!"

def test_positive():
    assert all_positive([1,2,3,4])
    assert not all_positive([0,1,2,3])
    assert not all_positive([-1,0,1,2])
