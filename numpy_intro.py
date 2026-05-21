
import numpy as np
import matplotlib.pyplot as plt

monthly_sales = np.array([15000, 18000, 22000, 19000, 25000, 28000])
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])

print(f'{monthly_sales.mean():.2f}')
print(monthly_sales.max())
plt.plot(months, monthly_sales, marker='o')
plt.savefig('monthly_sales.png')
plt.clf()