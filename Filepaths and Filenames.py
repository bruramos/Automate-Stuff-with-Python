import os

os.path.join('C:', 'Users') #juntar diretórios para qualquer sistema operacional

os.getcwd() #ver o diretório ativo

os.chdir('C:\\') #mudar o diretório ativo

os.path.dirname('C:\\Users\\teste.txt') #Retorna o caminho dos diretórios

os.path.basename('C:\\Users\\teste.txt') #Retorna o nome do arquivo ou último diretório

os.path.exists('C:\\Users\\teste.txt') #Verifica se o caminho ou arquivo existem

os.path.isdir('C:\\Users') #Verifica se o caminho é de uma pasta

os.path.isfile('C:\\Users\\teste.txt') #Verifica se o caminho é de um arquivo

os.path.getsize('C:\\Users') #Retorna o tamanho da pasta em int bytes

os.listdir('C:\\Users') #Retorna uma lista de strings dos diretórios e arquivos dentro da pasta

os.makedirs('C:\\Pasta1\\Pasta2') #Cria as pastas conforme especificado


#Caminho Absoluto -> Sempre começa com C://

os.path.abspath('C:\\Users') #Passa um caminho absoluto

os.path.isabs('C:\\Users') #Verifica se o caminho é absoluto ou relativo


#Caminho Relativo -> Relativo ao diretório ativo

os.path.relpath('C:\\Users', 'C:\\') #Retorna o caminho relativo entre dois caminhos

