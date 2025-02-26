import networkx as nx
import time
import matplotlib.pyplot as plt
import numpy as np
from problema1 import greedy_repair_algorithm
from problema1_brute_force import brute_force_repair
from problema1_brute_force2 import brute_force_solution 

case_numbers = []
greedy_priorities = []
brute_force_priorities = []
brute_force2_priorities = []
greedy_times = []
brute_force_times = []
brute_force2_times = []
greedy_costs = []
brute_force_costs = []
brute_force2_costs = []

def total_cost(edges, G):

    return sum(G[u][v]['cost'] for u, v in edges)

def run_test_case(case_number, G, s, D, P, B):

    print(f"\n=== Caso {case_number} ===")

    # Greedy
    start_time = time.time()
    greedy_result = greedy_repair_algorithm(G, s, D, P, B)
    greedy_time = time.time() - start_time
    greedy_priority = greedy_result[2]
    greedy_cost = total_cost(greedy_result[0], G)
    print(f"Greedy: {greedy_result} (Tiempo: {greedy_time:.6f}s, Prioridad: {greedy_priority}, Costo: {greedy_cost})")

    # Fuerza Bruta
    start_time = time.time()
    brute_force_result = brute_force_repair(G, s, D, P, B)
    brute_force_time = time.time() - start_time
    brute_force_priority = brute_force_result[2]
    brute_force_cost = total_cost(brute_force_result[0], G)
    print(f"Fuerza Bruta: {brute_force_result} (Tiempo: {brute_force_time:.6f}s, Prioridad: {brute_force_priority}, Costo: {brute_force_cost})")

    # Fuerza Bruta 2
    start_time = time.time()
    brute_force2_result = brute_force_solution(G, s, D, P, B)
    brute_force2_time = time.time() - start_time
    brute_force2_priority =brute_force2_result[2]
    brute_force2_cost = total_cost(brute_force2_result[0], G)
    print(f"Fuerza Bruta 2: {brute_force2_result} (Tiempo: {brute_force2_time:.6f}s, Prioridad: {brute_force2_priority}, Costo: {brute_force2_cost})")


    # Almacenar datos para graficar
    case_numbers.append(case_number)
    greedy_priorities.append(greedy_priority)
    brute_force_priorities.append(brute_force_priority)
    brute_force2_priorities.append(brute_force2_priority)
    greedy_times.append(greedy_time)
    brute_force_times.append(brute_force_time)
    brute_force2_times.append(brute_force2_time)
    greedy_costs.append(greedy_cost)
    brute_force_costs.append(brute_force_cost)
    brute_force2_costs.append(brute_force2_cost)



def plot_results():

    greedy_times_ms = [t * 1000 for t in greedy_times]
    brute_force_times_ms = [t * 1000 for t in brute_force_times]
    brute_force2_times_ms = [t * 1000 for t in brute_force2_times]

    plt.figure(figsize=(15, 5))

    # Gráfico de prioridad obtenida
    plt.subplot(1, 3, 1)
    plt.plot(case_numbers, greedy_priorities, marker='o', label="Greedy", linestyle="--")
    plt.plot(case_numbers, brute_force_priorities, marker='s', label="Fuerza Bruta", linestyle="-")
    plt.plot(case_numbers, brute_force2_priorities, marker='^', label="Fuerza Bruta 2", linestyle=":")
    plt.xlabel("Casos de prueba")
    plt.ylabel("Prioridad total obtenida")
    plt.title("Comparación de Prioridad Obtenida")
    plt.legend()
    plt.grid(True)

    # Gráfico de tiempo de ejecución en milisegundos
    plt.subplot(1, 3, 2)
    plt.plot(case_numbers, greedy_times_ms, marker='o', label="Greedy", linestyle="--")
    plt.plot(case_numbers, brute_force_times_ms, marker='s', label="Fuerza Bruta", linestyle="-")
    plt.plot(case_numbers, brute_force2_times_ms, marker='^', label="Fuerza Bruta 2", linestyle=":")
    plt.xlabel("Casos de prueba")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.title("Comparación de Tiempos de Ejecución")
    plt.legend()
    plt.grid(True)

    # Gráfico de costo total utilizado
    plt.subplot(1, 3, 3)
    plt.plot(case_numbers, greedy_costs, marker='o', label="Greedy", linestyle="--")
    plt.plot(case_numbers, brute_force_costs, marker='s', label="Fuerza Bruta", linestyle="-")
    plt.plot(case_numbers, brute_force2_costs, marker='^', label="Fuerza Bruta 2", linestyle=":")
    plt.xlabel("Casos de prueba")
    plt.ylabel("Costo total de reparación")
    plt.title("Comparación de Costos de Reparación")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    
    plt.savefig("./proyecto/subproblema1/comparacion_algoritmos.png", dpi=300)
    print("Imagen guardada como 'comparacion_algoritmos.png'")
    
    plt.show()


def test_cases():

    cases = [
        # Caso 1
        (1, nx.Graph([('s', 'a', {'cost': 2}), ('a', 'c', {'cost': 3}), ('s', 'b', {'cost': 2})]), 's', {'c', 'b'}, {'c': 5, 'b': 8}, 4),
        # Caso 2
        (2, nx.Graph([('s', 'a', {'cost': 2}), ('a', 'b', {'cost': 3}), ('b', 'c', {'cost': 3}), ('s', 'd', {'cost': 3})]), 's', {'c', 'd'}, {'c': 10, 'd': 15}, 5),
        # Caso 3
        (3, nx.Graph([('s', 'a', {'cost': 2}), ('a', 'b', {'cost': 3}), ('b', 'c', {'cost': 4}), ('s', 'd', {'cost': 4}), ('c', 'e', {'cost': 2}), ('d', 'e', {'cost': 2})]), 's', {'c', 'd', 'e'}, {'c': 12, 'd': 20, 'e': 8}, 6),
        # Caso 4
        (4, nx.Graph([('s', 'a', {'cost': 2}), ('a', 'b', {'cost': 3}), ('b', 'c', {'cost': 5}), ('s', 'd', {'cost': 3}), ('d', 'e', {'cost': 1}), ('e', 'f', {'cost': 2}), ('c', 'f', {'cost': 1}), ('d', 'g', {'cost': 4})]), 's', {'c', 'd', 'f', 'g'}, {'c': 15, 'd': 8, 'f': 10, 'g': 20}, 7),
            # Caso 5:
        (5, nx.Graph([('s', 'a', {'cost': 2}), ('a', 'b', {'cost': 2}), ('s', 'c', {'cost': 4}), ('c', 'd', {'cost': 1}), ('d', 'e', {'cost': 1}), ('b', 'e', {'cost': 4})]), 's', {'b', 'd', 'e'}, {'b': 5, 'd': 10, 'e': 15}, 6),
        # Caso 6:
        (6, nx.Graph([('s', 'a', {'cost': 1}), ('a', 'b', {'cost': 2}), ('s', 'c', {'cost': 3}), ('c', 'd', {'cost': 3}), ('b', 'd', {'cost': 1}), ('d', 'e', {'cost': 2}), ('c', 'e', {'cost': 5})]), 's', {'b', 'd', 'e'}, {'b': 2, 'd': 12, 'e': 8}, 7)
    ]

    for case in cases:
        run_test_case(*case)

    plot_results()

if __name__ == "__main__":
    test_cases()
