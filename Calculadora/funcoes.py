def somador(x, y):
    resultado_soma = x + y
    print(f'Resultado de {x} + {y} é:', resultado_soma)
    return resultado_soma

def subtrator(x, y):
    resultado_menos = x - y
    print(f'Resultado de {x} - {y} é:', resultado_menos)
    return resultado_menos

def multiplicacao(x, y):
    resultado_multiplicacao = x * y
    print(f'Resultado de {x} * {y} é:', resultado_multiplicacao)
    return resultado_multiplicacao

def divididor(x, y):
    while True:
        try:
            resultado_divididor = x / y
            print(f'Resultado de {x} / {y} é:', resultado_divididor)
            return resultado_divididor
        except ZeroDivisionError:
            print('Divisão por 0 é impossivel')
            return None

def potenciacao(x, y):
    resultado_potenciacao = x ** y
    print(f'Resultado de {x} ** {y} é:', resultado_potenciacao)
    return resultado_potenciacao

def fatorar(x):
    contador = 2
    while x > 1:
        if x % contador == 0:
            print(f'{x} | {contador}')
            x //= contador # Antes x = x //
        else:
            contador += 1
    print('1')

def raiz_de(x):
    if x < 0:
        print('Não é possível calcular a raiz de um numero negativo.')
        return None
    resultado_raiz = x ** 0.5
    if resultado_raiz.is_integer():
        resultado_raiz = int(resultado_raiz)
        print(f'A raiz de {x} é:', resultado_raiz)
    return resultado_raiz

def tabuada(start, *stop):
# # Quantos numeros adiante do inicio    
    if stop == (1,) or not stop:
        stop = 1
    elif stop:
        stop = int(list(stop).pop()) + 1
        if stop < start:
            print('Não posso realizar a operação com um intervalo de fim menor que seu ínicio')
            return None

# Calculo
    for _ in range(stop - start):
        atual = 1
        numero_tabuada = multiplicador(start)
        print(f'Tabuada atual [{start}]')
        for _ in range(10):
            print(f'{atual}. {numero_tabuada(atual)}')
            atual += 1
        start += 1
        print()

def impar_par(x):
    if x % 2 == 0:
        print(f'O número {x} é Par')
    else:
        print(f'O número {x} é Impar')
    return x

def multiplicador(y):
    def multiplica(x):
        resultado = x * y
        return resultado
    return multiplica
