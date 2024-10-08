import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import arviz as az

lambdas = [3, 6, 4]
probabilities = [3/13, 6/13, 4/13]

np.random.seed(0)  
samples = []
for _ in range(10000):
    frizer = np.random.choice([0, 1, 2], p=probabilities)
    sample = np.random.exponential(scale=1/lambdas[frizer])
    samples.append(sample)

mean_X = np.mean(samples)
std_X = np.std(samples)

plt.figure(figsize=(10, 6))
az.plot_kde(np.array(samples), label="Distribuția aproximativă a lui X")
plt.xlabel("Timpul de servire")
plt.ylabel("Densitate")
plt.title(f"Densitatea distribuției timpului de servire pentru un client\nMedia: {mean_X:.4f}, Deviația Standard: {std_X:.4f}")
plt.legend()
plt.grid(True)
plt.show()

print(f"Media estimată: {mean_X:.4f}")
print(f"Deviația standard estimată: {std_X:.4f}")
