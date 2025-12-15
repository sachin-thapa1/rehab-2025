"""Write some code to determine whether a number is an Armstrong number."""
#Program
def is_armstrong_number(number):
    if number < 0:
        raise ValueError("Positive integers only.")

    string = str(number)
    k = len(string)

    total = sum(int(i) ** k for i in string)
    return total == number
#Examples
print(is_armstrong_number(619))
print(is_armstrong_number(153))
