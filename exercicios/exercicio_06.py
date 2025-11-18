'''Exercícios das aulas 7.1, 7,2 e 7.3
1- faça um programa que receba um número, verifica se o número informado
é par ou ímpar e exiba o resultado da seguinte maneira:
O número x é ímpar ou o número x é par.
'''
#%%
def par_ou_impar(numero: int):
    """par_ou_ímpar: Fuma função que verifica se um número é par ou ímpar.

    Args:
        numero (int): representa um número inteiro.

    Returns:
        string: retorna uma string que verifica a condição do número.
    """
    if numero % 2 == 0:
        # print(f"{numero} é par!") | Outra forma de fazer
        return "par"
    else:
        # print(f"{numero} é ímpar!") | Outra forma de fazer
        return "ímpar"

# Entrada do usuário
numero = input("Entre com um número: ")
numero = int(numero)
resultado = par_ou_impar(numero)

print(f"O número {numero} é {resultado}!")

# Esta função retorna uma string!