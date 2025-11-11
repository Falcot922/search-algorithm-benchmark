class File:
    def __init__(self):
        self.elements

    def est_vide(self):
        return len(self.elements) == 0

    def enfiler(self, item):
        self.elements.append(item)

    def defiler(self):
        if self.est_vide():
            return
        return self.elements.pop(0)

    def taille(self):
        return len(self.elements)




class BFS(DataResearch):
    def problem_analyze(self):
        start_time = time.time()
        file_state = self.problem.i_state.File
        list_visited_state = set()
        parent = {self.problem.i_state : None}

        while file_state:
            state = file_state.defiler()
            self.visited_nodes += 1

            if self.problem.is_g_state(state):
                self.total_time = time.time() - start_time
                return self.pathing(parent, state)
            
            for next_state in self.problem.get_next_steps(state):
                list_visited_state.add(next_state)
                parent[next_state] = state 
                file_state.enfiler(next_state)
        self.total_time = time.time() - start_time
        return None 
    
    def pathing(self, parent, state):
        res = []
        while state:
            res.append(state)
            state = parent[state]
        res.reverse()
        return res 






