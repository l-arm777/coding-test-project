# 한번 센 단어는 제거해버린다

document = input()
keyword = input()

current_idx = 0
keyword_length = len(keyword)
count = 0

while current_idx < len(document):
    if document[current_idx:current_idx+keyword_length] == keyword:
        # print(document[current_idx:current_idx+keyword_length])
        count += 1
        current_idx += keyword_length
    else:
        current_idx += 1

print(count)
