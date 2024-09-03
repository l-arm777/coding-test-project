# 문자열 內 중복제거O, 순서보장X -> ''.join(dict.fromkeys(str)) return 문자열
# a-z 갯수 -> 26개
# IndexError ∵ 두 단어 길이가 같을 거라는 보장이 없음
input1 = input()
input2 = input()

output = 0
# <abbr> alphabet_array1, alphabet_array2 = [[0] * (ord('z') - ord('a') + 1) for _ in range(2)]
# <detail> alphabet_array1 = [0] * (ord('z') - ord('a')); alphabet_array2 = [0] * (ord('z') - ord('a')); can be detailed
# caution "+1"


def set_array(user):
    alphabet_array = [0] * (ord('z') - ord('a') + 1)
    for elem in ''.join(dict.fromkeys(user)):
        index = ord(elem) - ord('a')
        alphabet_array[index] += user.count(elem)

    return alphabet_array


alphabet_array1 = set_array(input1)
alphabet_array2 = set_array(input2)

"""
for elem in ''.join(dict.fromkeys(input1)):
    idx = ord(elem) - ord('a')
    alphabet_array1[idx] += input1.count(elem)

for elem in ''.join(dict.fromkeys(input2)):
    idx = ord(elem) - ord('a')
    alphabet_array2[idx] += input2.count(elem)
"""

for idx in range(len(alphabet_array1)):
    diff = abs(alphabet_array1[idx] - alphabet_array2[idx])
    if diff > 0:
        output += diff

print(output)
