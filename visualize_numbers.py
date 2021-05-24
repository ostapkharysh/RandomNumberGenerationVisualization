import json
import matplotlib.pyplot as plt
from collections import Counter


def visualize_numbers(json_file):
    """
    :param json_file: that stores a list of numbers
    :return: the barplot distribution visualization in PNG format
    """
    # Opening JSON file
    f = open(json_file, )
    numbers = json.load(f)
    calculated_numbers = Counter(numbers)
    fig = plt.figure(figsize=(10, 5))
    plt.bar(calculated_numbers.keys(), calculated_numbers.values(), color='maroon',
            width=0.4)

    plt.xlabel("Numbers")
    plt.ylabel("Occurence")
    plt.title("Sum of randomly occured numbers")
    plt.savefig("random_numbers_count_visualization.png")
    return "The barplot was successfully constructed."

print(visualize_numbers('1000_random_numbers.json'))
