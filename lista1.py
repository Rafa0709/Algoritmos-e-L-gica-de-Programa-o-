#1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números

print('LISTA 1 \n')

print('1º\n')
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print(f'Soma = {valor1 + valor2}')

#2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
print('\n---------------------')

print('2º\n')
valor = float(input('Digite o valor em metros: '))
print(f'O valor em mm eh {valor*1000}mm')

#3) Escreva um programa que leia a quantidade de dias, horas,
#minutos e segundos do usuário. Calcule
#o total em segundos.
print('\n---------------------')

print('3º\n')
dias = int(input('Digite os dias: '))
dias = dias*86400

horas = int(input('Digite as horas: '))
horas = horas*3600

minutos = int(input('Digite os minutos: '))
minutos = minutos*60

segundos = int(input('Digite os segundos: '))

total = dias + horas + minutos + segundos
print(f'O total de horas sera: {total}hrs')

#4
print('\n---------------------')

print('4º\n')
salario = float(input('Digite o salario: '))
aumento = float(input('Digite a porcentagem do aumento: '))

valorAumento = (salario*aumento/100)
novoSalario = salario + valorAumento

print(f'o aumento foi de: {valorAumento}R$')
print(f'o novo salário eh de: {novoSalario}R$')

#5
print('\n---------------------')

print('5º\n')
preco = float(input('Digite o preco da mercadoria: '))
desconto = float(input('Digite o percentual de desconto: '))

valorDesconto = preco*desconto/100
novoPreco = preco - valorDesconto

print(f'o desconto foi de: {valorDesconto}R$')
print(f'o preco a se pagar sera de: {novoPreco}R$')

#6
print('\n---------------------')

print('6º\n')
distancia = float(input('Digite a distancia em km: '))
velocidade = int(input('Digite a velocidade media em km/h: '))

tempo = distancia/velocidade

print(f'o tempo sera de: {tempo}hrs')

#7
print('\n---------------------')

print('7º\n')
tempC = float(input('Digite a temperatura em Celsius: '))
temF = (9*tempC/5)+32
print(f'a temperatura em Fahrenheit eh: {temF}F')

#8
print('\n---------------------')

print('8º\n')
tempF = float(input('Digite a temperatura em Fahrenheit: '))
tempC = (tempF-32)*5/9
print(f'a temperatura em Celsius eh: {tempC}C')

#9
print('\n---------------------')

print('9º\n')
qntdKm = int(input('Digite a quantidade de KM rodados: '))
qntdDias = int(input('Digite a quantidade de dias que foi alugado: '))

custoDia = qntdDias*60.00
custoKm = qntdKm*0.15
preco = custoDia + custoKm

preco = print(f'O preco a pagar sera de: {preco}R$')

#10
print('\n---------------------')

print('10º\n')
cigarroDia = int(input('Digite quantos cigarros fuma por dia: '))
anos = int(input('Digite quantos anos ja fumou: '))

cigarrosFumados = cigarroDia*anos*365
tempoPerdido = cigarrosFumados*10

print(f'O tempo perdido será de: {tempoPerdido/1440}dias')

#11
print('\n---------------------')

print('11º\n')
print('esse nao deu certo')
#print(len(str(2**1000000)))














































