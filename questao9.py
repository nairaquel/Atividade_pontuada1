import os
os.system("clear||cls")

#Uma financeira usa o seguinte critério para conceder empréstimos: o valor total do empréstimo deve 
#ser até dez vezes o valor da renda mensal do solicitante e o valor da prestação deve ser no máximo 30% da renda mensal do solicitante.
#Escreva um programa que leia a renda mensal de um solicitante, o valor total do 
#empréstimo solicitado e o número de prestações que o solicitante deseja pagar e informe se o empréstimo pode ou não ser concedido.


renda = float(input("Digite sua renda mensal: "))
emprestimo = float(input("Digite o valor do empréstimo: "))

calculo_da_renda = renda * 10
prestacao = renda * 0.3

if emprestimo > calculo_da_renda :
    print("Empréstimo negado!") 
    
else:
    parcela = int(input("Digite o valor das parcelas: "))
    calculo_parcela = emprestimo /parcela
    if calculo_parcela > prestacao: 
        print("Empréstimo negado!") 
    else:
      
        print("Empréstimo aceito!")
        print(f"RENDA:{renda}")
        print(f"EMPRÉSTIMO:{emprestimo}")
        print(f"PARCELA:{parcela}")
        print(f"VALOR DAS PARCELAS:{calculo_parcela:.2f}")
