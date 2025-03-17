produto = {
    'Nome': ['feijão','arroz'],
    'Quantidade' : [10,100,1000],
    'preco':[4,5,8,]
    }
for nome, quantidade,preco in zip(produto['Nome'], produto['preco'], produto['preco']):
     print("produto:",nome,"quantidade: ",quantidade, 'preco', preco) 