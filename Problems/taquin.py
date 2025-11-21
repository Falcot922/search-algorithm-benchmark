import math
from random import shuffle
from Problems.i_problems import Problem

class Taquin(Problem):
    def __init__(self, size, i_state, g_state):
        assert(int(math.sqrt(len(i_state))) == size)
        super().__init__(size, i_state, g_state)

    def get_next_steps(self, state):
        list_steps = []
        zero = state.index(0)

        row = zero // self.size
        col = zero % self.size

        moves = [(0,1), (0,-1), (1,0), (-1,0)]

        for dr, dc in moves:
            r = row + dr
            c = col + dc

            if 0 <= r < self.size and 0 <= c < self.size:
                new_state = list(state) 
                new_zero = r * self.size + c
                new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
                list_steps.append(tuple(new_state))

        return list_steps

    @staticmethod
    def is_solvable(state, size):
        ind = 0
        lst = [x for x in state if x != 0]

        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] > lst[j]:
                    ind += 1

        if size % 2 == 1:
            return  ind % 2 == 0

        row_zero = state.index(0) // size
        row_from_bottom = size - row_zero

        if row_from_bottom % 2 == 0:
            return  ind % 2 == 1
        else:
            return  ind % 2 == 0
        
    @staticmethod
    def generate(size):
        n = size * size
        g_lst = list(range(1, n)) + [0]
        while True:
            lst = list(range(n))
            shuffle(lst)
            if Taquin.is_solvable(lst, size):
                return Taquin(size, tuple(lst), tuple(g_lst))

    def is_g_state(self, state):
        return state == self.g_state
    
    def heuristic_function(self, state):
        dist = 0
        for i in range (len(state)):
            val = state[i]
            if val != 0:
                current_row = i // self.size
                current_col = i % self.size 
                g_row = self.g_state.index(val) // self.size 
                g_col = self.g_state.index(val) % self.size

                dist += abs(current_row - g_row) + abs(current_col - g_col)
        return dist
    
    


    




        
