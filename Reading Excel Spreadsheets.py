import openpyxl, os

os.chdir('C:\\Users\\Bruna Ramos\\Documentos\\Automate Stuff with Python')

workbook = openpyxl.load_workbook('example.xlsx') #Abrir Workbook

sheet = workbook.get_sheet_by_name('Sheet1') #Abrir Sheet

workbook.get_sheet_names() #Ver o nome de todas as Sheets

cell = sheet['A1'] #Retorna um objeto com informações da célula

cell.value #Retorna o valor da célula

sheet.cell(row=1, column=2) #Retorna um objeto com informações da célula
