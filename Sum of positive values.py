'''calculates the sum of all non-negative numbers in the list arr.
✅ Time complexity: O(n) — most optimized for this task.'''

arr = [-1,50,23,-66,-8,65,7,2]

sum = 0
for i in arr:
    if i >=0 :
        sum += i
print(sum) 