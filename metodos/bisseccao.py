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
    

# Início do método da bisseção
if (b - a) < precisao:
    x1 = a
else:
    k = 1
    M = funcao(a)
    while True:
        x = (a + b) / 2
        print("Iteracao: %d" % k)
        print("Valor de X: %f" % x)
        print("f(x): %f" % funcao(x))
        print("b - a: %f" % ((b - a) / 2))
        print('\n')
        
        # Atualização do intervalo
        if M * funcao(x) > 0:
            a = x
        else:
            b = x
        
        # Critério de parada: intervalo pequeno ou f(x) próximo de zero
        if abs(funcao(x)) <= precisao or (b - a) <= precisao:
            x1 = x
            break
        
        k = k + 1

# Resultado final
print('Valor de xBarra: %f' % x1)
