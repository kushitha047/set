***
 Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
***
set1_input = input()
set2_input = input()
set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))
set1.update(set2)
sorted_set = sorted(set1)
print(" ".join(map(str, sorted_set)))
