my_string="I am learning Python"
print("Is a string Alpha Numeric in nature", my_string.isalnum())
print("Is a string Alpabatic   in nature", my_string.isalpha())
print("Is a string decimal  in nature", my_string.isdecimal())
print("Is a string endswith ", my_string.endswith('Py'))

my_numeric= "987654321"
# this is the string operation and dont get confused with the interger ops and if u mention the varaible without quotes its considered as integer and will be AttributeError: 'int' object has no attribute 'isnumeric' ## issue with begginers like me 
print("is my numer Numeric", my_numeric.isnumeric())

print("Joins the elements of an iterable to the end of the string", "_".join(my_string))

print("It basically zerofill in front of the string which gets printed", my_string.zfill(25))
