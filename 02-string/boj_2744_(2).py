# 문자열-아스키코드 활용 (4ms 단축)

# 65-90 대문자(A-Z)
# 97-122 소문자(a-z)
# 같은 알파벳 상 대문자, 소문자 차이는 아스키 값으로 32 차이

# 문자열 -> 아스키코드 : ord("str")
# 아스키코드 -> 문자열 : chr(아스키코드)

user = input()
output = ""

for elem in user:
    elem2ascii = ord(elem)
    if 64 < elem2ascii < 91: output += chr(elem2ascii + 32)
    elif 96 < elem2ascii < 123: output += chr(elem2ascii - 32)

print(output)
