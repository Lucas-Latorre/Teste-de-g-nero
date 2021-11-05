from tqdm import tqdm
import time
import speech_recognition as sr
import pyttsx3
import os
from tkinter import *


print('Análise de Gênero Sexual')
print()
print('Aviso: Análise baseada em seus dados preenchidos no formulário!')
print()
answer  =input('Fazer o Teste y/n ?')
while answer != 'n':
    print()
    print('Preencha o Formulário')
    print()

    Nome = input('Nome Completo:')
    Idade =input('Idade:')
    Signo =input('Signo:')
    Clube =input('Seu time:')
    Bebida =input('Bebida Preferida:')
    Profissão =input('Profissão:')
    print()
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.say(f' {Nome}, {Idade} anos de  idade, do Signo de {Signo}, torcedor do  {Clube}, que gosta de beber {Bebida}, e trabalha na área de  {Profissão}')
    maquina.say(' Aguarde, estou analisando  seu   Gênero  Sexual...')
    maquina.runAndWait()
   

   
    for i in tqdm(range(10)):
        time.sleep(1)
        

       
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.say(f'{Nome}  você  é,  cem   por   cento   Gueey!' )
    maquina.runAndWait()
   
    answer  =input('Refazer  o Teste y/n ?')
    
  
    

    
       



       
