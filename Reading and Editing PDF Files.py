import PyPDF2, os

os.chdir('C:\\Users\\Bruna Ramos\\Documentos\\Automate Stuff with Python')

pdfFile = open('meetingminutes.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)

reader.numPages #Numero de páginas do documento

page = reader.getPage(0) #Pegar uma página específica do documento
page.extractText() #Extrair o texto dessa página específica

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())
