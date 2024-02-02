from collections import OrderedDict
n = int(input())
item_name= OrderedDict()

for _ in range(n):
    *name, net_price = input().split()
    name = ' '.join(name)
    item_name[name]= item_name.get(name,0) + int(net_price)

for item_name, net_price in item_name.items():
    print(item_name, net_price)
