import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

def create_markov_network():
    g = nx.Graph()
    g.add_edges_from([
        ('A1', 'A2'),
        ('A1', 'A3'),
        ('A2', 'A4'),
        ('A2', 'A5'),
        ('A3', 'A4'),
        ('A4', 'A5')
    ])
    return g

def visualize_and_find_cliques(g):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=15, edge_color='gray')
    plt.title("Markov Network Visualization")
    plt.show()
    
    cliques = list(nx.find_cliques(g))
    return cliques

def energy_for_clique(clique, t_values):
    return np.exp(sum(t_i * A_i for t_i, A_i in zip(t_values, clique)))

def compute_joint_probability(cliques, t_values_dict):
    all_variables = ['A1', 'A2', 'A3', 'A4', 'A5']
    all_combinations = list(product([0, 1], repeat=len(all_variables)))
    
    probabilities = {}
    for combination in all_combinations:
        prob = 1.0
        for clique in cliques:
            clique_values = [combination[all_variables.index(var)] for var in clique]
            t_values = [t_values_dict[var] for var in clique]
            prob *= energy_for_clique(clique_values, t_values)
        probabilities[combination] = prob
    
    total_sum = sum(probabilities.values())
    normalized_probabilities = {k: v / total_sum for k, v in probabilities.items()}
    
    max_prob = max(normalized_probabilities, key=normalized_probabilities.get)
    
    return normalized_probabilities, max_prob

def main():
    g = create_markov_network()
    cliques = visualize_and_find_cliques(g)
    
    t_values_dict = {
        'A1': 0.5,
        'A2': -0.3,
        'A3': 0.8,
        'A4': -0.2,
        'A5': 0.4
    }
    
    probabilities, max_prob_state = compute_joint_probability(cliques, t_values_dict)

    print("Probabilitățile normalizate:", probabilities)
    print("Starea cu probabilitate maximă:", max_prob_state)

main()
