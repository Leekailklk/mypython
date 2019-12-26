class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']
    def __init__(self,logo_name):
        self.local_logo=logo_name
    def drink(self,how_much):
        if how_much=='a sip':
            print('cool')
        elif how_much=='bottle':
             print('headace!')

coke_for_China=CocaCola('可口可乐')
coke_for_China.local_logo = '可口可乐'# 本土化
print(coke_for_China.local_logo)
coke = CocaCola('可乐')
coke.drink('a sip')
print(coke.local_logo)
