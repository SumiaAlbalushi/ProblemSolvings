def find_pairs_with_sum(arr, target):
   pairs = []

   for i in range(len(arr)):
       complement = target - arr[i]
       if complement in arr[i+1:]:
           pairs.append((arr[i], complement))

   return pairs

arr = [int(x) for x in input("Enter an array of numbers separated by spaces: ").split()]
target = int(input("Enter the target number: "))

pairs = find_pairs_with_sum(arr, target)
print("Pairs with sum", target, ":", pairs)