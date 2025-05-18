import matplotlib.pyplot as plt
import numpy as np

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate natural numbers and their prime status
natural_numbers = np.arange(1, 51)
prime_flags = [is_prime(n) for n in natural_numbers]

# Create the bar chart
plt.figure(figsize=(10, 5))
plt.bar(natural_numbers, prime_flags, color=['red' if is_prime(n) else 'gray' for n in natural_numbers])
plt.xlabel("Natural Numbers")
plt.ylabel("Prime (1) or Not Prime (0)")
plt.title("Prime Numbers Among Natural Numbers (1-50)")
plt.xticks(natural_numbers)
plt.yticks([0, 1], ["Not Prime", "Prime"])
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Show the plot
plt.show()
