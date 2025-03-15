import os
os.system("clear||cls")

#Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#Escreva um algoritmo que leia o número de litros vendidos e o tipo de 
#combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser 
#pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 6,59 e o preço do litro do álcool é R$ 3,79.

litros = float(input("Número de litros: "))
tipo_combustivel =(input("""
 A \t = \t álcool
 G \t = \t gasolina
Digite o tipo de combustível: """)).upper()

match tipo_combustivel: 
    case "A":   
        calculo1 =3.79 
        if calculo1 <= 25 :
            desconto_alcool = calculo1 - (calculo1 * 0.02)
            total = litros * desconto_alcool
            print(f"VALOR TOTAL:{total:.2f}")
        else: 
            desconto_alcool = calculo1 - (calculo1 * 0.04)
            total = litros * desconto_alcool
            print(f"VALOR TOTAL:{total:.2f}")
    case "G":
        calculo2 = 6.59
        if calculo2 <= 25:
            desconto_gasolina =calculo2 - (calculo2 * 0.03)
            total = litros * desconto_gasolina
            print(f"VALOR TORTAL:{total:.2f}")
        else:
            desconto_gasolina = calculo2 - (calculo2 * 0.05)
            total = litros * desconto_gasolina
            print(f"VALOR TOTAL:{total:.2f}")
    case _: 
        print("OPÇÃO IVÁLIDA!")
