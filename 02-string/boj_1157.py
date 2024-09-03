user = input().lower()
max_idx = 0
max_val = 0
output = ''

alphabet_array = [0] * (ord('z')-ord('a')+1)

for elem in ''.join(dict.fromkeys(user)):
    idx = ord(elem) - ord('a')
    alphabet_array[idx] += user.count(elem)

# print(alphabet_array)

for idx in range(len(alphabet_array)):
    if alphabet_array[idx] > max_val:
        max_idx = idx
        max_val = alphabet_array[idx]

if alphabet_array.count(max_val) > 1:
    output = '?'
else:
    output = chr(ord('a') + max_idx).upper()

print(output)
