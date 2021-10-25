quantApl = int(input("How many apple do you want to buy? \n> "))
quantOrng = int(input("How many orange do you want to buy? \n> "))

aplPrice = quantApl * 20
orngPrice = quantOrng * 25

overallTtl = aplPrice + orngPrice

print(f'Apple: 20 pesos * {quantApl} piece/s = {aplPrice}')
print(f'Orange: 25 pesos * {quantOrng} piece/s = {orngPrice}')

print(f'The total amount is {overallTtl} pesos.')