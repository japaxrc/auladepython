valor = float(input("valor da casa:"))
quantidade = int(input('insiraa quantidade de t-shift: '))
# condição para os descontos 
if quantidade < 20:
    desconto = 0
elif quantidade < 20:
    desconto = 0.1
else:
    desconto - 0.2
    # Parametros para os valores 
valor_sem_desconto = quantidade*valor
valor_com_desconto = valor *(1-desconto)   
valor_total = quantidade * valor_com_desconto
porcentagem_desconto = desconto * 100
# saída dos dados 
print(f'valor total sem desconto:', valor_com_desconto)
print(f'valor unitario: R${valor:.2f}')
print(f'valor com desconto: R$ {valor_total:.2f}({porcentagem_desconto:of}%desconto)')
print(f'valor total: R$ {valor_total:.2f} (desconto total: R${valor_desconto:.2f})')