document = input()
keyword = input()
idx_document = 0
count = 0

'''
for idx_document in range(0, len(document)):
    for idx_keyword in range(0, len(keyword)):
        if (idx_document + idx_keyword < len(document) or
                document[idx_document+idx_keyword] != keyword[idx_keyword]):
            break
    count += 1
    idx_document += len(keyword)  # 여전히 for문은 건너뜀없이 연속적으로 진행된다 (vs 자바)
'''

while idx_document < len(document):
    isCheck = True
    for idx_keyword in range(0, len(keyword)):
        if (idx_document + idx_keyword >= len(document) or
                document[idx_document+idx_keyword] != keyword[idx_keyword]):
            isCheck = False
            break

    if isCheck:
        count += 1
        idx_document += len(keyword)
    else:
        idx_document += 1

print(count)
