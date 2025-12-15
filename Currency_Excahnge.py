"""s
**Currency Exchange**
Your friend Chandler plans to visit exotic countries all around the world. Sadly, Chandler’s math skills aren’t very good. He’s worried about being scammed by currency exchanges during his trip, so he asks you to build a currency calculator for him.
Here are his specifications for the app:

1. Implement a function `estimate_value(budget, exchange_rate)` that returns the estimated value of the exchanged money.

2. Implement a function `exchange_money(budget, exchange_rate)` that returns the exact amount of foreign currency received after exchanging the budget.

3. Implement a function `get_change(budget, exchanging_value)` that returns the remaining amount of money after part of the budget has been exchanged.

4. Implement a function `get_number_of_bills(budget, exchange_rate, bill_value)` that returns the number of whole foreign currency bills that can be obtained.

5. Implement a function `get_leftover_change(budget, exchange_rate, bill_value)` that returns the amount of local currency left after exchanging for the maximum number of whole bills.
The functions should return values and not print anything.
"""
#Program
def exchange_money(budget, exchange_rate):
    return budget/exchange_rate

def get_change(budget, exchanging_value):
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):

    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):

    return round(amount/denomination)

def get_leftover_of_bills(amount, denomination):

    return amount % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):

    exchange_rate = exchange_rate * (1 + spread / 100)
    total_foreign_currency = budget / exchange_rate
    maximum_value = int(total_foreign_currency // denomination) * denomination
    return maximum_value

