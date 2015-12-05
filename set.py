#zoo is a tuple, which is a list whose variable values cannot be changed by the program
zoo = ('Kangaroo', 'Leopard','Moose')
print('Tuple:',zoo, '\tLength',len(zoo) )
print(zoo)

#set is where a restrictive python list of unique values, and created by assigning values as a comma-separated list between curly brackets (braces): phonetic-set = {'Alpha','Bravo', 'Bravo'}

bag = {'Red', 'Green','Blue'}
bag.add('Yellow')
print('\nSet:', bag, '\tLength',len(bag))
print(type(bag))

print('\nIs Green In bag Set?:', 'Green' in bag)
print('Is Orange In bag Set?:', 'Orange' in bag)

box = {'Red', 'Purple', 'Yellow'}
print('\nSet:', box, '\t\tLength', len(box))
print('Common To Both Sets:' , bag.intersection(box))
