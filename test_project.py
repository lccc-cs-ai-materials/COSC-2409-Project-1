# test_project.py

import pytest
from helper_functions import generate_greeting, calculate_average, categorize_numbers, count_word_frequency, find_max_in_dict

# Test for generate_greeting
def test_generate_greeting():
    assert generate_greeting(8) == "Good morning!"
    assert generate_greeting(14) == "Good afternoon!"
    assert generate_greeting(20) == "Good evening!"
    assert generate_greeting(2) == "Hello!"

# Test for calculate_average
def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([]) == None
    assert calculate_average([10, 20, 30]) == 20.0

# Test for categorize_numbers
def test_categorize_numbers():
    numbers = [1, 2, 3, 4, 5, 6]
    expected_output = {'odd': [1, 3, 5], 'even': [2, 4, 6]}
    assert categorize_numbers(numbers) == expected_output
    assert categorize_numbers([7, 8, 9, 10]) == {'odd': [7, 9], 'even': [8, 10]}
    assert categorize_numbers([0, 1, 2, 3, 4]) == {'odd': [1, 3], 'even': [0, 2, 4]}

# Test for count_word_frequency
def test_count_word_frequency():
    words = ["apple", "banana", "apple", "orange", "banana", "banana"]
    expected_output = {'apple': 2, 'banana': 3, 'orange': 1}
    assert count_word_frequency(words) == expected_output
    assert count_word_frequency(["dog", "cat", "dog", "fish"]) == {'dog': 2, 'cat': 1, 'fish': 1}
    assert count_word_frequency([]) == {}

# Test for find_max_in_dict
def test_find_max_in_dict():
    data = {"Alice": 80, "Bob": 95, "Charlie": 70}
    assert find_max_in_dict(data) == 'Bob'
    assert find_max_in_dict({"x": 10, "y": 20, "z": 15}) == 'y'
    assert find_max_in_dict({"A": 5, "B": 5, "C": 5}) == 'A'  # In case of ties, returns the first encountered max

# Test for FizzBuzz (direct loop test)
def test_fizzbuzz():
    fizzbuzz_output = []
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_output.append("FizzBuzz")
        elif i % 3 == 0:
            fizzbuzz_output.append("Fizz")
        elif i % 5 == 0:
            fizzbuzz_output.append("Buzz")
        else:
            fizzbuzz_output.append(str(i))
    
    # Verify that expected outputs match for some values
    assert fizzbuzz_output[2] == "Fizz"  # Index 2 represents the 3rd number: 3 (Fizz)
    assert fizzbuzz_output[4] == "Buzz"  # Index 4 represents the 5th number: 5 (Buzz)
    assert fizzbuzz_output[14] == "FizzBuzz"  # Index 14 represents the 15th number: 15 (FizzBuzz)
    assert fizzbuzz_output[0] == "1"  # First element should be "1"
