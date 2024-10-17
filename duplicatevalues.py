***
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5
***
set_input = input()
values_set = set(map(int, set_input.split()))
print(len(values_set))
