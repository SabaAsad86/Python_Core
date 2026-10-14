
full_name = input("Enter your full name: ").strip()

parts = full_name.split()

first_name = parts[0]
last_name = parts[-1]

initials = first_name[0].upper() + ". " + last_name[0].upper() + "."

print("Initials:", initials)
print("Uppercase:", full_name.upper())
print("Reversed:", full_name[::-1])
