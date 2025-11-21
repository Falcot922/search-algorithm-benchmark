import time
import tracemalloc
import json
import os
import datetime

from Strategy.BFS import BFS
from Strategy.DFS import DFS
from Strategy.AStar import AStar
from Strategy.IDA import IDA
from Strategy.IDA_star import IDAStar
from Problems.taquin import Taquin
from Problems.queen import NQueens
from Problems.hanoi import Hanoi


def run_algorithm(algo_class, problem):
    algo = algo_class(problem)

    tracemalloc.start()
    start_time = time.time()

    solution = algo.problem_analyze()

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "algorithm": algo_class.__name__,
        "time_ms": (end_time - start_time) * 1000,
        "memory_kb": peak / 1024,
        "nodes_explored": algo.visited_nodes,
        "distance": len(solution) if solution else None
    }


def main():
    algo_per_prob = {
        "Taquin": [AStar, IDAStar, DFS, BFS],
        "Hanoi": [DFS, BFS, AStar, IDA],
        "NQueens": [BFS, DFS]
    }

    all_results = []

    for problem_name, algos in algo_per_prob.items():
        print(problem_name)

        if problem_name == "Taquin":
            dim = int(input("Dimension du Taquin : "))
            n_tests = int(input(f"Nombre de tests pour {problem_name} : "))
        else:
            taille = int(input("Taille du problème : "))
            n_tests = int(input(f"Nombre de tests pour {problem_name} : "))
            dim = None

        for test_index in range(n_tests):

            if problem_name == "Taquin":
                problem = Taquin.generate(dim)
                test_name = f"Taquin-{dim}x{dim}"
            elif problem_name == "Hanoi":
                problem = Hanoi(taille)
                test_name = f"Hanoi"
            elif problem_name == "NQueens":
                problem = NQueens(taille)
                test_name = f"NQueens-8"

            run_results = []

            for algo in algos:
                result = run_algorithm(algo, problem)
                result["test_name"] = test_name
                run_results.append(result)

            all_results.append({
                "problem": problem_name,
                "results": run_results
            })

    json_filename = f"{datetime.date.today()}_testResults.json"
    dir_path = os.path.join(os.getcwd(), "result")
    os.makedirs(dir_path, exist_ok=True)
    json_output_path = os.path.join(dir_path, json_filename)

    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

    print(f"\nRésultats écrits dans : {json_output_path}")

if __name__ == "__main__":
    main()