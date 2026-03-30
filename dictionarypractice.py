sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]

def bad_version():
    C = 0
    S = 0
    E = 0
    M = 0
    STR = 0
    D = 0
    for i in sushi_orders:
        if i['name'] == 'California Roll':
            C +=1
        elif i['name'] == 'Salmon Nigiri':
            S +=1
        elif i['name'] == 'Edamame':
            E +=1
        elif i['name'] == 'Miso Soup':
            M +=1
        elif i['name'] == 'Spicy Tuna Roll':
            STR +=1
        elif i['name'] == 'Dragon Roll':
            D +=1
    print("you have", C, "cali rolls", S, "salm nigiri", E, "edamame", M, "miso soup", STR, "spicy tuna rolls and", D, "dragon rolls")
bad_version()

def good_version():
    the_receipt = {}
    for sushi in sushi_orders:
        if sushi['name'] in the_receipt:
            continue
        else:
            the_receipt[sushi['name']] = {
                'price': sushi['price'],
                'qty': 1,
            }
    print(the_receipt)

good_version()