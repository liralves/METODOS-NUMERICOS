from scipy.stats import norm

def bisseccao(target_cdf, tolerance=1e-6, a=-10, b=10):
    fa = norm.cdf(a) - target_cdf
    fb = norm.cdf(b) - target_cdf
    
    if fa * fb > 0:
        raise ValueError("Os valores de f(a) e f(b) devem ter sinais opostos.")
    
    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        fc = norm.cdf(c) - target_cdf
        
        if abs(fc) < tolerance:
            return c
        elif fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
            
    return (a + b) / 2

z_value = bisseccao(0.05)
print(f"Valor crítico para CDF = 0,05 é aproximadamente: {z_value}")
