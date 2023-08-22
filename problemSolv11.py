def longest_palindromic(s):
    n = len(s)
    longest = ""
    
    
    for i in range(n):
        left = right = i
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > len(longest):
                longest = s[left:right + 1]
            left -= 1
            right += 1
        
        left = i
        right = i + 1
        
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > len(longets):
                longest = s[left:right + 1]
            left -= 1
            right += 1
        return longest
strr = input("enter a string: ")
result = longest_palindromic(strr)
print("the longest palindromic substrung : ", result)
