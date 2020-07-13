import math
ativo = input('informe o ativo que você deseja consultar: ')
print ('você selecionou', ativo)
cotação = input('informe a ultima cotação do ativo: ')
vpa = input('informe o vpa do ativo: ')
lpa = input ('informe o lpa do ativo: ')
print ('usaremos o calculo da formula de graham para analisar o seu ativo')
num = ((float(vpa)*float(lpa))*22.5)
raiz = math.sqrt(num)
print(f'\nO valor intríseco da sua ação é {raiz}\n')
if (float(raiz) > float(cotação)) : print ('segundo a formula de graham o seu ativo esta barato')
if (float(raiz) < float(cotação)) : print ('segundo a formula de graham o seu ativo esta caro!!')

pl = (float(cotação)/float(lpa))
print (f'\nA sua ação esta sendo negociada com um pl de {pl}x\n')
 
