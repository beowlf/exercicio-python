'''
    Fazendo uma refra de três chegamos que 144 cigarros tiram 1 dia
    de vida da pessoa (1 dia = 1440 minutos = 144 cigarros)
'''
cigarros = int(input('Cigarro por dia: '))
anos = int(input('Anos fumados: '))
total_cigarros = anos * 365 * cigarros
dias_perdidos = total_cigarros / 144
print ('Você perdeu aproximadament %.2f dias' %dias_perdidos)
