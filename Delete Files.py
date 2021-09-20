import os

#Excluir apenas um arquivo
os.unlink('teste.txt')

#Excluir diretório (precisa estar vazio)
os.rmdir('C:\\Pasta1\\Pasta2')

import shutil

#Exclui permanentemente uma pasta com todos seus arquivos e pastas internos
shutil.rmtree('C:\\Pasta1\\Pasta2')

import send2trash

#Excluir arquivo e enviar para a lixeira
send2trash.send2trash('C:\\Pasta1\\Pasta2\\teste.txt')
