import random

# Declarando variaveis para impressão dos desenhos ascii
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Entrada com a opção do usuário
usuario = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura. \n"))
# Gerando um valor aleatório entre 0 e 2 através do Random para servir como opção do computador
computador = random.randint(0,2)
imagens = [pedra, papel, tesoura]

# Lógica condicional para determinar vitória, derrota ou empate 
# e impressão da arte ASCII de cada opção atribuida e o resultado
if usuario >= 3 or usuario < 0:
    print("Você digitou um número inválido. Você perdeu")
else:
    print(f"Você:{imagens[usuario]}\nComputador:{imagens[computador]}")
    if usuario == 0 and computador == 2:
        print("Você ganhou!")
    elif usuario == 2 and computador == 0:
        print("Você perdeu!")
    elif usuario > computador:
        print("Você ganhou!")
    elif computador > usuario:
        print("Você perdeu")
    elif usuario == computador:
        print("Empate")
