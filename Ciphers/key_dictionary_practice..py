dict = {}
column_order = []
direction = []
cols = int(input("Enter the column number: "))
for i in range(cols):
    route_key = int(input("Enter the key value: "))
    column_order.append(abs(route_key))
    if route_key > 0:
        direction.append("+")
    else:
        direction.append("-")
dict = dict.fromkeys(column_order)
direction_reverse = list(reversed(direction))
for key, value in dict.items():
    dict[key] = direction_reverse.pop()
print(dict)
