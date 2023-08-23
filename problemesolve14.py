def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2, operand1 = stack.pop(), stack.pop()
            stack.append(eval(f"{operand1}{char}{operand2}"))
    return stack[0]
expression = "231*9-"
result = evaluate_postfix(expression)
print("output",result)