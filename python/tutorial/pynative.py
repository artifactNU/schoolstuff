# Reverse list

# list1 = [100, 200, 300, 400, 500]

# list1.reverse()
# print(list1)

# ---

# Concatenate two lists index-wise

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# # Expected output:
# #['My', 'name', 'is', 'Kelly']

# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)

# ---

# Turn every item of a list into its square

# numbers = [1, 2, 3, 4, 5, 6, 7]

# # Expected output:
# #[1, 4, 9, 16, 25, 36, 49]

# result = [i * i for i in numbers]
# print(result)

# ---

# Concatenate two lists in the following order

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# # Expected output:
# # ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# result = [i + j for i in list1 for j in list2]
# print(result)

# ---

# Iterate both lists simultaneously

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# # Expected output:
# # 10 400
# # 20 300
# # 30 200
# # 40 100

# for i, j in zip(list1, list2[::-1]):
#     print(i, j)

# ---

# Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Expected output:
# ["Mike", "Emma", "Kelly", "Brad"]

result = list(filter(None, list1))
print(result)
