from abc import ABC, abstractmethod

class Problem(ABC):
    def __init__(self, size, i_state, g_state=None):
        self.size = size
        self.i_state = i_state
        self.g_state = g_state
    
    @abstractmethod
    def get_next_steps(self, state):
        """Se charge de retourner l'ensemble des états suivants possibles en partant de state"""
        pass

    @abstractmethod
    def is_g_state(self, state):
        """Se charge de retourner si un état correspond au but ou non"""
        pass 

    @abstractmethod
    def generate(self, size):
        """Se charge de générer un problème"""
        pass


    def heuristic_function(self, state):
        """Utiliser pour les algos nécessitant une fonction heuristique"""
        return 0
    
