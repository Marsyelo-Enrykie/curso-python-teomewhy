'''Exercício da aula 05.1
1- Escreva um programa que receba uma lsita de números do usuário e conte quantas vezes o número específico aparece na lista.
Solicite ao usuário um número e exiba a contagem
'''

#%%

lista = [1,2,3,3,1,2,1,2,5,5,6,4,7,6]

numero = input("Entre com um número")
numero = int(numero)

contador = 0
for percorrer_lista in lista:
    if percorrer_lista == numero:
        contador += 1
print(f"Quantidade de {numero}: {contador}x")