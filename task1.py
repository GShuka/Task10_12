# task1.py
import os

def process_char(char):
    try:
        int_value = int(char)
        return int_value
    except ValueError:
        return f"Error: '{char}' is not a digit."

if __name__ == "__main__":
    char_input = os.getenv("CHAR_INPUT")

    if char_input is None:
        print("Error: CHAR_INPUT environment variable is not set.")
        exit(1)

    result = process_char(char_input)
    print(result)

