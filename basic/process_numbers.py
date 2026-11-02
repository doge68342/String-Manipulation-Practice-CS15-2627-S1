def format_list(string_to_process):
    string_to_process = "  18,27,35,20  "
    string_to_process = string_to_process.strip()
    string_to_process = string_to_process.replace(",", " ")
    strings_to_process = string_to_process.split()
    numbers_to_process = []
    for string in strings_to_process:
        numbers_to_process.append(int(string))

    total = 0
    for num in numbers_to_process:
        total += num



    print(f"Total: {total}")
    print(f"Average: {total / len(numbers_to_process)}")

# Expected Output:
# "Total: 100"
# "Average: 25.0"