'''
Calcule a soma de numero inteira ate ser digitado zero
'''
soma = 0
while True:
    x = int(input("Digite um numero (0 sai): "))
    if x == 0:
        break
    soma = soma + x
print ("Soma: %d" %soma)
