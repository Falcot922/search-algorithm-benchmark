from i_problems import Problem

class RCube2x2(Problem):
    """
    Rubik's Cube 2x2 implementation.
    State format: (corners_perm, corners_ori)
    corners_perm: tuple of length 8 (0..7)
    corners_ori: tuple of length 8 (0,1,2)
    """

    MOVES = ['U','U\'','U2','D','D\'','D2','L','L\'','L2','R','R\'','R2','F','F\'','F2','B','B\'','B2']

    MOVE_TABLES = {
        'U':  {'cp': (3,0,1,2,4,5,6,7), 'co': (0,0,0,0,0,0,0,0)},
        'U\'':{'cp': (1,2,3,0,4,5,6,7), 'co': (0,0,0,0,0,0,0,0)},
        'U2': {'cp': (2,3,0,1,4,5,6,7), 'co': (0,0,0,0,0,0,0,0)},
        # D
        'D':  {'cp': (0,1,2,3,5,6,7,4), 'co': (0,0,0,0,0,0,0,0)},
        'D\'':{'cp': (0,1,2,3,7,4,5,6), 'co': (0,0,0,0,0,0,0,0)},
        'D2': {'cp': (0,1,2,3,6,7,4,5), 'co': (0,0,0,0,0,0,0,0)},
        # L
        'L':  {'cp': (4,1,2,0,7,5,6,3), 'co': (1,0,0,2,2,0,0,1)},
        'L\'':{'cp': (3,1,2,7,0,5,6,4), 'co': (2,0,0,1,1,0,0,2)},
        'L2': {'cp': (7,1,2,4,3,5,6,0), 'co': (0,0,0,0,0,0,0,0)},
        # R
        'R':  {'cp': (0,2,6,3,4,1,5,7), 'co': (0,1,2,0,0,2,1,0)},
        'R\'':{'cp': (0,5,1,3,4,6,2,7), 'co': (0,2,1,0,0,1,2,0)},
        'R2': {'cp': (0,6,5,3,4,2,1,7), 'co': (0,0,0,0,0,0,0,0)},
        # F
        'F':  {'cp': (0,1,3,7,4,5,2,6), 'co': (0,0,1,2,0,0,2,1)},
        'F\'':{'cp': (0,1,6,2,4,5,7,3), 'co': (0,0,2,1,0,0,1,2)},
        'F2': {'cp': (0,1,7,6,4,5,3,2), 'co': (0,0,0,0,0,0,0,0)},
        # B
        'B':  {'cp': (5,4,2,3,1,0,6,7), 'co': (2,1,0,0,1,2,0,0)},
        'B\'':{'cp': (5,4,2,3,1,0,6,7), 'co': (1,2,0,0,2,1,0,0)},
        'B2': {'cp': (1,0,2,3,5,4,6,7), 'co': (0,0,0,0,0,0,0,0)},
    }

    def __init__(self, i_state=None, g_state=None):
        if i_state is None:
            i_state = (tuple(range(8)), tuple([0]*8))
        if g_state is None:
            g_state = (tuple(range(8)), tuple([0]*8))
        super().__init__(i_state, g_state)

    def get_next_steps(self, state):
        next_states = []
        for move in self.MOVES:
            table = self.MOVE_TABLES.get(move)
            if table:
                next_states.append(self.apply_move(state, table))
        return next_states

    def is_g_state(self, state):
        return state == self.g_state

    def heuristic_function(self, state):
        cp, co = state
        g_cp, g_co = self.g_state
        h = sum(1 for i in range(8) if cp[i] != g_cp[i]) + sum(1 for i in range(8) if co[i] != g_co[i])
        return h

    def apply_move(self, state, table):
        cp, co = state
        new_cp = tuple(cp[i] for i in table['cp'])
        new_co = tuple((co[i] + table['co'][i]) % 3 for i in range(8))
        return (new_cp, new_co)
