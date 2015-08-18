orders = [
    {
        'name': 'Mario',
        'flavor': 'Pepperoni'
    },
    {
        'name': 'Pirao',
        'flavor': 'Rola'
    }
]

for order in orders:
    s = 'Nome: {}\nSabor: {}'
    print(s.format(order['name'], order['flavor']))
