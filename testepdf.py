import tabula
lista_tabelas = tabula.read_pdf('mpdf.pdf', pages='1')
print (len(lista_tabelas))
for tabela in lista_tabelas:
    print(tabela)