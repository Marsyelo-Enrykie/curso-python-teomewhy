'''Exercícios da aulas 02.1 e 02.2
1- Faça um programa que dê bom dia.
2- Faça um programa que dê bom dia, pergunte o nome da pessoa e responda que é um prazer conhecer ela, citando seu nome.
3- Crie uma história simples. Adicione essa história em um programa.a A cada parágrafo, a história deve aguardar o usuário aperta "enter" para dar continuidade.
4- Faça um programa que receba um número inteiro e calcule a sua raiz quadrada e exiba o resultado.
5- faça um programa que exiba o dobro de um número inserido pelo usuário.
'''
#%%
# Questão 1
print("Bom dia!")

#%%
# Questão 2
print("Bom dia!")
nome = input("Qual é o seu nome? ")
print(f"É um prazer te conhecer, {nome}!")

#%%
# Questão 3
p1 = "Era uma vez, um menino que amava tecnologia."
input()
p2 = "Ele encontrou um computador quebrado e decidiu explorar"
input()
p3 = "O menino aprendeu a consertar o computador quebrado, então os pais perceberam que ele tem o jeito."
input()
p4 = "Assim, o menino foi seguindo essa área de informática até se tornar um cientista da computação."
input()

#%%
# Questão 4
numero = input("Digite um número: ")
numero = int(numero)
raiz_Quadrada = numero ** (1/2)
print(f"A raiz quadrada de {numero} é {raiz_Quadrada}!")

#%%
# Questão 5
number = input("Digite um numero: ")
number = int(number)
dobro = number * 2
print(f"O dobro de {number} é {dobro}!")