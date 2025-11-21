from Strategy.i_datasearch import DataResearch
from Strategy.utils.pile import Pile
import time

class DFS(DataResearch):
    def problem_analyze(self):
        start_time = time.time()
        parent = {self.problem.i_state : None}
        pile_state = Pile()
        pile_state.empiler(self.problem.i_state)
        visited = set()

        while not pile_state.est_vide():
            current_state = pile_state.depiler()
            self.visited_nodes += 1
            
            if current_state in visited:
                continue
            visited.add(current_state)

            if current_state == self.problem.g_state:
                self.total_time = time.time() - start_time
                return self.pathing(parent, current_state)
            
            for nxt in self.problem.get_next_steps(current_state):
                if nxt not in visited:
                    parent[nxt] = current_state
                    pile_state.empiler(nxt)

        self.total_time = time.time() - start_time
        return None 
    
    def pathing(self, parent, state):
        res = []
        while state:
            res.append(state)
            state = parent[state]
        res.reverse()
        return res






