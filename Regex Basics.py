import re

message = 'Call me at 415-555-1001 or 415-555-1002 tomorrow.'

#Procurar o padrão na string
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)

print(mo.group())

#Procurar todas as ocorrências
print(phoneNumRegex.findall(message))
