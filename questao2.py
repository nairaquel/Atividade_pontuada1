import os
os.system("clear||cls")

#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).
#Por fim, mostre os dados do usuário.

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
estado_civil = input("Digite seu estado civil: ")

match estado_civil:
    case "casado":
        tempo_de_casado = input("Tempo de casado(anos): ")
    case "casada":
        tempo_de_casada = input("Tempo de casada(anos): ")
    case _:
        print("Resposta invalida!")

if estado_civil == "casado":
        print(f"Nome: {nome}")
        print(f"Sexo: {sexo}")
        print(f"Estado civil: {estado_civil}")
        print(f"Tempo de casado: {tempo_de_casado}")
else:
        print(f"Nome: {nome}")
        print(f"Sexo: {sexo}")
        print(f"Estado civil: {estado_civil}")
        print(f"Tempo de casada: {tempo_de_casada}")


        
        

