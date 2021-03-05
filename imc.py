print("Olá! para calcular seu IMC, insira os seguintes dados abaixo")

peso = input("Digite seu peso: ")
altura = input("Digite sua altura: ")

IMC = float(peso) / float(altura) ** 2 

print("O seu IMC é de:" ,IMC)