premios = [1000,5000,10000,30000,50000,100000,300000,500000,1000000]
p_acumulado = []
x=0
for p in premios:
    x += p
    p_acumulado.append(x)
