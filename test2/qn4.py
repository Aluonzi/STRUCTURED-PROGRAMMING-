#prog function that checks if a string is the same as the input string

def check_string_equality(input_string, string_to_check):
    return input_string.lower() == string_to_check.lower()

#test the function using a string
#we create a variable input_string
input_string = "Henry is great"
string_to_check = "henry is great"

print(check_string_equality(input_string, string_to_check))  