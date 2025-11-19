from Strategy.i_datasearch import DataResearch
import heapq
import time

class AStar(DataResearch):
    def problem_analyze(self):
        start_time = time.time()
        visited = set()
        parent = {self.problem.i_state: None}
        g_score = {self.problem.i_state: 0}

        open_list = []
        heapq.heappush(open_list, (self.problem.heuristic_function(self.problem.i_state), self.problem.i_state))

        while open_list:
            f, current_state = heapq.heappop(open_list)
            self.visited_nodes += 1

            if self.problem.is_g_state(current_state):
                self.total_time = time.time() - start_time
                return self.pathing(parent, current_state)

            visited.add(current_state)

            for next_state in self.problem.get_next_steps(current_state):
                tentative_g = g_score[current_state] + 1
                if next_state in visited and tentative_g >= g_score.get(next_state, float('inf')):
                    continue

                if tentative_g < g_score.get(next_state, float('inf')) or next_state not in [s for _, s in open_list]:
                    parent[next_state] = current_state
                    g_score[next_state] = tentative_g
                    f_score = tentative_g + self.problem.heuristic_function(next_state)
                    heapq.heappush(open_list, (f_score, next_state))

        self.total_time = time.time() - start_time
        return None

    def pathing(self, parent, state):
        path = []
        while state:
            path.append(state)
            state = parent[state]
        path.reverse()
        return path
