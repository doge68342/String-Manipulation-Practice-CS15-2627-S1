def format_title(string_to_process):
    string_to_process = string_to_process.lower()

    string_to_process = string_to_process.replace(" ", "")
    string_to_process = string_to_process.replace(",", " ")
    string_to_process = string_to_process.replace("::", " ")

    print(string_to_process.title())
# Expected Output: The Tale Of Two Cities