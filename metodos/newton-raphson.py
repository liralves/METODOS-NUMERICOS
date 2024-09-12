import sympy as sp

def newton_raphson(expressao, x0, tolerancia, max_iter):
    x = sp.Symbol('x')
    derivada = sp.diff(expressao, x)
    
    f_numerica = sp.lambdify(x, expressao)
    df_numerica = sp.lambdify(x, derivada)
    
    x_atual = x0
    for _ in range(max_iter):
        f_valor = f_numerica(x_atual)
        df_valor = df_numerica(x_atual)
        
        if df_valor == 0:
            print("Derivada zero. Não é possível continuar.")
            return None
        
        x_proximo = x_atual - f_valor / df_valor
        
        if abs(x_proximo - x_atual) < tolerancia:
            print(f"Solução encontrada: {x_proximo}")
            return x_proximo
        
        x_atual = x_proximo

    print("Número máximo de iterações atingido.")
    return x_atual

x = sp.Symbol('x')

expressao = x**3 - 9*x + 3

x0 = 2.0
tolerancia = 1e-6
max_iter = 100

raiz = newton_raphson(expressao, x0, tolerancia, max_iter)
print(f"Raiz aproximada: {raiz}")
