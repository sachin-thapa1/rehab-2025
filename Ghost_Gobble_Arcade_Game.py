"""

**Ghost Gobble Arcade Game**

In this exercise, you need to implement some rules from *Pac‑Man*, the classic 1980s‑era arcade game.([Exercism][1])

You must write four functions that evaluate game states using Boolean logic.([Exercism][1])

1. **Define if Pac‑Man eats a ghost**
   Define the `eat_ghost()` function that takes two parameters — whether Pac‑Man has a power pellet active and whether Pac‑Man is touching a ghost — and returns a Boolean value indicating if Pac‑Man can eat the ghost. The function should return **True only if Pac‑Man has a power pellet active and is touching a ghost**.([Exercism][1])

2. **Define if Pac‑Man scores**
   Define the `score()` function that takes two parameters — whether Pac‑Man is touching a power pellet and whether Pac‑Man is touching a dot — and returns a Boolean value indicating if Pac‑Man scored. The function should return **True if Pac‑Man is touching a power pellet or a dot**.([Exercism][1])

3. **Define if Pac‑Man loses**
   Define the `lose()` function that takes two parameters — whether Pac‑Man has a power pellet active and whether Pac‑Man is touching a ghost — and returns a Boolean value indicating if Pac‑Man loses. The function should return **True if Pac‑Man is touching a ghost and does *not* have a power pellet active**.([Exercism][1])

4. **Define if Pac‑Man wins**
   Define the `win()` function that takes three parameters — whether Pac‑Man has eaten all dots, whether Pac‑Man has a power pellet active, and whether Pac‑Man is touching a ghost — and returns a Boolean value indicating if Pac‑Man wins. The function should return **True only if Pac‑Man has eaten all the dots and has not lost the game according to the `lose()` rule**.
    """
#Program
def eat_ghost(power_pallet_active, touching_ghost):
   return power_pallet_active and touching_ghost

def score(touching_power_pallet, touching_dot):
   return touching_power_pallet or touching_dot

def lose(power_pallet_active, touching_ghost):
   return touching_ghost and power_pallet_active

def win(has_eaten_all_dots, power_pallet_active, touching_ghost):
   return has_eaten_all_dots and not lose(power_pallet_active, touching_ghost)

#Examples:
print(eat_ghost(True, True))      # True
print(eat_ghost(False, True))     # False

print(score(True, False))         # True
print(score(False, False))        # False

print(lose(False, True))          # False
print(lose(True, True))           # True

print(win(True, False, False))    # True
print(win(True, False, True))     # False

