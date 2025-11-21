from Strategy.i_datasearch import DataResearch
from Strategy.utils.pile import Pile
import time

class IDA(DataResearch):

    def problem_analyze(self):
        start_time = time.time()
        limit_depth = 0

        while True:
            parent = {self.problem.i_state: None}
            pile = Pile()
            pile.empiler((self.problem.i_state, 0))
            visited = set()

            while not pile.est_vide():
                current_state, depth = pile.depiler()
                self.visited_nodes += 1

                if current_state == self.problem.g_state:
                    self.total_time = time.time() - start_time
                    return self.pathing(parent, current_state)

                if depth == limit_depth:
                    continue

                visited.add(current_state)

                for nxt in self.problem.get_next_steps(current_state):
                    if nxt not in visited:
                        parent[nxt] = current_state
                        pile.empiler((nxt, depth + 1))

            limit_depth += 1

    def pathing(self, parent, state):
        res = []
        while state:
            res.append(state)
            state = parent[state]
        res.reverse()
        return res
