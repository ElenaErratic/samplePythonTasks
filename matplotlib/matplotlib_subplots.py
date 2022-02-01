import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10)
y = x

fig, axes = plt.subplots(3, 3, figsize=(10, 16))

axes[1, 1].plot(x, y)
plt.show()
