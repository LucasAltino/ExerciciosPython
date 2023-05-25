valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite o valor da taxa: "))
tempo = int(input("Digite o tempo: "))

prestação = valor + (valor * (taxa/100) * tempo)

print("O valor da prestação em atraso será de:", prestação)