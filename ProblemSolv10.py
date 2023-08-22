def contains_all_elements_in_range(arr, A, B):
   range_set = set(range(A, B+1))

   for num in arr:
       if num in range_set:
           range_set.remove(num)

       if not range_set:
           return True

   return False

N = int(input("Enter the number of elements: "))
A = int(input("Enter the lower bound of the range: "))
B = int(input("Enter the upper bound of the range: "))
arr = [int(x) for x in input("Enter the array elements separated by spaces: ").split()]

if contains_all_elements_in_range(arr, A, B):
   print("Yes")
else:
   print("No")