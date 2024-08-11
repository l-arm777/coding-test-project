class BOJ15651:
    def __init__(self):
        self.n, self.m = map(int, input().split())  # 사용자 입력 받기 (1 ≤ M ≤ N ≤ 7)
        self.selected_array = [0] * self.m          # 새로 만들어 진 수열
        self.result = ""                            # 수열 모음

    def generate_sequence(self, idx):
        # 수열이 완성 되었음
        if idx == self.m:
            self.result += " ".join(map(str, self.selected_array)) + "\n"
        # 수열이 완성 되지 않아 새 숫자를 채워 넣어 줘야 함
        else:
            for i in range(1, self.n + 1):
                self.selected_array[idx] = i
                self.generate_sequence(idx+1)


resolve = BOJ15651()
resolve.generate_sequence(0)
print(resolve.result.rstrip())
