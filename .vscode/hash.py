
faturamento =1_000
custo = 300
faturamento = faturamento + 500
print (faturamento)
print (custo)
imposto = (faturamento * 0.1)
lucro = (faturamento - custo - imposto)
email = 'kin5090@hotmail.com'
'''
print (imposto)
print (lucro)
print(f'A dinato teve um faturamento de {faturamento} \n com um custo de {custo} \n e um lucro de {lucro} \n no email {email}')
print (email.find('@'))
print (len(email))


print ('a among us teve um lucro de{} \n com um faturamento de {} \n e um custo de{} \n com um imposto de {}'.format(lucro, faturamento, custo, imposto))
tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12)
print (tempo_em_anos, 'anos')
print (tempo_em_meses % 12, 'meses')
'''
nome = 'antonio henrique  honorio'
email = 'kin5090@hotmail.com'
posicao = email.find('@')
servidor = email[posicao :]
nome_email = email[: posicao ]
margem =  lucro / faturamento
posicao_nome =nome.find(' ')
primeiro_nome = nome[: posicao_nome]
print(f' O faturamento {faturamento :.2f}\n custo foi de {custo:.2f}\n e o lucro {lucro:.2f}\n com uma margem de lucro de {margem:.0%}')
print (f'O {nome} acabou de se cadastrar no site da union, \n email:{email}\n servidor:{servidor} \n nome email:{nome_email} \n seja bem vindo  {primeiro_nome} ')
tracar_email = email.replace (:posicao,1:posicao))