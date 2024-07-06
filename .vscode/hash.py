faturamento =1000
custo = 300
faturamento = faturamento + 500
print (faturamento)
print (custo)
imposto = (faturamento * 0.1)
lucro = (faturamento - custo - imposto)


print (imposto)
print (lucro)
print ('a among us teve um lucro de{} \n com um faturamento de {} \n e um custo de{}'.format(lucro, faturamento, custo))