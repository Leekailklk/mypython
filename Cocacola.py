class CocaCola:
    formula=['coffeine','sugar','water','soda']
    def drink(self):
        print('energy')

coke_for_me=CocaCola()
coke_for_you=CocaCola()
print(CocaCola.formula)
coke_for_me.drink()
print(coke_for_you.formula)
for element in coke_for_me.formula:
    print(element)
print("\N{Cat}")