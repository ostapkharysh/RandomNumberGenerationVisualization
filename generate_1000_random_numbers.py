from random import randint
import json


def generate_1000_random_numbers():
    """
    :return: the generated list of 1000 random numbers in a range from 0 to 100
    """
    with open('1000_random_numbers.json', 'w') as f:
        json.dump([randint(0, 100) for _ in range(1000)], f)
    return "The numbers were randomly generated."

