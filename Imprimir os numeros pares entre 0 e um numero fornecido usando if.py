'''
Imprimir os numeros pares entre 0 e um numero fornecido usando if
'''
numero = int(input("digite um numero: ")) 
x = 0
while x <= numero:
    if x % 2 == 0:
        print (x)
    x = x + 1
