
OpenTextFile = open('C:\\Users\\Bruna Ramos\\Teste.txt') #Abre o arquivo em modo de leitura e retorna um FileObject

WriteTextFile = open('C:\\Users\\Bruna Ramos\\Teste.txt', 'w') #Abre o arquivo em modo de escrita para sobreescrever texto e retorna um FileObject

AppendTextFile = open('C:\\Users\\Bruna Ramos\\Teste.txt', 'a') #Abre o arquivo em modo de escrita para adicionar texto e retorna um FileObject


Content = OpenTextFile.read() #Lê o arquivo e retorna uma string

Contents = OpenTextFile.realines() #Lê as linhas do arquivo e retorna uma lista de strings

WriteTextFile.write('Teste') #Escreve no arquivo

TextFile.close() #Fecha o arquivo


#Biblioteca que cria dicionários para strings em modelo binário
import shelve

ShelfFile = shelve.open('Dados') #Abrir o storage
ShelfFile['Teste'] = ['Teste1', 'Teste2', 'Teste3'] #Inserir informações
ShelfFile.close() #Fechar o storage

list(ShelfFile.keys()) #Mostrar todas as chaves do dicionário criado
lis(ShelfFile.values()) #Mostrar todos os valores dentro do dicionário criado



