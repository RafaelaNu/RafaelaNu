'''
faca um jog para o usuario adivinhar qual e a palavra secreta
voce vai propor uma palavra secreta qualquer e vai dar a 
possibilidade para o usuario digitar apenas uma letra.
quando o usuario digitar uma letra, voce vai conferir se a 
letra digitada esta na palavra secreta. se a letra digitada 
estiver na palavra secreta exiba aletra , se a letra digitada 
nao estiver na palavra secretaexiba * , faca a contagem de
tentativas do seu usuario.
'''
import os # para limpar o terminal 

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True :
    
    letra_digitada = input('Digite uma letra') # entrou no laco e digitou qualquer coisa 
    numero_tentativas +=1 # ja comeca a contar nas tentativas 

    if len(letra_digitada) > 1 :
        print(' Digite apenas uma letra : ')
        continue

    if letra_digitada in palavra_secreta :
        letras_acertadas += letra_digitada

    palavra_formada = '' # em toda execucao do while o for checa todo esse laco
    for letra_secreta in palavra_secreta : # esse for seria logica do jogo
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'  

    print(' Palavra formada :' , palavra_formada)

    if palavra_formada == palavra_secreta :
        os.system('cls') # ou clear 
        print(' Voce ganhou !!! parabens!!')
        print(' A palavra era :', palavra_secreta) 
        print('tentativas :' , numero_tentativas) 
        letras_acertadas = ''
        numero_tentativas = 0        


