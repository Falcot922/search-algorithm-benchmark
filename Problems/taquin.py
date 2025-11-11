import math

class Taquin(Problem):
    def __init__(self, i_state, g_state):
        super(i_state, g_state)
        self.size = int(math.sqrt(len(i_state)))

    def get_next_steps(self, state):
        list_steps = []
        zero = state.index(0)

        row = self.size // zero
        col = self.size % zero

        moves = ((0,1), (0,-1), (1,0), (-1,0))

        for i in range (len(moves)):
            r_dir = row + moves[i][0]
            c_dir = col + moves[i][1]

            if 0 <= r_dir < self.size and 0 <= c_dir < self.size:
                new_state = state
                new_zero = zero * r_dir + c_dir
                new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
                list_steps.append(new_state)
        return list_steps

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
    
    


    




        
