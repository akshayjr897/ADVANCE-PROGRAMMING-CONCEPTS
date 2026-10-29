import numpy as np

arr = np.array([50, 10, 40, 20, 30])

print("Original Array:", arr)

# Ascending order
asc = np.sort(arr)
print("Ascending Order:", asc)

# Descending order
desc = np.sort(arr)[::-1]
print("Descending Order:", desc)