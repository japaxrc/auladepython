def contar (palavra):
    vogais = 'aeiou'
    conta= 0
    for vogal in palavra:
        if vogal in vogais:
            contar+=1
    return conta
palavra = str (input('digite a palavra'))
print (contar(palavra))

