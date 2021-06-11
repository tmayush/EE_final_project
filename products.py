products = {
    "Beverages": {
        "pepsi": {"Price": 80, "id": 1},
        "cococola": {"Price": 80, "id": 1},
        "sprite": {"Price": 80, "id": 1},
    },
    "Bread": {
        "sandwich loaves": {"Price": 80, "id": 1},
        "dinner rolls": {"Price": 80, "id": 1},
        "tortillas": {"Price": 80, "id": 1},
        "bagels": {"Price": 80, "id": 1},
    },
    "vegetables": {
        "curryleaf": {"Price": 80, "id": 1},
        "cauliflower": {"Price": 80, "id": 1},
        "carrot": {"Price": 80, "id": 1},
    },
    "Dairy": {
        "cheese": {"Price": 80, "id": 1},
        "eggs": {"Price": 80, "id": 1},
        "milk": {"Price": 80, "id": 1},
        "yogurt": {"Price": 80, "id": 1},
        "butter": {"Price": 80, "id": 1},
    },
    "FrozenFoods": {
        "waffles": {"Price": 80, "id": 1},
        "icecream": {"Price": 80, "id": 1},
    },
    "Meat": {
        "lunch meat": {"Price": 80, "id": 1},
        "poultry": {"Price": 80, "id": 1},
        "beef": {"Price": 80, "id": 1},
        "pork": {"Price": 80, "id": 1},
    },
}

for i in products:
    for j in products[i]:
        print(i, "-", j, "-", products[i][j])

