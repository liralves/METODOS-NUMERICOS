from scipy.stats import norm

def newton_raphson(target_cdf, tolerancia=1e-6, chute_inicial=0):
    x = chute_inicial
    while True:
        valor_cdf = norm.cdf(x)
        valor_pdf = norm.pdf(x)
        x_novo = x - (valor_cdf - target_cdf) / valor_pdf
        if abs(x_novo - x) < tolerancia:
            return x_novo
        x = x_novo

# Exemplo de uso
valor_critico = newton_raphson(0.05)
print(f"Valor crítico para CDF = 0,05 é aproximadamente: {valor_critico}")
