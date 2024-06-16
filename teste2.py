nome=input('Qual o seu nome ?')
es=input('Qual o estado que vc nasceu?')
t1=input('Que ano vç nasceu?')
from datetime import date
from datetime import datetime
t2=date.today().year
t3=datetime.now().time()
t3format=t3.strftime('%H:%M:%S')
calc=int(t2) - int(t1)
print(nome,'Vc tem ',calc, 'anos e nasceu no estado ',es)
print ('vc esta no ano de',t2,)
print(t3format)