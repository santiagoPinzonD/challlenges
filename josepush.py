totalp = int(input("Escriba el total de personas : "))
saltos = int(input("Escriba el numero de saltos : "))

def josep(totalp, saltos):
    if totalp == 1:
        return 0
    else:
        return ((josep(totalp - 1, saltos) + saltos) % totalp)

result = josep(totalp, saltos)
print("el ultimo es {}".format(result + 1))

