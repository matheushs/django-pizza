orders = []


def add_order(name, flavor, observation=None):
    order = {}
    order['name'] = name
    order['flavor'] = flavor
    order['observation'] = observation
    return order


orders.append(add_order('Mario', 'Pepperoni'))
orders.append(add_order('Pirao', 'Rola', 'Prefiro pegar o Ordonha'))

for order in orders:
    if order['observation']:
        template = 'Name: {name}\nFlavor: {flavor}\nObservation: {observation}'
    else:
        template = 'Name: {name}\nFlavor: {flavor}'
    print(template.format(**order))
    print('-'*30)
