import numpy as np


arr = np.arange(1, 28).reshape(3, 3, 3)

print("3D Array:")
print(arr)

# Flatten the array
flat = arr.flatten()
print("Flattened Array:", flat)

# Calculate statistical values
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))