import math
def calculate_probability():
    total_distributions = 3**6
    ways_to_choose_3 = math.comb(6, 3)
    ways_to_choose_2 = math.comb(3, 2)
    ways_to_choose_1=1
    valid_distributions = ways_to_choose_3 * ways_to_choose_2 * ways_to_choose_1 * math.factorial(3)
    probability = valid_distributions / total_distributions
    return probability

result = calculate_probability()
print(f"The probability is: {result}")