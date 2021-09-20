import re

#Verificar se começa com um padrão
beginsWithHelloRegex = re.compile(r'^Hello')
beginsWithHelloRegex.search('Hello there!')

#Verificar se termina com um padrão
endsWithHelloRegex = re.compile(r'world!$')
endsWithHelloRegex.search('Hello world!')

#Verificar se todos os dígitos batem (começa e termina com o padrão)
allDigitsRegex = re.compile(r'^\d+$')
allDigitsRegex.search('123456789')


#Ponto procura qualquer caracter exceto pular linha
atRegex = re.compile(r'.at')
message = 'The cat in the hat sat on the flat mat'
print(atRegex.findall(message))

#Ponto procura qualquer caracter exceto pular linha (entre 1 e 2 vezes)
atRegex = re.compile(r'.{1,2}at')
message = 'The cat in the hat sat on the flat mat'
print(atRegex.findall(message))

#Ponto procura qualquer caracter
dotStarRegex = re.compile(r'.*', re.DOTALL)

#Procurar padrão no meio de textos
text = 'First Name: Bruna Last Name: Sousa'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(text))

