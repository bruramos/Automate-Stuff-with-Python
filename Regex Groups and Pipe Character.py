import re

message = 'Call me at 415-555-1001 or 415-555-1002 tomorrow.'

#Procurar o padrão agrupado na string
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)

print(mo.group())
print(mo.group(1))
print(mo.group(2))

message = 'Call me at (415) 555-1001 or 415-555-1002 tomorrow.'

#Procurar o padrão contendo parênteses na string
phoneNumRegex = re.compile(r'\(\d\d\d\) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)

print(mo.group())

message = 'Batman is the owner of the Batmobile and the Batcopter'

#Procurar um padrão com opções usando o pipe (lógica ou)
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search(message)

print(mo.group())

print(batRegex.findall(message))


