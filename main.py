import time
import tracemalloc
from Strategy.BFS import BFS
from Strategy.DFS import DFS
from Strategy.AStar import AStar
from Problems.taquin import Taquin
from Problems.queen import NQueens
from Problems.hanoi import Hanoi


def run_algorithm(algo_class, problem):
    print(f"\n=== {algo_class.__name__} ===")

    algo = algo_class(problem)

    tracemalloc.start()
    start_time = time.time()

    solution = algo.problem_analyze()

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    exec_time = end_time - start_time
    memory_kb = peak / 1024

    print(f"Temps d'exécution : {exec_time:.4f} sec")
    print(f"Mémoire max : {memory_kb:.2f} Ko")
    print(f"Noeuds visités : {algo.visited_nodes}")
    print(f"Taille solution : {len(solution) if solution else 'Aucune solution'}")

    return {
        "algorithm": algo_class.__name__,
        "time": exec_time,
        "memory_kb": memory_kb,
        "nodes": algo.visited_nodes,
        "solution_length": len(solution) if solution else None,
    }


def main():

    initial = (1, 2, 3,
               4, 5, 6,
               7, 0, 8)

    goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)

    problems = [Taquin(i_state=initial, g_state=goal), NQueens(size=10), Hanoi(n_disks=4)]

    algorithms = [BFS, DFS, AStar]

    results = []
    
    for problem in problems:
        for algo in algorithms:
            result = run_algorithm(algo, problem)
            results.append(result)

    print("\n\n===== RÉSUMÉ DES RÉSULTATS =====\n")
    for r in results:
        print(f"[{r['algorithm']}]  temps={r['time']:.4f}s  mémoire={r['memory_kb']:.2f} Ko  "
              f"nœuds={r['nodes']}  solution={r['solution_length']}")


if __name__ == "__main__":
    main()
