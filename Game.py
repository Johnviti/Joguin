from  time import sleep
from random import randint
import os
'''Desafio 05 – Jogo das tentativas
Este desafio tem o intuito de demonstrar como funciona um jogo no qual tem como princípio, fazer com que os jogadores trabalhem a matemática, a história, raciocínio lógico e conhecimentos gerais ao tentar acertar um número gerado de forma aleatória. Nele o programador deve se utilizar de técnicas e comandos vistos em sala de aula para conseguir fazer o que se pede:
- O algoritmo deve solicitar quantos jogadores vão participar. No máximo devem ser 4 jogadores.
- Cada rodada os jogadores dão um palpite com o número que ele achar que é o correto.
- Após cada palpite o programa deve dar uma dica.
Obs: As dicas não podem se repetirem e devem ser realizadas de forma aleatória.
Exemplo(s):
O número é impar.
O número é divisível por 22.
O número está num intervalo de 1 e 1432.
A raiz desse número é maior que 32.
O número é menor do que a idade do descobrimento do Brasil.
O número é maior do que a quantidade de estados brasileiros.
...
- O programa deve permitir apenas até 5 rodadas de palpites e depois informar o resultado.
Obs: Os palpites só devem parar quando alguém acertar ou quando chegar ao limite de 5 rodadas.
- Ao final o programa deve informar quem acertou ou quem chegou mais próximo do número gerado, quantos palpites os jogadores deram para acertar, caso alguém tenha acertado, informar todas as dicas dadas e o número correto. Ao final o programa deve também perguntar se outros jogadores também desejam iniciar um novo jogo.
- Comente o algoritmo para que possamos identificar cada etapa realizada por ele.'''
def dica(number):
  if number > x:
   print("Errado o Numero é menor que X")
number=randint(1,3000)
print(number)
print(f"            ","-="*7)
print(f"            ","¦  Bem Vindo ¦")
print(f"            ","-="*7)
print("-"*50)
print("Venha se divertir, com nosso joguin de adivinhação")
print("_"*50)
x=int(input("Qual a quantidade de jogadores: "))
i=0
if x==2:
  jodador1=input("Digite seu nick: ")
  sleep(1)
  jogador2=input("Digite seu nick: ")
  sleep(3)
  os.system("cls")
  print("Vcs estão prontoss....")
  sleep(4)
  print("hummm.............................")
  sleep(2)
  print("Vou pensar um número! Sera que vc consegue adivinha?")
  sleep(4)
  
  while i<=x: 
    i+=1
    if i==1:   
     xjogador1=int(input("Opa "+jodador1+ ", Qual numero vc acha que é: "))
     sleep(1)
    if i==2:
     xjogador2=int(input("Opa "+jogador2+ ", Qual numero vc acha que é: "))
if x==3:
  jodador1=input("Qual seu nick: ")
  jogador2=input("Qual seu nick: ")
  jodagor3=input("Qual seu nick: ")
if x==4:
  jodador1=input("Qual seu nick: ")
  jogador2=input("Qual seu nick: ")
  jodagor3=input("Qual seu nick: ")
  jodador4=input("Qual seu nick: ")
  
