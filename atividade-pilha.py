def inverter_string(palavra):
    pilha = []

    for caractere in palavra:
        pilha.append(caractere)

    invertida = ""

    while pilha:
        invertida += pilha.pop()

    return invertida

entrada = "ALGORITMO"
print(inverter_string(entrada))