def rabbit(month:int, offsprint:int)->int:
    parent, child = 1,1
    for i in range(month-1):
        child, parent = parent, parent + (child*offsprint)

    return child

print(rabbit(34,2))