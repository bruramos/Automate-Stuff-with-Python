import re

#Verificar se um grupo aparece zero ou uma vez com ?
batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search('The adventures of Batwoman')
print(mo.group())


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-1234')

print(mo.group())


#Verificar se um grupo aparece zero ou mais vezes com *
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The adventures of Batwowowoman')
print(mo.group())


#Verificar se um grupo aparece uma ou mais vezes com +
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The adventures of Batwowoman')
print(mo.group())


#Procurar +, *, ? literais
regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())


#Procurar uma quantidade específica de repetições
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said HaHaHaHa')
print(mo.group())


#Greedy (procura o maior possível) e Nongreedy (procura o menor possível) match
digitGreedyRegex = re.compile(r'(\d){3,5}')
digitNongreedyRegex = re.compile(r'(\d){3,5}?')

message = '123456789'

mo = digitGreedyRegex.search(message)
print(mo.group())

mo = digitNongreedyRegex.search(message)
print(mo.group())
