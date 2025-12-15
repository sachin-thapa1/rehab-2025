"""
**Meltdown Mitigation**
In this exercise, we’ll develop a simple control system for a nuclear reactor.
For a reactor to produce power, it must be in a state of **criticality**. If the reactor is operating below criticality, it can become damaged. If the reactor goes beyond criticality, it can overload and result in a **meltdown**. The goal is to mitigate the chances of meltdown and correctly manage the reactor state.

The following three tasks are all related to writing code for maintaining an ideal reactor state:

1. **Check criticality balance**
   Implement a function that determines whether the reactor is in a balanced critical state based on the reactor temperature and the number of neutrons emitted per second.

2. **Determine reactor efficiency**
   Implement a function that calculates the reactor’s efficiency using voltage and current values and categorizes the efficiency level.

3. **Fail-safe mechanism**
   Implement a function that determines the reactor’s safety status based on temperature and neutron emission levels, indicating whether the system is operating safely or is in danger.
All functions should return values and not print anything.

"""
#Program
"""Functions to prevent a nuclear meltdown."""

def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency_percent = (generated_power / theoretical_max_power) * 100

    if efficiency_percent >= 80:
        return "green"
    if efficiency_percent >= 60:
        return "orange"
    if efficiency_percent >= 30:
        return "red"
    return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    product = temperature * neutrons_produced_per_second
    if product < 0.9 *  threshold:
        return "LOW"
    if abs(product - threshold) <= 0.1 * threshold:
        return "NORMAL"
    return "DANGER"
