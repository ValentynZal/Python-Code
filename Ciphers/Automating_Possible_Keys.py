from itertools import combinations
from itertools import permutations

# cols = int(input("Enter the column number: "))
cols = 4
etalon = ""
for i in range(1, cols+1):
    etalon += str(i)
perms = {''.join(i) for i in permutations(etalon)}

# list_perms = []
# i = 0
# for substr in perms:
#     i = 0
#     li = []
#     for j in range(0, len(substr)):
#         li.append(int(substr[j]))
#     list_perms[i] = tuple(li)
#     i += 1

# for substr in perms:
#     i = 0
#     list_perms[i] = tuple(substr)
#     i += 1
list_perms = []
j = 0
for substr in perms:
    list_perms[j] = [int(i) for i in substr.split()]

for i in list_perms:
    print(i)
    print("\n")