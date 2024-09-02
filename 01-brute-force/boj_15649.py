class BOJ15649:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.selected_array = [0] * self.m

    def generate_sequence(self, idx):
        if idx == self.m:
            print(" ".join(map(str, self.selected_array)))
            return
        else:
            for i in range(1, self.n+1):  # At the same level
                if i not in self.selected_array:  # Violations of the duplication condition are already filtered by this code
                    self.selected_array[idx] = i
                    self.generate_sequence(idx+1)  # Level Expansion
                    self.selected_array[idx] = 0
                    # When level expansion ends (no deeper recursion), reset the state for the next sibling level
                    # Without this reset, the final cases might not be generated correctly.
                    # 이후 for로 인해 상위 레벨 상 다음 형제로 이동


resolve = BOJ15649()
resolve.generate_sequence(0)
