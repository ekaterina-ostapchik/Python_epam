import random  # Import the random module to generate random numbers

# Generate a list of 100 random numbers ranging from 0 to 1000
a = [random.randint(0, 1000) for _ in range(100)]
print("Original List:", a)  # Print the original unsorted list

# Sorting the list using a nested loop
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:  # Swap if the current element is greater than the next
            a[i], a[j] = a[j], a[i]

print("Sorted List:", a)  # Print the sorted list

# Separate even and odd numbers into two lists
even_numbers = [num for num in a if num % 2 == 0]  # Extract even numbers
odd_numbers = [num for num in a if num % 2 != 0]  # Extract odd numbers

# Function to calculate the average of a list
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0  # Avoid division by zero

# Calculate the average for even and odd numbers
average_even = calculate_average(even_numbers)
average_odd = calculate_average(odd_numbers)

# Print the results
print(f"Average of even numbers: {average_even}")
print(f"Average of odd numbers: {average_odd}")
