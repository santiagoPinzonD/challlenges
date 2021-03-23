def pairs(n):
    list1 = [1, 2, 3, 9]
    control = 0
    for x in range(0, len(list1) -1):
        for z in range(len(list1) -1):
            if z <= len(list1) - 1:
                suma = list1[x] + list1[z + 1]
                if suma == n:
                    return True
                else:
                    suma = 0
    if control == 0:
        return False
    
print(pairs(4))
