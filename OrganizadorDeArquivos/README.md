# OrganizadorDeArquivos

Este script em Python organiza arquivos em uma pasta com base em suas extensões.

1. **Importações de bibliotecas**:
   - `import os`: Importa o módulo `os`, que fornece funções para interagir com o sistema operacional, como manipulação de arquivos e diretórios.
   - `import shutil`: Importa o módulo `shutil`, que fornece operações de alto nível em arquivos, como copiar, mover e excluir.

2. **Função `organizar_arquivos`**:
   - Recebe o caminho da pasta como argumento.
   - Verifica se o caminho da pasta existe. Se não existir, imprime uma mensagem indicando que a pasta não existe e retorna.
   - Percorre todos os arquivos na pasta usando `os.listdir(caminho_pasta)`.
   - Para cada arquivo, obtém o caminho completo do arquivo usando `os.path.join(caminho_pasta, filename)`.
   - Verifica se o caminho representa um arquivo usando `os.path.isfile(filepath)`.
   - Obtém a extensão do arquivo usando `os.path.splitext(filename)` e cria uma pasta para essa extensão se ainda não existir.
   - Move o arquivo para a pasta correspondente usando `shutil.move(filepath, os.path.join(pasta_destino, filename))`.
   - Imprime uma mensagem indicando que o arquivo foi movido para a pasta correspondente.

3. **Bloco `if __name__ == "__main__"`**:
   - Define o caminho da pasta que deseja organizar.
   - Chama a função `organizar_arquivos` passando o caminho da pasta como argumento.

Este script é útil para organizar arquivos em uma pasta de acordo com suas extensões, facilitando a visualização e o gerenciamento dos arquivos.
 
