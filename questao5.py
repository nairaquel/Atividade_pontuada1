import os
os. system("clear||cls")

#Faça um programa que leia um código de operação (+,-,* ou /), e também dois valores inteiros A e B. 
#O programa deve calcular o resultado da operação escolhida aplicado a A e B. Por exemplo, 
# se a operação escolhida foi * e A = 1 e B = 3, o programa deve fornecer como resultado o valor de 1*3, que é 3.


primeiro_numero = int(input("Digite o primeiro número: "))
operador = input("Digite a operação desejada(+ - * /):")
segundo_numero = int(input("Digite o segundo número: "))


match operador: 
    case "+":
        RESULTADO = primeiro_numero + segundo_numero
    case "-":
        RESULTADO = primeiro_numero - segundo_numero
    case "*":
        RESULTADO = primeiro_numero * segundo_numero
    case "/":
        RESULTADO = primeiro_numero / segundo_numero
    case _:
        RESULTADO = "OPÇÃO INVÁLIDA!"

print(f"\nprimeiro número:{primeiro_numero}")
print(f"operação: {operador}")
print(f"segundo número: {segundo_numero}")
print(f"Resultado: {RESULTADO}")
