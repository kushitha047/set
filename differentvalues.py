***
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
***
set1_input = input()
set2_input = input()
set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))
difference = set1.difference(set2)
sorted_difference = sorted(difference)
print(" ".join(map(str, sorted_difference)))
