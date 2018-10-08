#stings

#basics
'hello'
"hello"

"I'm a dog"

mystring= 'abcdefg'

print(mystring[0])

#last char
print(mystring[-1])

#from letter 'e' till the end
print(mystring[4:])

#up to and not including
print(mystring[:3])

print(mystring[2:5])

#whole string
print(mystring[:])

#step size 2
print(mystring[::2])


#methods
print(mystring.upper())

print(mystring.lower())

print(mystring.capitalize())

#splitting string
mystring= 'hello world'

print(mystring.split())

print(mystring.split('o'))

#insert string into string
mystring= '{y} {x}'.format(x='Bia',y='szia')

print(mystring)