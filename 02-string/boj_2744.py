user = input()
output = ""

for elem in user:
    if elem.isupper(): output += elem.lower()
    else: output += elem.upper()

print(output)
