from Strategy.i_datasearch import DataResearch
import time

class IDAStar(DataResearch):
    def __init__(self, problem):
        super().__init__(problem)
        self.path = []

    def problem_analyze(self):
        start_time = time.time()
        bound = self.problem.heuristic_function(self.problem.i_state)
        self.path = [self.problem.i_state]

        while True:
            t = self.search(0, bound)
            if t == "FOUND":
                self.total_time = time.time() - start_time
                return list(self.path)
            if t == float('inf'):
                self.total_time = time.time() - start_time
                return None  
            bound = t

    def search(self, g, bound):
        node = self.path[-1]
        f = g + self.problem.heuristic_function(node)
        if f > bound:
            return f
        if self.problem.is_g_state(node):
            return "FOUND"
        min_bound = float('inf')
        for succ in self.problem.get_next_steps(node):
            if succ not in self.path: 
                self.path.append(succ)
                self.visited_nodes += 1
                t = self.search(g + 1, bound)
                if t == "FOUND":
                    return "FOUND"
                if t < min_bound:
                    min_bound = t
                self.path.pop()
        return min_bound
