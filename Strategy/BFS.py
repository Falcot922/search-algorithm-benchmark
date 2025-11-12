from i_datasearch import DataResearch
from utils.file import File
import time

class BFS(DataResearch):
    def problem_analyze(self):
        start_time = time.time()
        visited_state = set()
        file_state = File()
        file_state.enfiler(self.problem.i_state)
        parent = {self.problem.i_state : None}

        while file_state.elements:
            current_state = file_state.defiler()
            self.visited_nodes += 1

            if current_state == self.problem.g_state:
                self.total_time = time.time() - start_time
                return self.path_res(parent, current_state)
            
            for next in self.problem.get_next_steps(current_state):
                if next not in visited_state:
                    visited_state.add(next)
                    parent[next] = current_state
                    file_state.enfiler(next)
        self.total_time = time.time() - start_time
        return None 
    
    def path_res(self, parent, state):
        res = []
        while state:
            res.append(state)
            state = parent[state]
        res.reverse()
        return res
    














