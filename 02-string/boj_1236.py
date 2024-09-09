N, M = list(map(int, input().split()))  # N 가로, 줄 / M 세로, 열
row = [0] * N
col = [0] * M
# col 세로, 열 / row 가로, 줄
state = []

for line in range(N):
    state.append(list(input()))

# print(state)

for i in range(N):
    for j in range(M):
        if state[i][j] == 'X':
            row[i] = 1
            col[j] = 1

# print(col, row)
print(max(col.count(0), row.count(0)))
