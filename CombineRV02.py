import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Parameters
mu1 = 0
sigma1 = 1
mu2 = 10
sigma2 = 1
p = 0.2

# Number of realizations
n = 10000

# Simulate the realizations of Y
uniform_samples = np.random.uniform(0, 1, n)
normal_samples_1 = np.random.randn(n) * sigma1 + mu1
normal_samples_2 = np.random.randn(n) * sigma2 + mu2

# Select from X1 or X2 based on the uniform_samples
realizations_Y = np.where(uniform_samples < p, normal_samples_1, normal_samples_2)

plt.figure(figsize=(10, 6))
sns.distplot(realizations_Y, bins=50, kde=True, hist=True, label='Distribution of Y for Realizations')
plt.xlabel('y')
plt.ylabel('Density')
plt.title('Distribution of Y with 10,000 Realizations')
plt.legend()
plt.grid(True)
plt.show()
