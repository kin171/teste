import json

import pandas as pd 

with open('jornada_agricola.txt', 'r') as arquivo:
    dados=json.load(arquivo)
    print(dados)    
    