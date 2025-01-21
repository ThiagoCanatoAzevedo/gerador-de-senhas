# Gerador de Senhas - Projeto em Python

Este projeto é um gerador de senhas aleatórias em Python que permite ao usuário criar senhas de diferentes níveis de segurança: **fraca**, **média** ou **forte**. O programa cria a senha conforme o tipo escolhido e salva a senha gerada em um arquivo de texto chamado `senhaGerada.txt`.

## Funcionalidades

- O usuário pode escolher o tipo de senha: **fraca**, **média** ou **forte**.
  - **Senha fraca**: Apenas letras minúsculas e maiúsculas.
  - **Senha média**: Letras minúsculas, maiúsculas e números.
  - **Senha forte**: Letras maiúsculas e minúsculas, números e caracteres especiais.
  
- O programa gera a senha de forma aleatória, com um tamanho que depende do tipo de senha escolhido.
  
- A senha gerada é salva em um arquivo de texto (`senhaGerada.txt`), e caso o usuário gere mais senhas, elas serão adicionadas ao arquivo.

## Como usar

1. **Clone o repositório:**

   Primeiro, faça o clone do repositório para o seu computador:

   ```bash
   git clone https://github.com/ThiagoCanatoAzevedo/Gerador-de-senhas
   ```

2. **Instale o Python:**
   O código foi escrito em Python, portanto, você precisará do Python instalado em seu computador. Você pode baixar e instalar o Python em https://www.python.org/downloads/.

3. **Execute o script:**
   Navegue até o diretório do projeto e execute o script Python:
   ```bash
   cd Gerador-de-senhas
   python index.py
