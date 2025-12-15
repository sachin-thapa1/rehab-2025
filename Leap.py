"""A leap year (in the Gregorian calendar) occurs:

In every year that is evenly divisible by 4.
Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
Some examples:

1997 was not a leap year as it's not divisible by 4.
1900 was not a leap year as it's not divisible by 400.
2000 was a leap year!"""

#Program
#method 1
def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

#Method 2
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

#Method 3
def leap_year(year):
    try:
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    except TypeError:
        return False

