def rearrange_lternate(arr,n):
    positive_indx = 0
    negetive_indx = 0
    
    for i in range(n):
        if arr[i]<0:
            negetive_indx = i
            break
        
        
    while positive_indx < n and negetive_indx < n:
       
        while positive_indx < n and arr[positive_indx] >= 0:
           positive_indx += 1
        
        while negetive_indx < n and arr[negetive_indx] >= 0:
           negetive_indx += 1
           
           
    if positive_indx < n and negetive_indx < n:
            arr[positive_indx], arr[negetive_indx] = arr[negetive_indx], arr[positive_indx]
    
    return arr
N = 9
arr =[9, 4,-2, -1, 5, 0, -5, -3, 2]
output = rearrange_lternate(arr , N)
print(output)

