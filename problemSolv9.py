def count_substrings_with_equal_case(s):
   n = len(s)
   count = 0
   lowercase_count = 0
   uppercase_count = 0

   for i in range(n):
       if s[i].islower():
           lowercase_count += 1
       else:
           uppercase_count += 1

       if lowercase_count == uppercase_count:
           count += 1

   return count

input_str = "WomensDAY"
result = count_substrings_with_equal_case(input_str)
print("Number of substrings with equal case:", result)  