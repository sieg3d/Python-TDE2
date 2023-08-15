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


#8. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de
#10%. Para os inferiores ou iguais, o número é de 15%.