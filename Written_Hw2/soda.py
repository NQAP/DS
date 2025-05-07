# Function to calculate total sodas
def countSodas(money, price, bottle):
    sodas = money // price
    return sodas + countRec(sodas, bottle)

# Recursive helper function
def countRec(sodas, bottle):
    if sodas < bottle:
        return 0
    newSodas = sodas // bottle
    return newSodas + countRec(sodas % bottle + newSodas, bottle)

# Example usage
money = 15
price = 1
bottle = 3
print(countSodas(money, price, bottle))