import json
import random

with open("Menu_principal/Professores/professores.json", "r") as f:
    professores = json.load(f)


def menu_professor():
    menu = int(input("Bem-vindo ao nosso sistema de controle de professor! Escolha uma opção abaixo: \n[1] Cadastrar Professor \n[2] Visualizar Professor \n[3] Editar Professor \n[4] Apagar Professor \nResp: "))
    if menu == 1:
        cadastrar_professor()
    elif menu == 2:
        ver_professores()
    elif menu == 3:
        editar_professor()
    elif menu == 4:
        excluir_professores()
    while menu != 1 and menu != 2 and menu != 3 and menu != 4:
        errado = int(input("DIGITO ERRADO! Escolha uma opção abaixo: \n[1] Cadastrar Professor \n[2] Visualizar Professor \n[3] Editar Professor \n[4] Apagar Professor \nResp: "))
        if errado == 1:
            cadastrar_professor()
        elif errado == 2:
            ver_professores()
        elif errado == 3:
            editar_professor()
        elif errado == 4:
            excluir_professores()
        
def cadastrar_professor():                                                  
    nome = input("Digite o nome do professor: ").title()
    sobrenome = input("Digite o sobrenome do professor: ").title()
    nome = nome + '' + sobrenome

    CPF = input("Digite o seu CPF: ")
    
    if len(CPF) == 11:
        CPF = f'{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}.{CPF[9:11]}'
        print(CPF)
    
    materias = input("Quais matérias este professor ensina: ").split(', ')
    #turmas = int(input("Quantas turmas este professor da aula: "))

    matricula = random.randint(1000000, 9999999)
    
    professores[nome] = {'Matricula': matricula, "Materias": materias, "Senha": CPF, "CPF": CPF}

    denovo = int(input("Deseja continuar o cadastrando: \n[1] Sim \n[2] Não \nResp: "))
    if denovo == 1:
        cadastrar_professor()
    else:
        menu_professor()
    


def editar_professor():
    pass

def ver_professores():

    print(f"\n{'-== PROFESSORES ==-': ^50}\n{'='*50}")

    for professor in professores:
        print(f"\n{f'---==oOo==---': ^50}\nProfessor: {professor}")
        for informacoes in professores[professor]:
            professor_informacoes = professores[professor][informacoes]
            if type(professor_informacoes) == list:
                print(f"{informacoes}:", end=' ')
                for lista_informacoes in professor_informacoes:
                    if lista_informacoes != professor_informacoes[-1]:
                        print(lista_informacoes, end=', ')
                    else:
                        print(lista_informacoes)
            else:
                print(f"{informacoes}: {professor_informacoes}")
        print(f"{f'---==oOo==---': ^50}")

    menu_professor()

def excluir_professores():
    encontrar = input("Digite o nome do aluno que você deseja apagar: ")
    if encontrar in professores:
        print(encontrar)
        apagar = int(input("Deseja apagar este professor: \n[1] Sim \n[2] Não \nResp:  "))    
        if apagar == 1:
            del professores[encontrar]
        else:
            excluir_professores()
    else:
        print("Este professor não existe")
    prosseguir = int(input("Deseja continuar apagando: \n[1] Sim \n[2] Não \nResp: "))
    if prosseguir == 1:
        excluir_professores()
    else:
        menu_professor()

def vizualizar_turmas():
    pass

def visualizar_alunos_turmas():
    pass

menu_professor()
