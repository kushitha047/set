***
 Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
***
set_input = input()
values_list = list(map(int, set_input.split()))
unique_values_set = set(values_list)
duplicate_count = len(values_list) - len(unique_values_set)
print(f"Duplicate Values: {duplicate_count}")
sorted_unique_values = sorted(unique_values_set)
print(" ".join(map(str, sorted_unique_values)))
