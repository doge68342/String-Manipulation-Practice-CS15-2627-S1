def process_numbers(string_to_process):
    string_to_process = string_to_process.strip()
    strings_to_process = string_to_process.split(",")
    numbers_to_process = []
    for string in strings_to_process:
        try:
            numbers_to_process.append(int(string))
        except ValueError:
            print("Invalid input, all inputs must be numbers seperated by commas")
            return False

    total = 0
    for num in numbers_to_process:
        total += num

    print(f"Total: {total}")
    print(f"Average: {total / len(numbers_to_process)}")
    return True

# Expected Output:
# "Total: 100"
# "Average: 25.0"