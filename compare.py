def compare(a, b):
    sum = ""
    for x in a:
        for z in b:
            if x == z:
                sum+= x
                break
    return sum

a = "ABCDE"
b = "EFGAAAAB"
print(compare(a, b))