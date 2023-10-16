gh= float(input('Quanto ganhas por hora? '))
h= float(input('Qual o número de horas trabalhadas no mes?  '))
s= gh*h
ir= s * 0.11
inss= s * 0.08
sindicato= s * 0.05
sl= s - (ir + inss + sindicato)
print(' Salário bruto: {} R$'.format(s))
print('Imposto de Renda: {} R$ '.format(ir))
print('INSS: {} R$'.format(inss ))
print('Sindicato: {} R$ '.format(sindicato))
print('Salário liquido: {} R$'.format(sl))