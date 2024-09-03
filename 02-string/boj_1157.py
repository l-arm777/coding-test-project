# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지
# my_way:
# 1. 각 알파벳 개수를 구한다 -> 문자열의 중복되지 않는 원소만 모은 뒤 각각에 대해 count
# 2. 그 중 최대값을 구한다 -> 알바펫배열에서 max값을 구하고 max값이 여러개면 '?', 유일하면 '값' 출력
# lecture_way: 1. 각 알파벳 개수를 구한다 2. 그 중 최대값을 구한다

user = input().lower()
max_idx = -1
max_val = -1
output = ''

alphabet_array = [0] * (ord('z')-ord('a')+1)

for elem in ''.join(dict.fromkeys(user)):
    idx = ord(elem) - ord('a')
    alphabet_array[idx] += user.count(elem)

# print(alphabet_array)
'''
# 알파벳 개수 구하기
for elem in user:
    idx = ord(elem) - ord('a')
    if alphabet_array[idx] == 0:
       alphabet_array[idx] += user.count(elem) 
       
# count 쓰지 않고 알파벳 개수 구하기
def getAlphabetCount(user):
    user.upper()
    alphabet_array = [0] * 26
    for elem in user:   
        alphabet_array[ord(elem)-ord('A')] += 1
        
    return alphabet_array
'''

for idx in range(len(alphabet_array)):
    if alphabet_array[idx] > max_val:
        max_idx = idx
        max_val = alphabet_array[idx]

if alphabet_array.count(max_val) > 1:
    output = '?'
else:
    output = chr(ord('a') + max_idx).upper()

print(output)
