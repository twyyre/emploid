import re

def contains_arabic_letters(input_string):
    # Define a regular expression pattern for Arabic letters
    arabic_letters_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')

    # Check if the input string contains Arabic letters
    return bool(arabic_letters_pattern.search(input_string))

# Test the function
test_string1 = "Hello, 123"
test_string2 = "مرحبا بك"

print(contains_arabic_letters(test_string1))  # Output: False
print(contains_arabic_letters(test_string2))  # Output: True
