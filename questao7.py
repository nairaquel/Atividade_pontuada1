import os
os.system("clear||cls")

#Faça um algoritmo para ler: a descrição do produto (nome), 
#a quantidade adquirida e o preço unitário. Calcular e escrever o total
#(total = quantidade adquirida * preço unitário), o desconto e o total a pagar 
#(total a pagar = total - desconto), sabendo-se que: 
#- Se quantidade <= 5 o desconto será de 2% 
#- Se quantidade > 5 e quantidade <= 10 o desconto será de 3% 
#- Se quantidade > 10 o desconto será de 5%.


nome_produto = input("Digite o nome do produto:" )
quantia = float(input("Digite a quantidade do produto:" ))
preço = float(input("Digite o preço do produto:" ))

total = quantia * preço

if quantia <= 5:
    desconto = total - (total * 0.02)

elif quantia <= 10:
    desconto = total -(total * 0.03)

else:
    desconto = total - (total * 0.05)


print(f"Nome do produto: {nome_produto}")
print(f"Quantidade:{quantia}")
print(f"Preço{preço}")
print(f"Valor total:{total}")
print(f"Desconto:{desconto:.2f}")
