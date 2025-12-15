"""**Collatz Conjecture**

The Collatz conjecture is a famous unsolved problem in mathematics.

It states that for any positive integer, the following process will eventually reach the number 1:

* If the number is even, divide it by 2.
* If the number is odd, multiply it by 3 and add 1.

Repeat the process with the resulting number.

Your task is to write a function that calculates **how many steps** are required to reach 1, starting from a given positive integer.

If the given number is **zero or negative**, an error should be raised.

The function should return the **number of steps** needed to reach 1 and should not print anything.
"""

#Program
import unittest
from typing import List

def collatz_sequence(n: int) -> List[int]:
    """Return the Collatz sequence starting from n."""
    if n <= 0:
        raise ValueError("Only positive integers are allowed")

    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

def steps(number: int) -> int:
    """Return the number of steps to reach 1 in the Collatz sequence."""
    return len(collatz_sequence(number)) - 1

class TestCollatz(unittest.TestCase):
    def test_steps_zero(self):
        with self.assertRaises(ValueError) as err:
            steps(0)
        self.assertEqual(str(err.exception), "Only positive integers are allowed")

    def test_steps_one(self):
        self.assertEqual(steps(1), 0)

    def test_steps_four(self):
        self.assertEqual(steps(4), 2)  # 4 → 2 → 1

if __name__ == "__main__":
    unittest.main()
