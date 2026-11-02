def format_name(string_to_process):
    names = string_to_process.lower().strip().title().split()
    full_name = f"{names[1]} {names[0]}"
    full_name = full_name.replace(",", "")
    print(full_name)
format_name("asdf, fdsa")