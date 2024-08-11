my_dict = {'Nika' : 1982 , 'Oleg' : 2000}
print(my_dict)
print(my_dict.get('Nika'))
print(my_dict.get('Any'))
my_dict['Any'] = 2002
my_dict['Poly'] = 1980
print (my_dict)
print(my_dict.pop ('Oleg'))
print(my_dict)
my_set = {1,11,12,1,11,12, 'Polly', 'Polly', 'Polly', 'Polly', 'Polly'}
print(my_set)
my_set.add('Nikola')
my_set.add(10)
my_set.discard(11)
print(my_set)


