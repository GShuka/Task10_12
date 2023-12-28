# task1.py
def char_to_integer(char_variable):
    try:
        result = int(char_variable)
        return result
    except ValueError:
        return "Input is not a digit."

char_input = input("Enter a character: ")
result = char_to_integer(char_input)
print("Result:", result)

