
def fibonacci(ind: int) -> int:
    if ind == 0:
        return 0 
    elif ind == 1:
        return 1
    else:
        return fibonacci(ind-1)+fibonacci(ind-2)


print(fibonacci(23))
    