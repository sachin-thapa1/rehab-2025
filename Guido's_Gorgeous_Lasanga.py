"""
**Guido’s Gorgeous Lasagna**
You’re going to write some code to help you cook a gorgeous lasagna from your favorite cookbook. You have five tasks, all related to cooking your recipe. ([Exercism][1])
1. **Define expected bake time in minutes as a constant
   Define the `EXPECTED_BAKE_TIME` constant that represents how many minutes the lasagna should bake in the oven (40 minutes). ([Exercism][1])

2. **Calculate remaining bake time in minutes**
   Complete the `bake_time_remaining()` function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the `EXPECTED_BAKE_TIME` constant. ([Exercism][1])

3. **Calculate preparation time in minutes**
   Define the `preparation_time_in_minutes()` function that takes the number of layers as an argument and returns how many minutes you would spend making them (each layer takes 2 minutes). ([Exercism][1])

4. **Calculate total elapsed time (prepping + baking) in minutes**
   Define the `elapsed_time_in_minutes()` function that takes two parameters — `number_of_layers` and `elapsed_bake_time` — and returns the total minutes you have been cooking: preparation time plus baking time.
5. **Update the recipe with notes**
   Add docstrings to the functions.
"""
#Program
EXPECTED_BAKING_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Return the remaining bake time with elapsed bake time"""
    return EXPECTED_BAKING_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Return preparation time based on number of layers"""
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layer, elapsed_bake_time):
    """Return total time spent: preparation time + elapsed time"""
    return preparation_time_in_minutes(number_of_layer) + elapsed_bake_time
#examples
# Test the functions
print("Expected bake time:", EXPECTED_BAKING_TIME)
print("Bake time remaining after 30 minutes:", bake_time_remaining(30))
print("Preparation time for 3 layers:", preparation_time_in_minutes(3))
print("Elapsed time for 3 layers and 20 minutes baking:", elapsed_time_in_minutes(3, 20))

