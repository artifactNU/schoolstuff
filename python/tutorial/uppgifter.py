# ----------------------------------------------------------
# Hitta ett tal större än ett visst värde


# def find_greater_than(lista, value):
#     if type(lista) is not list:
#         return False, "lista måste vara en lista"
#     if type(value) not in [int, float]:
#         return False, "value måste vara ett tal"
#     return [x for x in lista if x > value]


# print(find_greater_than([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# print(find_greater_than([1, 2.5, 3, 4, 5.2, 6.8, 7.1, 8, 9.1, 10.9], 3))
# print(find_greater_than([-9, -3, 2, 8, 15, 31, 5, 4, 8], 5))
# ----------------------------------------------------------

lst = [80, 20, 10, 5, 4]

hittat_tal = None

for element in lst:
    if element < 10:
        if hittat_tal is None:
            hittat_tal = element
    print(element)
