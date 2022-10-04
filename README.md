# Tasks

## Easy

1. Fill in the gaps in the implementation of linear search in `linear_search.py`
2. Complete the trace tables for linear search in file `trace_tables.xlsx` assuming this pseudocode for linear search:
  ```vba
  function linear_search(l, x)
    n = len(l)
    for index = 0 to n-1
      if l[index] == x then
        return index
      end if
    next index
    return -1
  end function
  ```

## Medium
1. In the file `positives.py` write a function `all_positive(l)` that takes a list and returns `True` if all numbers inside `l` are positive.
2. In the file `primes.py` complete the function `prime(n)` to see whether the argument given for th parameter `n` is a prime number. As a reminder: `n` is prime if there is no number from `2` to `n-1` that evenly divides `n`.  