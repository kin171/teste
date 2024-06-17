from datetime import date
from datetime import datetime

nome = input("Qual o seu nome ?")
anime = input("Qual seu anime esta vendo agora?")
filme = input("qual seu filme favorito")
estado = input("Qual o estado que vc nasceu?")
serie = input("Que serie esta vendo no momento?")
mes = input("QUAL MES VC NASCEU?")
DIA = input("QUAL DIA VC NASCEU?")
anoNascimento = input("Que ano vç nasceu?")
ano = date.today().year

hora = datetime.now().time()
horaFormat = hora.strftime("%H:%M:%S")
calcularIdade = int(ano) - int(anoNascimento)

print(
    "Seja bem vindo ",
    nome,
    ". \nVc tem ",
    calcularIdade,
    " anos \n nasceu no estado: ",
    estado,
    "\n esta vendo o anime",
    anime,
    "\n Seu filme favorito é",
    filme,
)
print(
    "vc esta no ano de",
    ano,
)
print(horaFormat)