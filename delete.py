***
Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
***
set_input = input()
delete_value = int(input())
values_set = set(map(int, set_input.split()))
if delete_value in values_set:
    values_set.remove(delete_value)  
    sorted_values = sorted(values_set)  
    print(" ".join(map(str, sorted_values)))
else:
    print("Given value is not present in the set list.")
