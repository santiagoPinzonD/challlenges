def weight_average(my_list=[]):
    #for x in range(0, len(my_list)):
        #for z in range(0, len(my_list))
    return sum(x[0] * x[1] for x in my_list) / (sum(x[1] for x in my_list)

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))