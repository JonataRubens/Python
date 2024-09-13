# Dicionario
 
Este script Python implementa um programa simples de pesquisa em um dicionário de palavras e seus significados.

1. **Função `pesquisador(nome_buscado)`**:
   - Abre o arquivo 'significados.txt' em modo de leitura.
   - Lê todas as linhas do arquivo e percorre cada linha.
   - Divide cada linha em partes usando ':' como separador.
   - Verifica se a linha tem pelo menos duas partes.
   - Converte a chave (a primeira parte) para minúsculas e remove espaços em branco.
   - Junta as partes restantes (o valor) de volta em uma string.
   - Se a chave corresponder ao nome buscado (também convertido para minúsculas), retorna o valor correspondente.
   - Se a palavra não for encontrada, retorna a mensagem "Palavra não encontrada no dicionário."
   - Lida com exceções como FileNotFoundError e qualquer outra exceção genérica, retornando mensagens de erro apropriadas.

2. **Loop de Menu Principal**:
   - Inicia um loop `while` que continuará até que a opção digitada seja 0 (sair).
   - Imprime as opções do menu: "1- pesquisar por nome" e "0- sair".
   - Solicita ao usuário que digite sua opção.
   - Se a opção for 0, o loop é interrompido.
   - Se a opção for 1, o usuário é solicitado a inserir o nome da palavra que deseja buscar o significado.
   - Chama a função `pesquisador` com o nome buscado e imprime o resultado retornado pela função.

Este programa oferece uma maneira simples de buscar o significado de palavras em um dicionário de texto e fornece uma interface de usuário básica para interação.
