***
Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
***
set_input = input("Enter values separated by space: ")
values_set = set(map(int, set_input.split()))
maximum_value = max(values_set)
minimum_value = min(values_set)
print(f"Maximum: {maximum_value}")
print(f"Minimum: {minimum_value}")
