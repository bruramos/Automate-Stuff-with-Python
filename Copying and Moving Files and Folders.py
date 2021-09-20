import shutil

shutil.copy('C:\\Users\\Teste.txt', 'C:\\') #Copia o arquivo para a nova pasta

shutil.copy('C:\\Users\\Teste.txt', 'C:\\TesteTeste.txt') #Copia e renomeia o arquivo para a nova pasta

shutil.copytree(('C:\\Users', 'C:\\Users (Backup)') #Copia toda a pasta para outro diretório especificado

shutil.move('C:\\Users\\Teste.txt', 'C:\\') #Move o arquivo de pasta

shutil.move('C:\\Users\\Teste.txt', 'C:\\Users\\TesteTeste.txt') #Renomear o arquivo
