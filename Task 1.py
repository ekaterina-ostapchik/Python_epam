import random

a= random.sample(range(1, 101), 100)
print(a)

# sorting list using nested loops
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[i] >= a[j]:
            a[i], a[j] = a[j], a[i]

# sorted list
print("Sorted List", a)

# Separate the even and odd numbers into two different lists
even_numbers = [num for num in a if num % 2 == 0]  # List comprehension for even numbers
odd_numbers = [num for num in a if num % 2 != 0]  # List comprehension for odd numbers

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:  # Avoid division by zero if the list is empty
        return 0
    return sum(numbers) / len(numbers)  # Calculate sum and divide by the length of the list

# Calculate the average for even numbers
average_even = calculate_average(even_numbers)

# Calculate the average for odd numbers
average_odd = calculate_average(odd_numbers)

# Print the average result for even numbers
print(f"Average of even numbers: {average_even}")

# Print the average result for odd numbers
print(f"Average of odd numbers: {average_odd}")