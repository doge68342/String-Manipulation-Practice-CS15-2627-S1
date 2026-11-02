from format_list import format_list
from format_name import format_name
from format_title import format_title
from process_numbers import process_numbers

print("Choose how you would like to process a string:")
print()
print("1. Format a Name")
print("2. Format a Title")
print("3. Format a List")
print("4. Process Numbers")
print()
def get_function():
    try:
        function = int(input("Enter your choice: "))
        if function > 0 and function < 5:
            return function
        else:
            print("invalid function")
            return get_function()
    except ValueError:
        print("invalid function")
        return get_function()
function = get_function()

while True:
    string_to_process = input("Enter the string to process: ")
    print()
    print("Processed String:")

    if function == 1:
        if format_name(string_to_process) == True:
            break
    if function == 2:
        format_title(string_to_process)
        break
    if function == 3:
        format_list(string_to_process)
        break
    if function == 4:
        if process_numbers(string_to_process) == True:
            break