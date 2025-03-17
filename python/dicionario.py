produto = {
    'nome':'feijão',
    'quantidade' : 10
}
#produto é dicíonario
for chave, valor in produto.items():
   print(chave,valor)

produto['quantidade'] = 100

nome = produto ['nome']

#só será chamado dicionario la de cima

quantidade = produto['quantidade']
print ("nome:", nome)
print ('quantidade: ', quantidade)
#sera feita a impressão do dicionário
 