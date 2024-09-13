def bissecao(f, a, b, tol, max_iter):
    fa = f(a)
    fb = f(b)
    
    # Verificando se a e b possuem sinais opostos
    if fa * fb >= 0:
        print("f(a) e f(b) devem ter sinais opostos.")
        return None
    
    dados = []
    
    for n in range(1, max_iter + 1):
        xn = (a + b) / 2
        fxn = f(xn)
        
        dados.append([n, a, b, xn, fxn, abs(fxn)])
        
        if fxn == 0 or abs(fxn) < tol:
            # Raiz encontrada ou tolerância satisfeita
            print(f"A raiz aproximada é {xn} e foi encontrada na iteração {n}.")
            break
        
        if fa * fxn < 0:
            b = xn
            fb = fxn
        else:
            a = xn
            fa = fxn
    
    return xn, dados

# Exemplo de uso:
def funcao_exemplo(x):
    return x**2 - 6

# Intervalo inicial [a, b], tolerância e número máximo de iterações
a = 1
b = 3
tol = 0.01
max_iter = 100

raiz, dados_bissecao = bissecao(funcao_exemplo, a, b, tol, max_iter)

# Mostrar os dados da tabela
for linha in dados_bissecao:
    print("n: {}, a: {:.5f}, b: {:.5f}, xn: {:.5f}, f(xn): {:.5f}, ε: {:.5f}".format(*linha))
