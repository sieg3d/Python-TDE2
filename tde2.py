#1.Faça um Programa que leia três números inteiros e mostre o maior deles.

'''
numero_1 = int(input('Digite o primeiro número:'))
numero_2 = int(input('Digite o segundo número:'))
numero_3 = int(input('Digite o terceiro número:'))

if numero_1 > numero_2 and (numero_1 > numero_3):
    print(f'O maior número digitado é: {numero_1}')
elif numero_2 > numero_1 and (numero_2 > numero_3):
    print(f'O maior número digitado é: {numero_2}')
elif numero_3 > numero_1 and (numero_3 > numero_2):
    print(f'O maior número digitado é: {numero_3}')
'''


'''
#2. Crie um código em python que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo
#b) a soma do triplo do primeiro com o terceiro
#c) o terceiro elevado ao cubo

num_int_1 = int(input('Digite o primeiro número inteiro:'))
num_int_2 = int(input('Digite o segundo número inteiro:'))
num_real = float(input('Digite o número real:'))

print(f'O produto do dobro do primeiro com metade do segundo é: {(num_int_1*2)/(num_int_2/2):.2f}')
print(f'A soma do triplo do primeiro com o terceiro é: {(num_int_1*3)+num_real}')
print(f'O terceiro elevado ao cubo é: {num_real**3}')
'''


'''
#3. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#● C = 5 * ((F-32) / 9)

fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
celsius = 5*((fahrenheit-32)/9)
print(f'A conversão de {fahrenheit}° Fahrenheit é {celsius:.1f}° Celsius')
'''
'''
#4. Faça um programa que sorteia um número de 0 a 9999 e mostre na tela cada um dos dígitos separadamente.exemplo: unidade: 4 dezena: 3 centena: 8 milhar

import random
sorteio = random.randint(0,10000)
print(sorteio)
milhar = sorteio//1000
centena = sorteio//100%10
dezena = sorteio//10%10
unidade = sorteio//1%10

print(f'\nUnidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
'''

'''
#5. Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que foi multado. A multa vai custar R$7,00 por cada KM acima do limite.

velocidade = int(input('Insira a velocidade: '))
multa = 7.0
valor = 0

if velocidade > 80:
    print('Você foi multado!')
    valor = multa*(velocidade-80)
    print(f'Você deverá pagar R${valor:.2f} pelos {velocidade-80}km acima da velocidade')
else:
    print('Você está dentro do limite de velocidade.')
'''

'''
#6. Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.

ano = int(input('Digite o ano: '))

if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
    print('É ano bissexto!')
else: print('Não é bissexto')
'''

'''
#7. Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

n_1 = float(input('Digite o primeiro número:'))
n_2 = float(input('Digite o segundo número:'))
n_3 = float(input('Digite o terceiro número:'))

menor = min(n_1, n_2, n_3)
maior = max(n_1, n_2, n_3)

print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}.')
'''

'''
#8. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de
#10%. Para os inferiores ou iguais, o número é de 15%.

salario_base = float(input('Insira o salário bruto do colaborador: '))
aumento = 0
if salario_base > 1250:
    aumento = salario_base * 0.1
    print(f'O salário do colaborador é R${salario_base:.2f} e seu aumento será de R${aumento:.2f} totalizando R${(salario_base + aumento):.2f}.')
else:
    aumento = salario_base * 0.15
    print(f'O salário do colaborador é R${salario_base:.2f} e seu aumento será de R${aumento:.2f} totalizando R${(salario_base + aumento):.2f}.')
'''
'''
# 9. Crie um código em python que peça os 3 lados de um triângulo. O script deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
lado_1 = float(input('Insira um lado do triangulo: '))
lado_2 = float(input('Insira o segundo lado do triangulo: '))
lado_3 = float(input('Insira o terceiro lado do triangulo: '))

if lado_1 == 0 and lado_2 == 0 and lado_3 == 0: 
    print('Não é um triangulo')
elif ((lado_1 == lado_2) and lado_1 != lado_3) or ((lado_1 == lado_3) and lado_1 != lado_2) or ((lado_2 == lado_3) and lado_3 != lado_1):
    print('Possui dois lados iguais e um diferente. Logo é um triangulo isóceles.')
elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
    print('Possui tres lados diferentes. Logo é um triangulo escaleno.')
else:
    print('Os lados são iguais, portanto é um triangulo equilátero.')
'''

'''
#10. Escreva um programa usando while que leia a capacidade de um elevador e o peso de 5 pessoas. Informar se o elevador está liberado para subir ou se excedeu a carga máxima.
peso_atual = 0
qtd_pessoas = 0
peso_max = float(input('Qual o peso máximo suportado? '))
while qtd_pessoas < 5 and peso_atual <= peso_max:
    peso_pessoa = float(input(f'Qual o peso da pessoa {qtd_pessoas+1}? '))
    qtd_pessoas +=1
    peso_atual += peso_pessoa
    if qtd_pessoas == 5 and peso_atual <= peso_max:
        print(f'Atingiu a quantidade máxima de pessoas. O peso atual é: {peso_atual:.2f}.\nLiberado para subir/descer!')
    elif peso_atual == peso_max:
        print(f'Atingiu a o peso máximo suportado. O peso atual é: {peso_atual:.2f}Kg com o total de {qtd_pessoas} pessoas.\nLiberado para subir/descer!')
    elif peso_atual > peso_max:
        print(f'A capacidade máxima é {peso_max}Kg e no momento está com {peso_atual}Kg.\nElevador não liberado para subir/descer.')
'''

#11. Desafio: Faça um script que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O script deverá pedir os valores de a, b e c e fazer os testes necessários.

import math 

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))