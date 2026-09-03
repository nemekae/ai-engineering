import numpy as np # type: ignore  # noqa: I001

# Array and Scalar broadcasting
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([10, 20, 30])

result = a + b  

print (result)
print("Sum: ", np.sum(result))
print("Mean: ", np.mean(result))
print("Max: ", np.max(result))
print("Min: ", np.min(result))
print("Standard Deviation: ", np.std(result))
print("Variance: ", np.var(result))

print("\n")

# Generate a random array of shape (5, 5) with values between 1 and 50
dataset = np.random.randint(1, 51, size=[5, 5])  # Random array of shape (2, 3)
print("Random Array: \n", dataset)

print("\n")

# Filter values greater than 25 and change with 0
filtered_dataset = dataset.copy()
filtered_dataset[filtered_dataset > 25] = 0
print("Filtered Array (values > 25 set to 0): \n", filtered_dataset)

print("\n")
# Calculate the statistics of the filtered dataset
print("Sum of Filtered Array: ", np.sum(filtered_dataset))
print("Mean of Filtered Array: ", np.mean(filtered_dataset))
print("Max of Filtered Array: ", np.max(filtered_dataset))
print("Min of Filtered Array: ", np.min(filtered_dataset))      
print("Standard Deviation of Filtered Array: ", np.std(filtered_dataset))
print("Variance of Filtered Array: ", np.var(filtered_dataset))