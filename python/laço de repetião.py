quantidadeImpares = 0
quantidadePares = 0
#declarar as variaveis 
for i in range(5):
    numero = int(input("informe o numero: \n"))
                 
    if numero % 2 == 0:
        quantidadePares = quantidadePares + 1

    else:
        quantidadeImpares = quantidadeImpares + 1
print(f"quantidade de pares: {quantidadePares}")
print(f"quantidade de impares: {quantidadeImpares}")