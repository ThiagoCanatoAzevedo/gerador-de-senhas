# -*- coding: utf-8 -*-
import string
import random
import os

numeros = []

os.system('cls')

def listaAlfabetoNumerosCaracteresEspeciais():
    global numeros
    global letrasMaiusculas 
    global letrasMinusculas
    global caracteresEspeciais

    letrasMaiusculas = list(string.ascii_uppercase)
    letrasMinusculas = list(string.ascii_lowercase)
    caracteresEspeciais = ['!', '@', '#', '$', '%', '&', '-', '*', '_', '+', '=', '§', '?', '/', '|', '*', '.', ',']

    cont = 0
    while (cont < 10):

        numeros.append(str(cont))
        cont+=1
    
def escolhaTipoSenha():
    global tipoSenha
    tipoSenha = input("Você gostaria de uma senha fraca, média, ou forte? APERTE + PARA SABER O QUE CADA UMA POSSUI - ")
    print("-"*50)
    
    if(tipoSenha == "+"):
        tipoSenha = input("Aqui vai o que cada uma faz.\n Fraca: Apenas letras minúsculas e maiúsculas \n Média: Letras minúsculas, maiúsculas e números \n Forte: Possui tudo. Letras maiúsculas e minúsculas, números e caracteres especias \n Agora escolha uma ")

    elif (tipoSenha == "Forte" or tipoSenha == "forte"):
        print("Você escolheu a senha: ", tipoSenha)
    elif (tipoSenha == "Média" or tipoSenha == "média" or tipoSenha == "media" or tipoSenha == "Media"):
        print("Você escolheu a senha: ", tipoSenha)
    else:
        print("Você escolheu a senha: ", tipoSenha)


def randomizacaoSenha():
    global senhaFinal
    cont = 0

    senhaFinal = []
    letrasMaiusculasMinusculasFraca = letrasMaiusculas + letrasMinusculas
    letrasMaiusculasMinusculasNumerosMedia = letrasMaiusculasMinusculasFraca + numeros
    letrasMaiusculasMinusculasNumerosCaracteresEspeciaisFim = letrasMaiusculasMinusculasNumerosMedia + caracteresEspeciais

    if(tipoSenha == "Forte" or tipoSenha == "forte"):
        while(cont < 8):
            senhaForteElementos = random.choice(letrasMaiusculasMinusculasNumerosCaracteresEspeciaisFim)
            senhaFinal.append(senhaForteElementos)
            cont+=1

    elif (tipoSenha == "Média" or tipoSenha == "média" or tipoSenha == "media" or tipoSenha == "Media"):
        while(cont < 6):
            senhaMediaElementos = random.choice(letrasMaiusculasMinusculasNumerosMedia)
            senhaFinal.append(senhaMediaElementos)
            cont += 1

    else:
        while(cont < 4):
            senhaFracaElementos = random.choice(letrasMaiusculasMinusculasFraca)
            senhaFinal.append(senhaFracaElementos)
            cont+=1        
    
    senhaFinal = ''.join(senhaFinal)  
    print("-"*50)  
    print("Sua senha é: " , senhaFinal)
    

def salvaValoresArquivo():
    print("-"*50)
    print("Um arquivo .txt foi criado com a senha que você gerou (Caso você crie novas senhas ele irá salvar também)")
    arquivo = open("senhaGerada.txt", "a")
    arquivo.write(tipoSenha+" --> "+senhaFinal+'\n')
    arquivo.close()


listaAlfabetoNumerosCaracteresEspeciais()
escolhaTipoSenha()
randomizacaoSenha()
salvaValoresArquivo()