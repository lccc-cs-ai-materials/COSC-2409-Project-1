# Guided Project: Demonstrating Python Infrastructure with Functions, Modules, and TDD

## **Overview**
In this project, you will gain hands-on experience with structured Python programming techniques, including:
1. **Functions**: How to use reusable code blocks.
2. **Modules**: Organizing code into separate files for clarity and reusability.
3. **Test-Driven Development (TDD)**: Using tests to guide your implementation and ensure correctness.

This project is designed to demonstrate the power of these tools by having you integrate and run pre-written code, rather than writing new functionality from scratch. Your role is to:
- Understand the structure of the project.
- Use the provided code and see how it interacts with test cases.
- Explore additional exercises to practice loops, lists, dictionaries, and conditional statements.

---

## **Project Files**
### **1. Project Structure**
The project is organized as follows:

```plaintext
project_directory/
    main_project.py       # Main script to demonstrate functionality
    helper_functions.py   # Contains reusable functions
    test_project.py       # Pytest-based tests for the project
```

You will use the `helper_functions.py` module and modify pre-defined function stubs in `main_project.py`. The `test_project.py` file contains tests to verify functionality.

We use functions in this code.  We will cover functions in a lot more depth later, but use them here to help facilitate test driven development.  This is different that other start of semester courses, and that's why we're using a guided walkthrough for this first project.  Functions are a key programming structure that give use small parts of a larger project that are testable and understandable.   

We will demonstrate how they come together and allow us to test both parts of a larger project and the entire project as a whole.


By using GitHub Classrooms, you'll be submitting your code and having it automatically tested by a continuous integration (CI) system that runs these unit tests. The tests will provide feedback on whether your code works as expected, and you will be able to make improvements to pass these tests.


---

## **Code Walkthrough**

### **1. Provided Code**
#### **helper_functions.py**

This file contains two functions that will be used in the main project:

```python
# Generates a greeting message based on the time of day
def generate_greeting(hour):
    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    elif 18 <= hour <= 22:
        return "Good evening!"
    else:
        return "Hello!"

# Calculates the average of a list of numbers
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
```

#### **test_project.py**

This file contains tests for the `helper_functions` module:

```python
import pytest
from helper_functions import generate_greeting, calculate_average

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
```

---

### **2. Exercises**

Below are additional exercises to help you practice loops, lists, dictionaries, and conditional statements:

#### **Exercise 1: Categorize Numbers**
Write a function to categorize numbers into "odd" or "even" and store them in a dictionary:

```python
def categorize_numbers(numbers):
    result = {"odd": [], "even": []}
    for num in numbers:
        if num % 2 == 0:
            result["even"].append(num)
        else:
            result["odd"].append(num)
    return result

# Example usage
numbers = [1, 2, 3, 4, 5, 6]
print(categorize_numbers(numbers))  # Output: {'odd': [1, 3, 5], 'even': [2, 4, 6]}
```

#### **Exercise 2: Word Frequency Counter**
Write a function that counts the frequency of each word in a list:

```python
def count_word_frequency(words):
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Example usage
words = ["apple", "banana", "apple", "orange", "banana", "banana"]
print(count_word_frequency(words))  # Output: {'apple': 2, 'banana': 3, 'orange': 1}
```

#### **Exercise 3: FizzBuzz Implementation**
Write a loop that prints numbers from 1 to 50, but:
- Prints "Fizz" for multiples of 3.
- Prints "Buzz" for multiples of 5.
- Prints "FizzBuzz" for multiples of both.

```python
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

#### **Exercise 4: Find Maximum in a Dictionary**
Write a function that finds the key with the maximum value in a dictionary:

```python
def find_max_in_dict(data):
    return max(data, key=data.get)

# Example usage
data = {"Alice": 80, "Bob": 95, "Charlie": 70}
print(find_max_in_dict(data))  # Output: 'Bob'
```

---

## **Objectives**
By completing this project and exercises, you’ll:
1. Understand how functions organize and simplify code.
2. Gain experience working with modules to import and reuse functionality.
3. Learn how TDD ensures code correctness and provides feedback during development.
4. Practice key Python concepts like loops, lists, dictionaries, and conditionals.

---

## **Next Steps**
1. Copy the provided code into your project files.
2. Run the test cases using `pytest` to observe how the tests validate functionality.
3. Complete the exercises to reinforce your understanding of Python basics.
4. Reflect on how these concepts apply to larger, real-world projects.

