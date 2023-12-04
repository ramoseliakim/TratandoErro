# Projeto Tratando Erro
#Eliakim Ramos. Turma 11
nome = str(input("Digite seu nome completo: "))
saidaLoop = 0
while saidaLoop == 0:
    try:
        ano = int(input("Digite seu ano de nascimento: "))
        if ano < 1922 or ano > 2022:
            print("Você usou um número inválido. Tente novamente")
        else:
            resultado = 2023 - ano
            print(f"{nome}, você tem {resultado} anos")
            saidaLoop = 1
    except ValueError:
        print("Letras e caracteres não são permitidos.\nTente novamente.")
