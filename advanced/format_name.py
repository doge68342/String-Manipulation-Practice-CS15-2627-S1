def format_name(string_to_process):
    names = string_to_process.lower().strip().title().split()
    try:
        full_name = f"{names[1]} {names[0]}"
    except IndexError:
        print("please input two names")
        return False
    full_name = full_name.replace(",", "")
    print(full_name)
    return True