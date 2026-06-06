# Python  code  for positioning provide manual number

print( "This is int: {0}, This is bool: {1}".format(10, True, 45.7))
print( "This is int: {0}, This is bool: {1}, This is float:{2}".format(10, True, 45.7))
print( "This is int: {2}, This is bool: {0}, This is float:{2}".format(10, True, 45.7))
print( "This is int: {2}, This is bool: {1}, This is float:{0}".format(10, True, 45.7))
#print( "This is int: {3}, This is bool: {4}, This is float:{5}".format(10, True, 45.7))
print( "This is int: {2}, This is bool: {4}, This is float:{3}".format(10, True, 45.7, 'AA', 'B'))
print( "This is int: {2}, This is bool: {1}, This is float:{3}".format(10, True, 45.7, 'AA', 'B'))

## print( "This is int: {2}, This is bool: {}, This is float:{}".format(10, True, 45.7, 'AA', 'B'))


##ValueError: cannot switch from manual field specification to automatic field numbering
##explination for error
## Python wont allow mixing of manual and automatic
## Can it work with both manual and automatic?
## No. Python intentionally disallows mixing them in a single format string because it creates ambiguity about how automatic numbering should continue after manually specified indexes.
## A good rule is:
#Use all {} → automatic numbering.
#Use all {0}, {1}, {2} → manual numbering.
#Don't mix them in the same format string

print("This is int: {num}, This is bool: {flag}, This is float: {value}".format(num=10, flag=True, value=45.7))
#print("This is int: {num}, This is bool: {}, This is float: {value}".format(num=10, flag=True, value=45.7))

print('This is int: {num}, This is bool: {flag}, This is float: {value}'.format(num=10, flag=True, value=45.7))
#print('This is int: {num}, This is bool: {}, This is float: {value}'.format(num=10, flag=True, value=45.7))

# What is string literal anything mentione in between "helloworld" or 'helloworld'

print("Helloworld")
a= "dilipkumar "
print(a)
