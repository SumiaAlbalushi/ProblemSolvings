def find_distinct_sum(num):
    n = len(num)
    distinct_sum = set()
    
    for i in range(2 ** n):
        subset_sum = 0
        for j in range(n):
            if i & (1<<j):
                subset_sum += num[j]
        distinct_sum.add(subset_sum)
        
    return list(distinct_sum)

num = [1,2]
distinct_sum = find_distinct_sum(num)
print(distinct_sum)