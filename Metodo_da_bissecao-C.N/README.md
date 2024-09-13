# Motodo da bisseçãoC.N


Este script Python realiza a bisseção de uma função para encontrar suas raízes e inclui funções para plotar a função e a raiz encontrada.
1. **Importações de Bibliotecas:**
   - `import numpy as np`: Importa a biblioteca NumPy, que fornece suporte para arrays e funções matemáticas.
   - `import matplotlib.pyplot as plt`: Importa a biblioteca Matplotlib, que é usada para criar visualizações gráficas.

2. **Função `bissecao(f, a, b, tol, max_iter)`:**
   - Implementa o método da bisseção para encontrar uma raiz da função `f` no intervalo `[a, b]`.
   - `f`: A função cuja raiz está sendo encontrada.
   - `a`, `b`: Os limites do intervalo onde a raiz está localizada.
   - `tol`: A tolerância desejada para a raiz.
   - `max_iter`: O número máximo de iterações permitidas.
   - Retorna a raiz encontrada e uma lista de dados contendo informações sobre cada iteração.

3. **Função `funcao_exemplo(x)`:**
   - Define uma função de exemplo para ser usada no método da bisseção.

4. **Função `plotar_funcao_e_raiz(f, a, b, raiz, dados)`:**
   - Plota a função `f` no intervalo `[a, b]`.
   - `raiz`: A raiz encontrada pela bisseção.
   - `dados`: Uma lista de dados contendo informações sobre cada iteração da bisseção.

5. **Variáveis e Execução do Script:**
   - Define os parâmetros para a bisseção: intervalo `[a, b]`, tolerância `tol` e número máximo de iterações `max_iter`.
   - Chama a função `bissecao` com a função de exemplo, intervalo, tolerância e número máximo de iterações.
   - Se uma raiz é encontrada, imprime os dados de cada iteração e plota a função com a raiz destacada.
   - Se a raiz não é encontrada, imprime uma mensagem indicando isso.

Este script demonstra o método da bisseção para encontrar raízes de funções e fornece uma visualização gráfica da função e da raiz encontrada.
