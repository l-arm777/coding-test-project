document = input()
len_document = len(document)

keyword = input()
len_keyword = len(keyword)

transfer_document = document.replace(keyword, "")
# print(transfer_document)
len_transfer_document = len(transfer_document)

count = (len_document - len_transfer_document) // len_keyword
print(count)
