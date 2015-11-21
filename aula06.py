s = float(input('Salario: '))
p = float(input('porcentagem de aumento: '))
aumento = s * p / 100
novo = s + aumento
print('Aumento: R$ %.2f' %aumento)
print('novo Salario: R$ %.2f' %novo)
