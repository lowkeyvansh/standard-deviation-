import math

def calculate_std_dev(lst):
    mean = calculate_mean(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    std_dev = math.sqrt(variance)
    return std_dev

print(calculate_std_dev([1, 2, 3, 4, 5]))
