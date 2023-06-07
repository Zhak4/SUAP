import json

alunos = {}

with open("Menu_principal/Alunos/alunos.json", "r") as file:
    alunos = json.load(file)
    
def menu_aluno():
    
    while True:

        print(f"\n{'-== SISTEMA DE CONTROLE DE ALUNOS ==-': ^50}\n{'='*50}\n{'---==oOo==---': ^50}")
        pergunta = input("Bem-vindo ao sistema de controle de alunos! \n[1] Cadastrar aluno  \n[2] Visualizar alunos \n[3] Editar aluno \n[4] Apagar Alunos \n\nOpção: ")

        if pergunta == '1':
            cadastrar_aluno()

        elif pergunta == '2':
            visualizar_aluno()

        elif pergunta == '3':
            editar_aluno()

        elif pergunta == '4':
            deletar_aluno()

        else:
            print("Opção inválida")

def cadastrar_aluno():

    print(f"\n{'-== CADASTRAR ALUNO ==- ': ^50}\n{'='*50}\n{'---==oOo==---': ^50}")
    nome_aluno = input("Digite o seu nome: ").title()
    sobrenome_aluno = input("Digite o seu sobrenome: ").title()
    
    nome = nome_aluno + ' ' + sobrenome_aluno
    
    CPF = input("Digite o seu CPF: ")
    
    if len(CPF) == 11:
        CPF = f'{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:11]}'
    else:
        CPF_anterior = CPF
        while CPF == CPF_anterior or len(CPF) != 11:
            print("CPF inválido!")
            CPF = input("Digite um CPF diferente: ")
    
    maior = 0

    for aluno in alunos:
        if alunos[aluno]["Matricula"] > maior:
            maior = alunos[aluno]["Matricula"]
    
    alunos[nome] = {'Matricula': maior + 1, "Senha": CPF, "CPF": CPF}

    while True:
        continuar = input("Deseja continuar cadastrando alunos: \n[1] Sim \n[2] Não \nResp: ")

        if continuar == '1':
            print(f"{f'---==oOo==---': ^50}")
            cadastrar_aluno()

        elif continuar == '2':
            menu_aluno()
        else:
            print("Opção inválida!")
    
def visualizar_aluno():

    print(f"\n{'-== ALUNOS CADASTRADOS ==-': ^50}\n{'='*50}")

    for aluno in alunos:
        print(f"\n{f'---==oOo==---': ^50}\nAluno: {aluno}")
        for informacoes in alunos[aluno]:
            aluno_informacoes = alunos[aluno][informacoes]
            if type(aluno_informacoes) == list:
                print(f"{informacoes}:", end=' ')
                for lista_informacoes in aluno_informacoes:
                    if lista_informacoes != aluno_informacoes[-1]:
                        print(lista_informacoes, end=', ')
                    else:
                        print(lista_informacoes)
            else:
                print(f"{informacoes}: {aluno_informacoes}")
        print(f"{f'---==oOo==---': ^50}")
    
    menu_aluno()
    
def editar_aluno():
    buscar_aluno = input("Digite o nome do aluno que você deseja editar: ")
    qtd_alunos = 0
    if buscar_aluno in alunos:
        for informacoes in alunos[buscar_aluno]:
            print(informacoes, alunos[buscar_aluno][informacoes])
            
    edicao = int(input("O que você deseja alterar: \n[1] Nome e Sobrenome \n[2] Matrícula \n[3] Senha \nResp: "))
    if edicao == 1:
        nome = input("Digite o seu nome: ")
        sobrenome = input("Digite o seu sobrenome: ")
        novo_nome = nome + ' ' + sobrenome

        alunos[novo_nome] = alunos[buscar_aluno]
        del alunos[buscar_aluno]
    elif edicao == 2:
        nova_matricula = int(input("Digite a sua matrícula: "))
        alunos[buscar_aluno]['Matricula'] = nova_matricula
    elif edicao == 3 :
        nova_senha = input("Digite a sua senha: ")
        alunos[buscar_aluno]["Senha"] = nova_senha
    
    
    repetir = int(input("Deseja continuar editando os alunos: \n[1] Sim \n[2] Não \nResp: "))
    if repetir == 1:
        editar_aluno()
    else:
        menu_aluno()
                           
def deletar_aluno():
    encontrar = input("Digite o nome do aluno que você deseja apagar: ")
    if encontrar in alunos:
        print(encontrar)
        apagar = int(input("Deseja apagar este aluno: \n[1] Sim \n[2] Não \nResp:  "))    
        if apagar == 1:
            del alunos[encontrar]
        else:
            deletar_aluno()
    else:
        print("Este aluno não existe")
    prosseguir = int(input("Deseja continuar apagando: \n[1] Sim \n[2] Não \nResp: "))
    if prosseguir == 1:
        deletar_aluno()
    else:
        menu_aluno()
    
menu_aluno()

print(alunos)
