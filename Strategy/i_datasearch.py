from abc import ABC, abstractmethod

class DataResearch(ABC):
    def __init__(self, problem):
        self.problem = problem
        self.visited_nodes = 0
        self.total_time = 0

    @abstractmethod
    def problem_analyze(self):
        pass