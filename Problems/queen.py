from Problems.i_problems import Problem

class NQueens(Problem):
    def __init__(self, size=8):
        self.size = size
        super().__init__(i_state=())

    def get_next_steps(self, state):
        next_states = []
        row = len(state)  
        if row >= self.size:
            return next_states 

        for col in range(self.size):
            if self.is_safe(state, row, col):
                next_states.append(state + (col,))
        return next_states

    def is_g_state(self, state):
        return len(state) == self.size

    def heuristic_function(self, state):
        conflicts = 0
        for i, c1 in enumerate(state):
            for j, c2 in enumerate(state):
                if i < j:
                    if c1 == c2 or abs(c1 - c2) == abs(i - j):
                        conflicts += 1
        return conflicts

    def is_safe(self, state, row, col):
        for r, c in enumerate(state):
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True
