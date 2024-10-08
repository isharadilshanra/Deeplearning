import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu1 = 0
sigma1 = 1
mu2 = 10
sigma2 = 1
p = 0.2

# PDF of the mixture
def pdf_Y(y):
    return p * norm.pdf(y, mu1, sigma1) + (1 - p) * norm.pdf(y, mu2, sigma2)

# Range of values
y = np.linspace(-5, 15, 1000)

# Compute PDF values
pdf_values = pdf_Y(y)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(y, pdf_values, label='PDF of Y')
plt.xlabel('y')
plt.ylabel('Density')
plt.title('PDF of the Mixture Distribution Y')
plt.legend()
plt.grid(True)
plt.show()
