# main_project.py

# Import functions from the helper_functions module
from helper_functions import generate_greeting, calculate_average, categorize_numbers, count_word_frequency, find_max_in_dict

def main():
    # Demonstrate generate_greeting function
    print("Demonstrating generate_greeting function:")
    current_hour = 14  # Example: current time is 2 PM
    greeting = generate_greeting(current_hour)
    print(f"At {current_hour} o'clock, we greet with: {greeting}\n")

    # Demonstrate calculate_average function
    print("Demonstrating calculate_average function:")
    numbers = [1, 2, 3, 4, 5]
    average = calculate_average(numbers)
    print(f"The average of {numbers} is: {average}\n")

    # Demonstrate categorize_numbers function
    print("Demonstrating categorize_numbers function:")
    numbers_to_categorize = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    categorized = categorize_numbers(numbers_to_categorize)
    print(f"The categorization of {numbers_to_categorize} is: {categorized}\n")

    # Demonstrate count_word_frequency function
    print("Demonstrating count_word_frequency function:")
    words = ["apple", "banana", "apple", "orange", "banana", "banana"]
    word_frequency = count_word_frequency(words)
    print(f"The word frequencies in {words} are: {word_frequency}\n")

    # Demonstrate find_max_in_dict function
    print("Demonstrating find_max_in_dict function:")
    data = {"Alice": 80, "Bob": 95, "Charlie": 70}
    max_key = find_max_in_dict(data)
    print(f"The key with the highest value in {data} is: {max_key}\n")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
