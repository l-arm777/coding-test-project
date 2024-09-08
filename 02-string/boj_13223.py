# default: current < future but after one day: current > future
# -> ⓐ 24:00:00 - current || ⓑ future
# 시간 빌림 계산 (current보다 future의 hour은 크지만 min, sec은 작을 때)
# -> sec이 작으면 ⓐ min-1 ⓑ future_sec + 60 ⓒ 계산진행 / min이 작으면 ⓐ hour-1 ⓑ future_min+ 60 ⓒ 계산진행
# idx 0[hour, 시] 1[minute, 분], 2[second, 초]
def calculate_time(minuend, subtrahend):
    # minuend - subtrahend
    result = [0] * 3

    # second 먼저 계산
    result[2] = minuend[2] - subtrahend[2]
    if minuend[2] < subtrahend[2]:
        minuend[1] -= 1
        result[2] += 60

    # minute 계산
    result[1] = minuend[1] - subtrahend[1]
    if minuend[1] < subtrahend[1]:
        minuend[0] -= 1
        result[1] += 60

    result[0] = minuend[0] - subtrahend[0]

    return result


current = list(map(int, input().split(':')))
future = list(map(int, input().split(':')))
output = [0, 0, 0]

# print(future, current)
# print(calculate_time(future, current))

# 하루가 지났을 경우
# 문제조건: 로봇팔이 소금을 투하할때까지 필요한 시간을 hh:mm:ss -> 이 시간은 1초보다 크거나 같고, 24시간보다 작거나 같다.
if future[0] < current[0] or (future[0] == current[0] and future[1] <= current[1]):
    noon = [24, 0, 0]

    yesterday = calculate_time(noon, current)

    for i in range(3):
        output[i] = yesterday[i] + future[i]

    # 계산 상 sec, min이 60을 넘었을 때 => 언제 이런 케이스가 발생할까
    # 60과 같을때도 올림 해주어야 함
    if output[2] >= 60:
        output[1] += 1
        output[2] -= 60
    if output[1] >= 60:
        output[0] += 1
        output[1] -= 60
else:
    output = calculate_time(future, current)

print(':'.join(list(map(lambda x: str(x).zfill(2), output))))
