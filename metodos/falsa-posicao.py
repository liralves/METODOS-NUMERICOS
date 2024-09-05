import math

def funcao(xo):
    return pow(xo, 3) - (9 * xo) + 3

# Solicitação de intervalos e precisão
a = float(input("Intervalo a: "))
b = float(input("Intervalo b: "))
precisao = float(input("Precisao: "))
print('\n')

# Verificação inicial: f(a) e f(b) devem ter sinais opostos
while funcao(a) * funcao(b) >= 0:
    print("Erro: f(a) e f(b) devem ter sinais opostos.")
    a = float(input("Intervalo a: "))
    b = float(input("Intervalo b: "))
    precisao = float(input("Precisao: "))
    print('\n')

k = 1
while True:
    # Cálculo do ponto de interseção
    x = b - (funcao(b) * (b - a)) / (funcao(b) - funcao(a))
    
    print("Iteracao: %d" % k)
    print("Valor de X: %f" % x)
    print("f(x): %f" % funcao(x))
    print("b - a: %f" % (b - a))
    print('\n')
    
    # Verificação do critério de parada
    if abs(funcao(x)) <= precisao or (b - a) <= precisao:
        x1 = x
        break
    
    # Atualização do intervalo
    if funcao(a) * funcao(x) < 0:
        b = x
    else:
        a = x
    
    k += 1

# Resultado final
print('Valor de x1: %f' % x1)