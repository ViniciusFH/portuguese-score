from corretor import *
from grande_dicionario import dicionario
import time
import unidecode
import re
repeater = True
while repeater:
    score = 1.0
    palavras = [word.lower() for word in unidecode.unidecode(re.sub('[\"\'\-]+'," ",input("Insira a frase: "))).split() if not re.match("^[^a-zA-Z]+$",word)]
    temp_1=time.time()
    if len(palavras)>0 and len(palavras)<15:
        erradas,informais = identifica(palavras,dicionario)
        informais = len(informais)
        corretas = len(palavras)-(len(erradas)+informais)
        sugestoes,niveis = corretor_frase(erradas,dicionario)
        impossiveis = len([impossivel for impossivel in sugestoes if len(sugestoes[impossivel])==0])
        um = len([nivel for nivel in niveis if nivel==1])
        dois = len([nivel for nivel in niveis if nivel==2])
    else:
        erradas = 0
        informais = 0
        corretas = 0
        impossiveis = 0
        um = 0
        dois = 0
    peso(len(palavras),corretas,um,dois,impossiveis,informais)
