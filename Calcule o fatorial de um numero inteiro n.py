'''
Calcule o fatorial de um numero inteiro n
'''
i = 1
fat = 1
n = int(input("Digite o %d numero: "))
while i <= n:
    fat = fat * i
    i = i + 1
print ("Fat(%d) = %d" %(n, fat))
    
