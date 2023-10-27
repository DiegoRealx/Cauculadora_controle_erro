while True:
    numero = input('Digite um numero: ')
    numero1 = input('Digite um numero: ')
    operador = input('Digite um operador: ')

    numeros_validos = None

    num_flot = 0 
    num_flot1 = 0
    operador_validos = '+-/*'

    try:
        num_float = float(numero)
        num_float1 = float(numero1)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos is None:
        print('Um ou ambos numeros são invalidos')
        continue
    if operador not in operador_validos:
        print('Operador invalido. ')
        continue
    if len(operador)>1:
        print('Digite apenas um operador. ')
        continue

    if operador == '+':
            print(f'A soma entre {numero} e {numero1} é ', num_float + num_float1 )
    elif operador == '-':
         print(f'A subtração entre {numero} e {numero1} é', num_float - num_float1 )
    elif operador == '*':
         print(f'A mulplicação emtre {numero} e {numero1} é', num_float * num_float1)
    elif operador == '/':
         print(f'A divisão entre {numero} e {numero1} é ', num_float / num_float1)
    else: 
        print('impossiel chegar aqui')

    sair = input('Digite [S]im para Sair: ').lower()
    
    if sair == 's':
        print()
        print('Fim')
        break
   


