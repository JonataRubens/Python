# GeradorDeSenhas
 
Este script Python gera senhas aleatórias com base nos requisitos especificados pelo usuário.

1. **Importações de bibliotecas**:
   - `import random`: Importa o módulo `random`, que fornece funções para gerar números aleatórios.
   - `import string`: Importa o módulo `string`, que fornece constantes úteis para operações com strings, como alfabeto, dígitos e caracteres especiais.

2. **Cabeçalho e Introdução**:
   - Imprime o título do programa: "Gerador de senhas".

3. **Configuração de Parâmetros**:
   - Define uma lista de caracteres válidos para as senhas, que inclui letras maiúsculas (`string.ascii_uppercase`), dígitos (`string.digits`) e letras minúsculas (`string.ascii_lowercase`).
   - Solicita ao usuário o número de senhas que deseja gerar e converte a entrada para um número inteiro (`int()`).
   - Solicita ao usuário o número de letras que deseja em cada senha e converte a entrada para um número inteiro (`int()`).

4. **Geração de Senhas**:
   - Imprime "Senha gerada" para indicar que as senhas estão sendo geradas.
   - Usa um loop `for` para gerar o número especificado de senhas.
   - Dentro desse loop, gera uma senha aleatória para cada iteração:
     - Define uma string vazia `senha` para armazenar a senha.
     - Usa outro loop `for` para adicionar o número especificado de letras à senha:
       - Adiciona uma letra aleatória da lista de caracteres válidos à senha usando `random.choice(lista)`.
     - Imprime a senha gerada.

Este script é útil para gerar senhas aleatórias com diferentes requisitos de comprimento e composição, oferecendo uma maneira simples de criar senhas seguras para uso pessoal ou profissional.
