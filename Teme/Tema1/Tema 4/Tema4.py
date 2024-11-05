import numpy as np
from scipy.stats import poisson, expon

lambda_customers = 20
mean_order_time = 2
alpha = 5

num_customers = poisson.rvs(lambda_customers)
order_times = expon.rvs(scale=mean_order_time, size=num_customers)
cook_times = expon.rvs(scale=alpha, size=num_customers)

print(f"Numarul de clienti intr-o ora: {num_customers}")
print(f"Timpuri de plasare a comenzilor (minute): {[round(time, 2) for time in order_times]}")
print(f"Timpuri de gatire pentru fiecare comanda (minute): {[round(time, 2) for time in cook_times]}")






import numpy as np
from scipy.stats import poisson, expon

lambda_customers = 20          
average_order_time = 2        
max_wait_time = 15             
probability_threshold = 0.95   

def simulate_service(alpha, num_simulations=10000):
    successful_simulations = 0

    for _ in range(num_simulations):
        num_customers = np.random.poisson(lambda_customers)
        if num_customers == 0:
            successful_simulations += 1
            continue
        order_times = np.random.exponential(average_order_time, num_customers)
        cooking_times = np.random.exponential(alpha, num_customers)
        total_times = order_times + cooking_times

        if np.all(total_times <= max_wait_time):
            successful_simulations += 1

    return successful_simulations / num_simulations

def find_optimal_alpha(alpha_min, alpha_max, tolerance=0.01):
    while alpha_max - alpha_min > tolerance:
        alpha_mid = (alpha_min + alpha_max) / 2
        probability = simulate_service(alpha_mid)

        if probability >= probability_threshold:
            alpha_min = alpha_mid
        else:
            alpha_max = alpha_mid

    return alpha_min

alpha_min = 0.1
alpha_max = 5.0
tolerance = 0.01

alpha_optimal = find_optimal_alpha(alpha_min, alpha_max, tolerance)
print(f"Valoarea maxima a lui α pentru a servi clientii in sub {max_wait_time} minute cu probabilitate de {probability_threshold*100}% este aproximativ: {alpha_optimal:.2f} minute.")


def average_wait_time(alpha, num_simulations=10000):
    total_wait_time = 0
    total_customers = 0

    for _ in range(num_simulations):
        num_customers = np.random.poisson(lambda_customers)
        if num_customers == 0:
            continue
        order_times = np.random.exponential(average_order_time, num_customers)
        cooking_times = np.random.exponential(alpha, num_customers)
        total_times = order_times + cooking_times
        total_wait_time += np.sum(total_times)
        total_customers += num_customers

    average_wait = total_wait_time / total_customers
    return average_wait

average_wait = average_wait_time(alpha_optimal)
print(f"Timpul mediu de asteptare pentru a fi servit al unui client este de aproximativ: {average_wait:.2f} minute.")