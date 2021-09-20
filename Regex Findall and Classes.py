import re

message = 'Call me at 415-555-1234, 415-555-2345 or 415-555-3456'

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.findall(message))

#Com 2 grupos
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(message))

#Com 3 grupos
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(message))


lyrics = '''12 drummers drumming,
11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking,
7 swans a-swimming, 6 geese a-laying, 5 golden rings, 4 calling birds,
3 French hens, 2 turtle doves, And a partridge in a pear tree!'''

#Achar os números com as palavras seguintes
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

#Modelo de regex para caracteres (vogais)
vowelRegex = re.compile(r'[aeiou]') # mesma coisa que r'(a|e|i|o|u)

#Modelo de regex para caracteres (2 ou mais vogais)
vowelRegex = re.compile(r'[aeiou]{2}')

#Modelo de regex para caracteres (exceto vogais)
consonantRegex = re.compile(r'[^aeiou]{2}')

#Modelo de regex para caracteres (vogais maiúsculas e minúsculas)
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE) #ou re.I
