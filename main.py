# import square
# square.circle(10)
# # from square import circle
# # circle(10)
#


# import random as r
# num =100
# array = []
# for i in range(num):
#     array.append(r.randint(1, 20))
# print(array)
# array = list(set(array))
# print(array)
#
# print(len(array))



import square
array = square.generateList(100)
array = square.unique(array)
print(array,square.counter(array))


