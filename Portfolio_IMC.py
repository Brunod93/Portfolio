#O cálculo é feito da seguinte forma: divide-se o peso (em kg) pelo quadrado da altura (em metros).
# IMC = Peso / Altura²
# RESULTADO	SITUAÇÃO
# Abaixo de 17	Muito abaixo do peso
# Entre 17 e 18,49	Abaixo do peso
# Entre 18,5 e 24,99	Peso normal
# Entre 25 e 29,99	Acima do peso
# Entre 30 e 34,99	Obesidade I
# Entre 35 e 39,99	Obesidade II (severa)
# Acima de 40	Obesidade III (mórbida)


print('Calcule seu IMC')

# 1º Definição do Loop para evitar que o usuário digite um número inválido.

while True:
    try:
        Peso = float(input('\nQual seu peso? ').strip())
        Altura = float(input('\nQual sua altura? ').strip())
        break
    except ValueError:
        print('ERRO: Utilize ponto ao invés de virgula.')

#2º Cálculo do IMC e definição da estrutura condicional

IMC = Peso/Altura**2
print('\nSeu IMC é {:.2f} '.format(IMC))

if(IMC<17.00):
    print('Você está muito abaixo do peso.')
elif(IMC>=17.00)and(IMC<=18.49):
    print('Você está abaixo do peso.')
elif(IMC>=18.50)and(IMC<=24.99):
    print('Você está no peso normal.')
elif(IMC>=25.00)and(IMC<=29.99):
    print('Você está acima do peso.')
elif(IMC>=30.00)and(IMC<=34.99):
    print('Você está com Obesidade I.')
elif(IMC>=35.00)and(IMC<=39.99):
    print('Você está com Obesidade II. (severa)')
elif(IMC>=40.00):
    print('Você está com Obesidade III. (mórbida)')
