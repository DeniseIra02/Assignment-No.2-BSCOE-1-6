money = int(input("How much is your money? \n> "))
aplPrice = int(input ("How much is the price of apple per piece? \n> "))

aplQuant = money // aplPrice
total = aplQuant * aplPrice
change = money - total

print(f'Quantity: {money} pesos / {aplPrice} pesos = {aplQuant} apple/s')
print(f'Total: {aplQuant} apple/s * {aplPrice} pesos = {total} pesos')
print (f'Change: {money} pesos - {total} pesos = {change} pesos')

print(f'You can buy {aplQuant} apple/s and your change is {change} pesos.')