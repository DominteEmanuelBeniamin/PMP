from hmmlearn import hmm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Dimensiunea gridului
dimensiune_grid = (10, 10)

# Lista de culori predefinite
culori = [
    "red", "blue", "green", "yellow", 
    "purple", "orange", "pink", "cyan", 
    "brown", "lime"
]

# Citirea gridului
df = pd.read_csv('grid_culori.csv', header=None)
grid_culori = df.values.reshape((10, 10))

# Generarea secvenței de culori observate
# This needs to be specified or generated
observatii = ['red', 'blue', 'green', 'yellow', 'purple']

# Mapare culori -> indecși
culoare_to_idx = {culoare: idx for idx, culoare in enumerate(culori)}
idx_to_culoare = {idx: culoare for culoare, idx in culoare_to_idx.items()}

# Transformăm secvența de observații în indecși
observatii_idx = [culoare_to_idx[c] for c in observatii]

# Definim stările ascunse ca fiind toate pozițiile din grid (100 de stări)
numar_stari = dimensiune_grid[0] * dimensiune_grid[1]
stari_ascunse = [(i, j) for i in range(dimensiune_grid[0]) for j in range(dimensiune_grid[1])]
stare_to_idx = {stare: idx for idx, stare in enumerate(stari_ascunse)}
idx_to_stare = {idx: stare for stare, idx in stare_to_idx.items()}

# Matrice de tranziție
transitions = np.zeros((numar_stari, numar_stari))
for i, j in stari_ascunse:
    vecini = [
        (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)  # sus, jos, stânga, dreapta
    ]
    for vecin in vecini:
        if 0 <= vecin[0] < 10 and 0 <= vecin[1] < 10:
            transitions[stare_to_idx[(i, j)], stare_to_idx[vecin]] = 1 / len(vecini)

# Normalize the transitions to ensure they sum to 1
transitions /= transitions.sum(axis=1, keepdims=True)

# Matrice de emisie
emissions = np.zeros((numar_stari, len(culori)))
for i in range(10):
    for j in range(10):
        idx = stare_to_idx[(i, j)]
        color_idx = culoare_to_idx[grid_culori[i, j]]
        emissions[idx, color_idx] = 1  # Perfect observation model

# Initialize the model
model = hmm.MultinomialHMM(n_components=numar_stari)
model.startprob_ = np.ones(numar_stari) / numar_stari  # Uniform start probability
model.transmat_ = transitions
model.emissionprob_ = emissions

# Run the Viterbi algorithm
logprob, states = model.decode(np.array([observatii_idx]).T, algorithm="viterbi")
path = [idx_to_stare[state] for state in states]

# Visualization
fig, ax = plt.subplots(figsize=(8, 8))
for i in range(dimensiune_grid[0]):
    for j in range(dimensiune_grid[1]):
        color = grid_culori[i, j]
        ax.add_patch(plt.Rectangle((j, dimensiune_grid[0] - i - 1), 1, 1, color=color))
        ax.text(j + 0.5, dimensiune_grid[0] - i - 0.5, color, 
                color="white", ha="center", va="center", fontsize=8, fontweight="bold")

# Highlight the resulting path
for idx, (i, j) in enumerate(path):
    ax.add_patch(plt.Circle((j + 0.5, dimensiune_grid[0] - i - 0.5), 0.3, color="black", alpha=0.7))

ax.set_xlim(0, dimensiune_grid[1])
ax.set_ylim(0, dimensiune_grid[0])
ax.set_xticks(range(dimensiune_grid[1]))
ax.set_yticks(range(dimensiune_grid[0]))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(visible=True, color="black", linewidth=0.5)
ax.set_aspect("equal")
plt.title("Drumul rezultat al stărilor ascunse", fontsize=14)
plt.show()