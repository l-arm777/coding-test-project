user_input = input()


def get_alphabet_count(user):
    alphabet_array = [0] * 26

    for elem in user:
        if elem.isupper():
            alphabet_array[ord(elem)-ord('A')] += 1
        else:
            alphabet_array[ord(elem)-ord('a')] += 1

    return alphabet_array


my_array = get_alphabet_count(user_input)

max_value = -1
output = ''
for idx in range(26):
    if my_array[idx] > max_value:
        max_value = my_array[idx]
        output = chr(ord('A')+idx)
    elif my_array[idx] == max_value:
        # 한 번 물음표로 업데이트됐다해서 끝나지 않는다
        # ∵ for문 반복이 26번 모두 공평하게 존재하고, 물음표로 업데이트하고 무조건 반복문이 끝나는 건 아니므로 충분히 재업데이트 가능
        output = '?'
 
print(output)
