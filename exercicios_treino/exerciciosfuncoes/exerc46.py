# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverte(valor):
    novo_valor = str(valor)
    print(novo_valor[::-1])





reverte(1564)


# # python 3.x
# original_number = int(input("Enter an integer: "))
# copy_number = original_number
# reversed_number = 0
# while original_number > 0:
#     remainder = original_number % 10
#     reversed_number = reversed_number * 10 + remainder
#     original_number = original_number // 10
# if copy_number == reversed_number:
#     print(copy_number, "is a palindrome number")
# else:
#     print(copy_number, "is not a palindrome number")