from Problems.i_problems import Problem

class Hanoi(Problem):
    def __init__(self, n_disks):
        initial_state = (tuple(range(n_disks, 0, -1)), (), ())
        goal_state = ((), (), tuple(range(n_disks, 0, -1)))
        super().__init__(initial_state, goal_state)
        self.n = n_disks

    def is_g_state(self, state):
        return state == self.g_state

    def get_next_steps(self, state):
        next_states = []
        for start in range(3):
            if len(state[start]) == 0:
                continue  
            
            disk_to_move = state[start][-1]
            
            for end in range(3):
                if start == end:
                    continue

                if (len(state[end]) == 0 or state[end][-1] > disk_to_move):
                    new_state = self.move_disk(state, start, end)
                    next_states.append(new_state)
        return next_states
    
    def generate(self, n):
        return Hanoi(n)

    def move_disk(self, state, start, end):
        state = list(map(list, state))

        disk = state[start].pop() 
        state[end].append(disk)    

        return (tuple(state[0]), tuple(state[1]), tuple(state[2]))

    def heuristic_function(self, state):
        goal_tower = 2
        _, _, goal = self.g_state

        h = 0
        for i in range(self.n):
            expected_disk = i + 1
            if expected_disk not in state[goal_tower]:
                h += 1
        return h
