'''
Faça um programa que leia tres numeros e mostre o maior deles
'''
a = int(input('Primeiro: '))
b = int(input('SEgundo: '))
c = int(input('Terceiro: '))

if a >= b and a >= c:
    print ('Primeiro: %d' %a)
elif b >= c:
    print ('Primeiro: %d' %b)
else:
    print ('Primeiro: %d' %c)
