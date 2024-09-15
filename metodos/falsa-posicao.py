from scipy.stats import norm

def regula_falsi(target_cdf, tolerance=1e-6, a=-10, b=10):
    fa = norm.cdf(a) - target_cdf
    fb = norm.cdf(b) - target_cdf
    
    while abs(b - a) > tolerance:
        c = b - (fb * (a - b)) / (fa - fb)

        fc = norm.cdf(c) - target_cdf 
        
        if abs(fc) < tolerance:
            return c
        elif fc * fb < 0:
            a, fa = b, fb
        b, fb = c, fc
        
    return (a + b) / 2

z_value = regula_falsi(0.05)
print(f"Valor crítico para CDF = 0,05 é aproximadamente: {z_value}")
explique o código
