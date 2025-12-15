"""Calculate the number of grains of wheat on a chessboard.

A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.

Write code that calculates:

the number of grains on a given square
the total number of grains on the chessboard"""

#Program
def square(n):
    if not 0 < n <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 **(n-1)

def total():
    return (2 ** 64) - 1
