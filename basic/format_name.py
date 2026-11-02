string_to_process = "   sMitH, aLeX    "
names = string_to_process.lower().strip().title().split()
full_name = f"{names[1]} {names[0]}"
full_name = full_name.replace(",", "")
print(full_name)
# Expected output: "Alex Smith"