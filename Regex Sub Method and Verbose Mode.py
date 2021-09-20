import re

#Substituir strings no padrão
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice and Agent Bob are married'))

print(namesRegex.sub('REDACTED','Agent Alice and Agent Bob are married'))


namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice and Agent Bob are married'))

print(namesRegex.sub('Agent \1****','Agent Alice and Agent Bob are married'))


#Verbose para pular linha no Regex
re.compile(r'''
(\d\d\d) #area code 
-        #first dash
\d\d\d   #first 3 digits
-        #second dash
\d\d\d\d #last 4 digits''', re.VERBOSE)
