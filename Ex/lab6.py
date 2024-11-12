import pymc as pm
import numpy as np
import matplotlib.pyplot as plt
import arviz as az

data = np.array([56, 60, 58, 55, 57, 59, 61, 56, 58, 60])

with pm.Model() as model:
    mu = pm.Normal('mu', mu=np.mean(data), sigma=10)         
    sigma = pm.HalfNormal('sigma', sigma=10)                 
    y_obs = pm.Normal('y_obs', mu=mu, sigma=sigma, observed=data) 

    trace = pm.sample(2000, tune=1000, target_accept=0.9, return_inferencedata=True)

hdi_mu = pm.hdi(trace.posterior['mu'], hdi_prob=0.95)
hdi_sigma = pm.hdi(trace.posterior['sigma'], hdi_prob=0.95)

mu_lower, mu_upper = hdi_mu['mu'].values
sigma_lower, sigma_upper = hdi_sigma['sigma'].values

print(f"95% HDI for mu: [{mu_lower:.2f}, {mu_upper:.2f}]")
print(f"95% HDI for sigma: [{sigma_lower:.2f}, {sigma_upper:.2f}]")

az.plot_posterior(trace, var_names=["mu", "sigma"], hdi_prob=0.95)
plt.show()
