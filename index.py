import string
import random
import os

def lista_alfabeto_numeros_caracteres_especiais():
    """Função que define os elementos que podem ser usados para gerar a senha."""
    letras_maiusculas = list(string.ascii_uppercase)
    letras_minusculas = list(string.ascii_lowercase)
    caracteres_especiais = ['!', '@', '#', '$', '%', '&', '-', '*', '_', '+', '=', '§', '?', '/', '|', '*', '.', ',']
    numeros = [str(i) for i in range(10)]  # Geração de números de 0 a 9
    
    return letras_maiusculas, letras_minusculas, caracteres_especiais, numeros


def escolha_tipo_senha():
    """Função para que o usuário escolha o tipo de senha que deseja gerar."""
    print("Você gostaria de uma senha fraca, média ou forte? Digite '+' para saber o que cada tipo possui.")
    tipo_senha = input().strip().lower()

    if tipo_senha == "+":
        print("""
        Aqui vai o que cada uma faz:
        Fraca: Apenas letras minúsculas e maiúsculas
        Média: Letras minúsculas, maiúsculas e números
        Forte: Possui tudo. Letras maiúsculas e minúsculas, números e caracteres especiais
        """)
        tipo_senha = input("Agora, escolha uma opção (Fraca, Média ou Forte): ").strip().lower()

    return tipo_senha


def randomizacao_senha(tipo_senha, letras_maiusculas, letras_minusculas, numeros, caracteres_especiais):
    """Função que gera a senha aleatória conforme o tipo escolhido."""
    senha_final = []
    letras_maiusculas_minusculas_fraca = letras_maiusculas + letras_minusculas
    letras_maiusculas_minusculas_numeros_media = letras_maiusculas_minusculas_fraca + numeros
    letras_maiusculas_minusculas_numeros_caracteres_forte = letras_maiusculas_minusculas_numeros_media + caracteres_especiais

    if tipo_senha == "forte":
        lista_de_elementos = letras_maiusculas_minusculas_numeros_caracteres_forte
        tamanho_senha = 8
    elif tipo_senha == "média":
        lista_de_elementos = letras_maiusculas_minusculas_numeros_media
        tamanho_senha = 6
    else:
        lista_de_elementos = letras_maiusculas_minusculas_fraca
        tamanho_senha = 4

    for _ in range(tamanho_senha):
        senha_final.append(random.choice(lista_de_elementos))

    senha_final = ''.join(senha_final)
    return senha_final


def salva_valores_arquivo(tipo_senha, senha_final):
    """Função para salvar a senha gerada em um arquivo de texto."""
    with open("senhaGerada.txt", "a") as arquivo:
        arquivo.write(f"{tipo_senha.capitalize()} --> {senha_final}\n")


def main():
    os.system('cls')  # Limpa o terminal

    letras_maiusculas, letras_minusculas, caracteres_especiais, numeros = lista_alfabeto_numeros_caracteres_especiais()

    tipo_senha = escolha_tipo_senha()

    senha_final = randomizacao_senha(tipo_senha, letras_maiusculas, letras_minusculas, numeros, caracteres_especiais)

    print("-" * 50)
    print(f"Sua senha é: {senha_final}")

    salva_valores_arquivo(tipo_senha, senha_final)

    print("-" * 50)
    print("Uma senha foi gerada e salva no arquivo 'senhaGerada.txt'.")


if __name__ == "__main__":
    main()
