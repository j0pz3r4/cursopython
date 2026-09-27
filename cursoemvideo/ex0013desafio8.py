#APLICATIVO QUE LE O PREÇO DO PRODUTO E DEVOLVE ELE COM DESCONTO DE 5%

print ('//DESCONTO NA COMPRA//')
n1 = float(input('Qual o valor do produto?:'))
desconto = n1 - (n1 * 0.05)
preco_final = n1 - desconto
print ('O desconto do produto e de',desconto,'reais','PREÇO FINAL:',preco_final)