import openpyxl

# Escolher a planilha que quer ler
book = openpyxl.load_workbook('Planilha de compras.xlsx')

# Escolhendo página
frutas_page = book['Frutas']

# Imprimindo as linhas
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
   for cell in rows:
       #Alterar algum valor
        if cell.value == 'Banana':
            cell.value = 'Maracuja'

# Salvar
book.save('Planilha de compras v2.xlsx')