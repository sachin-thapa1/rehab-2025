"""Determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)

A scalene triangle has all sides of different lengths."""

#Program
def equilateral(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c or b + c <= a or c + a <= b):
        return False
    return a == b == c

def isosceles(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c or b + c <= a or c + a <= b):
        return False
    return a == b or b == c or a == c

def scalene(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c or b + c <= a or c + a <= b):
        return False
    return a != b and b != c and a != c

