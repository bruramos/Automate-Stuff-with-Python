#Programa que verifica o tamanho dos arquivos dentro de determinada pasta

import os

TotalSize = 0

for filename in os.listdir('C:\\Users'):
    if not os.path.isfile(os.path.join('C:\\Users', filename)):
        continue
    TotalSize = TotalSize + os.path.getsize(os.path.join('C:\\Users', filename))

print(TotalSize)
