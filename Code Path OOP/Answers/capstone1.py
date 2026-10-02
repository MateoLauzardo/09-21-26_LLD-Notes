# PROBLEM 1  (Enum)
# ---------
# A traffic light cycles RED -> GREEN -> YELLOW -> RED. Use an Enum for the

# colors and implement `next_light()` so it returns the next color in the cycle.

# Note: do not use strings like "red" anywhere. The point of an Enum is that a
# typo like "rde" becomes impossible.

# Evaluate the time and space complexity of `next_light()`. Define your variables
# and provide a rationale for why you believe your solution has the stated time
# and space complexity.
# =============================================================================
 
from enum import Enum
 
class Light(Enum):
    #name #value 
    RED = 1
    GREEN = 2
    YELLOW = 3
 
def next_light(light):
        
    if light.name == Light.RED.name:
        return Light.GREEN

    if light.name == Light.GREEN.name:
        return Light.RED
    
    if light.name == Light.YELLOW.name:
        return Light.RED
 
# Complexity of next_light():
# Time: o(n)
# Space:
# Variables:
# Rationale:
 
 
def example_problem_1():
    print(next_light(Light.RED))
    print(next_light(Light.GREEN))
    print(next_light(Light.YELLOW))
    
answer1 = example_problem_1()
 
# Example Output:
# Light.GREEN
# Light.YELLOW
# Light.RED
 