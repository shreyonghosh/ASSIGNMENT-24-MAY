def calculate(operation, *args):
    if not args:
        return 0
    
    if operation == '+':
        result = 0
        for num in args:
            result += num
        
        return result
    
    elif operation == '-':
        result = args[0]
        for num in args[1:]:
            result -= num

        return result
    
    elif operation == '*':
        result = 1
        for num in args:
            result *= num

        return result
    
    elif operation == '/':
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise ValueError("Division by zero is not allowed")
            
            result /= num
        
        return result
    else:
        raise ValueError(f"Unsupported operator: '{operation}")
    
print(calculate('+', 1, 2, 3))
print(calculate('*', 2, 3, 4))
