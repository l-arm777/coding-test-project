n, m = map(int, input().split())

selected_array = []


def dfs():
    if len(selected_array) == m:
        print(' '.join(map(str, selected_array)))
        return
    else:
        for i in range(1, n+1):
            selected_array.append(i)
            dfs()
            selected_array.pop()


dfs()
# 한 번에 출력 하려 하면 타임 오버될 수 있다. 완료된 수열은 바로 바로 출력 하는 게 차라리 나을 수 있다
