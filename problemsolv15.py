def first_nonRepeating_char(S):
    char_freq = {}
    
    for char in S:
        
        if char in char_freq:
            char_freq[char] += 1
        
        else:
            char_freq[char] = 1
            
    for char in S:
        if char_freq[char] == 1:
            return char
    return '$'

S = "hello"
output = first_nonRepeating_char(S)
print(output)