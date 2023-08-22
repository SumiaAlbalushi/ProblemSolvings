def find_leaders(arr):

    n = len(arr)

    max_right = arr[n - 1]

    leaders = [max_right]


    for i in range(n - 2, -1, -1):

        if arr[i] >= max_right:

            max_right = arr[i]

            leaders.append(max_right)


    return leaders[::-1]  


A = [16, 17, 4, 3, 5, 2]

leaders = find_leaders(A)

print("Leaders in the array:", leaders)  