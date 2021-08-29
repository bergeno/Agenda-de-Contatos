AGENDA = {}

# Contatos Iniciais

AGENDA["Bernardo"] = {
    "Tel": "+31 998880150",
    "Email": "bernardo.com.catao@gmail.com",
    "Endereco": "Rua Ouro Preto 1143",

}
AGENDA["Norma"] = {
    "Tel": "+31 992910173",
    "Email": "saraiva.norma@gmail.com",
    "Endereco": "Alameda das Braunas 994",

}


def mostrar_contatos():
    print("-------------------------------")
    for contato in AGENDA:
        buscar_contatos(contato)
        print("-----------------------")


def buscar_contatos(contato):
    try:
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]["Tel"])
        print("Email:", AGENDA[contato]["Email"])
        print("Endereço:", AGENDA[contato]["Endereco"])
    except:
        print("Nome inválido!")


def incluir_editar_contatos(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "Tel": telefone,
        "Email": email,
        "Endereco": endereco,
    }
    print(">>>> Contato {} adicionado/editado com sucesso!".format(contato))


def excluir_contatos(contato):
    AGENDA.pop(contato)
    print(">>>> Contato {} excluído com sucesso!".format(contato))


def menu():
    print('''----------------------------
    Agenda

    1 - Mostrar todos os contatos
    2 - Buscar Contato
    3 - Incluir Contato
    4 - Editar Contato
    5 - Excluir Contato
    6 - Exportar Contatos (CSV)
    7 - Importar Contatos (CSV)
    0 - Fechar Agenda''')

def exportar_contatos():
    try:
        with open('importar.csv', 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['Tel']
                email = AGENDA[contato]['Email']
                endereco = AGENDA[contato]['Endereco']
                arquivo.write("{},{},{},{}\n" .format(contato, telefone, email, endereco))
        print(">>>>>Agenda exportada com sucesso")
    except Exception as error:
        print(">>>>>Algum erro ocorreu ao exportar contatos")
        print(error)

def importar_contatos(nome_do_arquivo):

    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            print(linhas.split(","))
    except FileNotFoundError:
        print(">>>>>Arquivo não encontrado")
    except Exception as error:
        print(">>>>>>Algum erro inesperado ocorreu")
        print(error)

sair = "false"
while sair == "false":
    menu()

    print('')
    escolha = str(input("Escolha uma opção: "))

    if escolha == "1":
        mostrar_contatos()
    elif escolha == "2":
        contato = str(input("Digite o nome do contato: "))
        buscar_contatos(contato)
    elif escolha == "3" or escolha == "4":
        contato = str(input("Digite o nome do contato: "))
        telefone = str(input("Digite o número do contato: "))
        email = str(input("Digite o email do contato: "))
        endereco = str(input("Digite o endereço do contato: "))
        incluir_editar_contatos(contato, telefone, email, endereco)
    elif escolha == "5":
        contato = str(input("Digite o nome do contato: "))
        excluir_contatos(contato)
    elif escolha == "6":
        exportar_contatos()
    elif escolha == "7":
        nome_do_arquivo = input('Digite o nome do arquivo: ')
        importar_contatos(nome_do_arquivo)
    elif escolha == "0":
        sair = "true"
    elif escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4" and escolha != "5" and escolha != "0":
        print("Comando Inválido!")


