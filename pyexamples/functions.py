orders = []


def add_order(name, flavor):
    order = {}
    order['name'] = name
    order['flavor'] = flavor

    orders.append(order)

print(orders)
add_order('Mario', 'pepperoni')
add_order('Pirao', 'rola')
print(orders)
