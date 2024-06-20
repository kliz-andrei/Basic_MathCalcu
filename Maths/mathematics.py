def multiplication(a, b):
    result = a * b
    return result

def summation(a, b):
    result = a + b
    return result

def subtraction(a, b):
    result = a - b
    return result

def division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    result = a / b
    return result
