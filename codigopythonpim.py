#Importa random para embaralhar a ordem das perguntas do quiz
import random

#Importa a biblioteca string para utlização de .ascii_uppercase, .ascii_lowercase e .digits no gerador de senhas
import string 

#Importa datetime para os relatórios
from datetime import datetime

#Dicionário para contabilizar a quantidade de acessos em cada item do programa

acessos = {
    "menu" : 0,
    "aprender" : 0,
    "intro_python" : 0,
    "hist_curi" : 0,
    "lista_comandos" : 0,
    "boas_práticas" : 0,
    "quiz" : 0,
    "quiz_intro_python" : 0,
    "quiz_hist_curi" : 0,
    "quiz_lista_comandos" : 0,
    "quiz_boas_práticas" : 0,
    "gerador" : 0,
    "transformador" : 0,
    "relatórios" : 0,
    "acessos_funcionalidades" : 0,
    "notas" : 0,
    "senha_gerada" : 0,
    "senha_transformada" : 0
}

#Lista para armazenar as notas dos quizzes
relatorio_quiz = []

#Lista para armazenar as senhas geradas
relatorio_senha_gerada = []

#Lista para armazenar as senhas transformadas
relatorio_senha_transformada = []


global duracao


#Função para acessar os relatórios apenas com senha
def acessar_relatorios(senha_segura):
    print("\n===== ACESSO AOS RELATÓRIOS =====")
    if tentativa == senha_segura:
        print(f"\nAcesso permitido, seja bem vindo aos seus relatórios {nome}")
        acessos["relatórios"] += 1
        relatorios()
    else:
        print("\nSenha incorreta. Acesso negado!")

#Funções para verificação de CPF simples        
def verificador_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    return len(cpf) == 11 and cpf != cpf[0] * 11
    
def cpf_valido():
    while True: 
        cpf_input = input("\nDigite seu cpf: ")
        if verificador_cpf(cpf_input):
            print("\nCPF aceito!")
            return cpf_input
        else:
            print("\nCPF inválido! Tente novamente.")
            
        
#Introduz o programa e pede autorização do usuário para utilização do seu nome durante o programa
def introducao():
    global inicio_programa
    inicio_programa = datetime.now()
    print("Olá, seja bem vindo")
    print("\nNeste programa você vai encontrar tudo o que se precisa saber para iniciar sua jornada em Python!")
    print("\nPara começarmos, qual é o seu nome?")
    global nome
    nome = input('\n')
    cpf = cpf_valido()
    print(f"\n{nome}, segundo a LGPD o usuário deve ser informado sobre qualquer utilização de seus dados, por isso pedimos o seu consentimento para utilizar o seu nome e cpf apenas para identificação pessoal e também para tornar esse código mais pessoal durante a sua utilização.")
    print('\n')
    print("Você concorda com os nossos termos de utilização e política de privacidade?")
    
    print("\nCONCORDO ou DISCORDO")
    lgpd = input('\n').lower()
    
    if lgpd == "concordo":
        print("Muito obrigada, seus dados estão seguros conosco!")
        print(f"\nSeja bem vindo(a) {nome}")
        
        while True:
            print("\nDigite uma senha numérica de 6 dígitos para iniciar o programa. Essa senha também será utilizada para acessar aos relatórios:")
            
            global senha_segura    
            senha_segura = input('\nSenha: ')
            if senha_segura.isdigit() and len(senha_segura) == 6: 
                break
            else:
                print("Senha inválida. A senha deve conter 6 dígitos numéricos!")
                    
            
        print("\nSenha registrada com sucesso.")
        print("\nExecutando o programa")
        acessos["menu"] += 1
        menu_principal()
            
    elif lgpd == "discordo":
        print("Para seu maior conforto o programa será reiniciado, sinta-se livre para criar um nome e cpf especial para utilizar durante esse programa!")
        introducao()
            
    else:
        print("Opção inválida!")
        introducao()

    
def menu_principal():
    print("\nNo menu abaixo escolha o que deseja fazer:")
    print("\n(1) Aprender")
    print("\n(2) Fazer um Quiz")
    print("\n(3) Gerador de senha segura")
    print("\n(4) Transformador de senha")
    print("\n(5) Relatórios")
    print("\n(6) Sair")
    
    escolha_mp = int(input('\nSua escolha: '))
    
    try:
        if escolha_mp == 1:
            acessos["aprender"] += 1
            menu_aprender()
        elif escolha_mp == 2:
            acessos["quiz"] += 1
            menu_quiz()
        elif escolha_mp == 3:
            acessos["gerador"] += 1
            print("\n===== GERADOR DE SENHAS SEGURAS =====")
            print("\nBom ter você aqui, nesta página você poderá gerar uma senha segura apenas respondendo algumas perguntas! ")
            gerador_de_senha()
        elif escolha_mp == 4:
            acessos["transformador"] += 1
            print("===== TRANFORMADOR DE SENHA =====")
            print(f"\nOlá {nome}, nessa página você poderá transformar uma senha numérica simples em uma senha segura de base hexadecimal com caracteres especiais!")
            transformador_de_senha()
        elif escolha_mp == 5:
            acessos["relatórios"] += 1
            relatorios(senha_segura)
        elif escolha_mp == 6:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"Você usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit() 
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")
            
def menu_aprender():
    print("\nÓtimo, agora selecione o que deseja aprender:")
    print('\n')
    print("(1) Introdução à Python")
    print("(2) História e Curiosidades")
    print("(3) Lista de Comandos")
    print("(4) Boas práticas em segurança digital")
    print("(5) Voltar ao menu principal")
    print("(6) Sair")
    
    escolha_ma = int(input('\nSua escolha: '))
    
    try:
        if escolha_ma == 1:
            acessos["intro_python"] += 1
            int_python()
        elif escolha_ma == 2:
            acessos["hist_curi"] += 1
            hist_curiosidade()
        elif escolha_ma == 3:
            acessos["lista_comandos"] += 1
            lista_de_comandos()
        elif escolha_ma == 4:
            acessos["boas_práticas"] += 1
            boas_praticas()    
        elif escolha_ma == 5:
            acessos["menu"] += 1
            menu_principal()
        elif escolha_ma == 6:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"Você usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit()
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")
        
        
def int_python():
    print("\nPython é uma linguagem de alto nível, o que significa que é mais próxima da linguagem humana, facilitando assim a escrita e a leitura do código. Por isso Python se torna uma das linguagens mais utilizadas no aprendizado da programação.")
    print('\n')
    print("\nA seguir vamos aprender os principais conceitos de Python:")
    print("\n1. Variáveis")
    print("\nVariáveis são o espaço de memória onde armazenamos informações que serão usadas mais tarde. Nesse espaço podemos armazenar tanto dados simples, como textos e números, quanto dados mais complexos como resultados de operações matemáticas.")
    print("\nPara salvar dados nas variáveis devemos usar o simbolo '='")
    print("\nExemplos de variáveis:")
    print("\nnome = maria")
    print("idade = 25")
    print("minutos_por_dia = 24 * 60")
    print("\n2. Tipos de dados")
    print("\n•Inteiros (int): Números sem casas decimais. Ex:5")
    print("•Flutuantes (float): Números com casas decimais. Ex:3.14")
    print("•Strings (str): Sequência de texto. Ex:'Olá, Mundo!'")
    print("\n3. Print e Input")
    print("\nA função print serve para imprimir uma informação na tela. Então se quisermos imprimir a string 'Olá, Mundo!', devemos escrever utilizando a função print seguida de () e "". ")
    print("\nJá a função input serve para receber um dado. Para utilizar o input é necessário informar ao código qual o tipo especíico de dado se espera receber do usuário:")
    print("\nNo caso de string - input()")
    print("No caso de inteiros - int(input())")
    print("No caso de naturais - float(input())")
    print("\n4. Operadores")
    print("\nOs operadores são usados para fazer cálculos e comparações, sendo eles:")
    print("\nSoma: +")
    print("\nSubtração: -")
    print("\nMultiplicação: *")
    print("\nDivisão: /")
    print("\nIgual a: ==")
    print("\nDiferente de: !=")
    print("\nMaior que: »")
    print("\nMenor que: «")
    print("\nMaior ou igual a: »=")
    print("\nMenor ou igual a: «=")
    print("\nO que deseja fazer agora:")
    print("\n(1) Fazer um quiz")
    print("(2) Menu principal")
    print("(3) Sair")
    print('\n')
    
    escolha_intpy = int(input('\nSua escolha: '))
    
    try: 
        if escolha_intpy == 1:
            acessos["quiz_intro_python"] += 1
            quiz_intropython(quiz_1)
        elif escolha_intpy == 2:
            acessos["menu"] += 1
            menu_principal()
        elif escolha_intpy == 3:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"Você usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit()
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")
        
def hist_curiosidade():
    print("\nPython foi criada por Guido van Rossum em 1989. Guido projetou essa linguagem para ser fácil de ler e escrever, ele se baseou em linguagens como o ABC. O lançamento oficial só ocorreu em 1991.")
    print("\n5 curiosidades sobre Python:")
    print("\n. O nome 'Python' vem do programa de televisão britânico 'Monty Python's Flying Circus' que Guido gostava.")
    print("\n. Python pode ser executada em diversos sistemas operacionais, como Windows, Linux e macOS, sem necessidade de grandes modificações no código.")
    print("\n. Python é uma linguagem interpretada, isso significa que o código é executado linha por linha por um interpretador, em vez de ser convertido em código como acontece com linguagens compiladas.")
    print("\n. Python vem sendo uma linguagem amplamente utilizada no ensino de programação")
    print("\n. A sintaxe de Python foi projetada para ser intuitiva e fácil de ler, usando identação, espaços em branco, para definir blocos de código, o que ajuda na clareza e na organização")
    print("\nO que deseja fazer agora:")
    print("(1) Fazer um quiz")
    print("(2) Menu principal")
    print("(3) Sair")
    print('\n')
    
    escolha_histcuri = int(input('\nSua escolha: '))
    
    try: 
        if escolha_histcuri == 1:
            acessos["quiz_hist_curi"] += 1
            quiz_histcuri(quiz_2)
        elif escolha_histcuri == 2:
            acessos["menu"] += 1
            menu_principal()
        elif escolha_histcuri == 3:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"Você usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit()
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")
        
def lista_de_comandos():
    print("\nprint([expressão]): Exibe o valor de uma expressão no console.")
    print("\ninput([prompt]): Lê uma entrada do usuário a partir do teclado.")
    print("\nint([valor]): Converte um valor para o tipo inteiro.")
    print("\nfloat([valor]): Converte um valor para o tipo ponto flutuante.")
    print("\nstr([valor]): Converte um valor para o tipo string.")
    print("\nlist([objeto]): Converte um objeto (como um conjunto ou tupla) em uma lista.")
    print("\nrange([início], [fim], [passo]): Retorna uma sequência de números, útil para loops.")
    print("\nO que deseja fazer agora:")
    print("\n(1) Fazer um quiz")
    print("(2) Menu principal")
    print("(3) Sair")
    
    escolha_listcomand = int(input('\nSua escolha: '))
    
    try: 
        if escolha_listcomand == 1:
            acessos["quiz_lista_comandos"] += 1
            quiz_listcomand(quiz_3)
        elif escolha_listcomand == 2:
            acessos["menu"] += 1
            menu_principal()
        elif escolha_listcomand == 3:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"Você usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit()
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")
        
        
def boas_praticas():
    print("\nNa era da tecnologia é importante que tenhamos conhecimento de algumas práticas que devemos ter para nos manter seguros digitalmente. A seguir você irá aprender um pouco sobre os principais conceitos da cibersegurança básica além de alguns detalhes sobre a Lei Geral de Proteção de Dados ou LGPD.")
    print("\n")
    print("\n» Cibersegurança")
    print("\nCibersegurança é um conjunto de práticas para proteger sistemas, redes, dispositivos e dados de ameaças cibernéticas, é um campo fundamental para a proteção contra ataques que visam acessar, destruir ou alterar dados, além de previnir que sistemas sejam interrompidos.")
    print('\n')
    print("\nOs conceitos mais importantes são:")
    print("\n. Confidencialidade")
    print("Garante que apenas pessoas autorizadas possam acessar certas informações")
    print("\nEx: Senhas criptografadas, autenticação")
    print('\n')
    print("\n. Integridade")
    print("Assegura que os dados não sejam alterados ou corrompidos sem autorização")
    print("\nEx: Verificação de integridade de arquivos, assinaturas digitais")
    print('\n')
    print("\n. Disponibilidade")
    print("Garante que os dados e sistemas estejam acessíveis quando necessário.")
    print("\nEx: Proteção contra ataques DDoS, backups regulares.")
    print('\n')
    print("\nAlém desses conceitos que apresentamos acima, podemos também proteger nossos equipamentos com senhas seguras usando ferramentas como Bitwarden, 1Password, LastPass, NordPass ou o gerenciador do navegador ajudam a gerar senhas fortes automaticamente, guardar e preencher senhas com segurança")
    print('\n')
    print("\n» LGPD ")
    print("\nA LGPD na tecnologia tem um papel central, já que a maior parte dos dados pessoais hoje é coletado, armazenado e processado digitalmente. A lei impacta aplicações, bancos de dados, sistemas, sites, apps e até algoritmos de IA.")
    print("\nComo a LGPD se aplica:")
    print("\nSegundo a LGPD uma empresa só pode coletar dados com o consetimento do usuário, devendo ele ser claramente informado sobre quais dados são coletados e qual a finalidade deste dado. A coleta e o consentimento devem ter bases legais.")
    print('\n')
    print("Um exemplo prático e simples é uma empresa de delivery de comidas. Essa empresa precisa somente do seu nome, endereço e telefone, esses dados devem ser coletados apenas para fim de entrega ou cadastramento caso o usuário seja previamente informado. O usuário deve ter conhecimento de como serão tratados os seus dados.")
    
    print("\nO que deseja fazer agora:")
    print("\n(1) Fazer um quiz")
    print("(2) Menu principal")
    print("(3) Sair")
    
    escolha_boas_praticas = int(input('\nSua escolha: '))
    
    try: 
        if escolha_boas_praticas == 1:
            acessos["quiz_boas_práticas"] += 1
            quiz_boas_praticas(quiz_4)
        elif escolha_boas_praticas == 2:
            acessos["menu"] += 1
            menu_principal()
        elif escolha_boas_praticas == 3:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"Você usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit()
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")

def menu_quiz():
    print("Selecione o quiz que deseja fazer.")
    print("\n1) Introdução à Python")
    print("2) História e curiosidades")
    print("3) Lista de comandos")
    print("4) Boas práticas")
    print("5) Menu principal")
    print("6) Sair")
    
    escolha_mq = int(input('\nSua escolha: '))
    
    try:
        if escolha_mq == 1:
            acessos["quiz_intro_python"] += 1
            quiz_intropython(quiz_1)
        elif escolha_mq == 2:
            acessos["quiz_hist_curi"] += 1
            quiz_histcuri(quiz_2)
        elif escolha_mq == 3:
            acessos["quiz_lista_comandos"] += 1
            quiz_listcomand(quiz_3)
        elif escolha_mq == 4:
            acessos["quiz_boas_práticas"] += 1
            quiz_boas_praticas(quiz_4)
        elif escolha_mq == 5:
            acessos["menu"] += 1
            menu_principal()
        elif escolha_mq == 6:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"Você usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit()
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")
    
    
#Perguntas e respostas do quiz de introdução a python

quiz_1 = [
    {
        "pergunta": "O que significa o termo variável na programação?",
        "alternativas" : {
            "a" : "Uma função que retorna o valor",
            "b" : "Um espaço na memória para armazenar dados",
            "c" : "Um tipo de laço de repetição",
            "d" : "Um tipo de estrutura condicional",
            "e" : "Um tipo de banco de dados"
        },
        "correta" : "b"
    },
    {
        "pergunta" : "O que é Python?",
        "alternativas" : {
            "a" : "Uma cobra",
            "b" : "Um servidor web",
            "c" : "Uma ferramenta para edição de imagens",
            "d" : "Uma linguagem de programação",
            "e" : "Um banco de dados"
        },
        "correta" : "d"
    },
    {
        "pergunta" : "Qual o operador usado quando se trata de uma igualdade?",
        "alternativas" : {
            "a" : "+",
            "b" : "/",
            "c" : "=",
            "d" : "!=",
            "e" : "=="
        },
        "correta" : "e"
    },
    {
        "pergunta" : "Se eu quiser receber um dado numérico do usuário, quais comandos eu devo usar juntamente com o input?",
        "alternativas" : {
            "a" : "int / float",
            "b" : "string somente",
            "c" : "print / string",
            "d" : "float / while",
            "e" : "n.d.a"
        },
        "correta" : "a"
    },
    {
        "pergunta" : "Python é uma linguagem:",
        "alternativas" : {
            "a" : "Traduzida",
            "b" : "Interligada",
            "c" : "Interpretada",
            "d" : "Acessível",
            "e" : "n.d.a"
        },
        "correta" : "c"
    }
]

# Embaralha a ordem das perguntas usando o random do começo do código
random.shuffle(quiz_1)

#Função para realizar o quiz acima
def quiz_intropython(quiz_1):
    acertos1 = 0
    for i, item in enumerate(quiz_1, 1):
        print(f"\nPergunta {i}: {item['pergunta']}")
        for chave, texto in item["alternativas"].items():
            print(f"  {chave}) {texto}")
        resposta = input("\nSua resposta: ").lower()
        if resposta == item["correta"]:
            print("Correto!")
            acertos1 += 1
        else:
            print(f"Errado! A resposta correta era: {item['correta']}) {item['alternativas'][item['correta']]}")
    print(f"\nVocê acertou {acertos1} de {len(quiz_1)} perguntas.")
    notas_quiz("Introdução à Python", acertos1)
    acessos["menu"] += 1
    print("\nO que deseja fazer agora:")
    print("\n(1) Menu principal")
    print("(2) Sair")
    print('\n')
    
    escolha_intpy = int(input('\nSua escolha: '))
    
    try: 
        if escolha_intpy == 1:
            acessos["menu"] += 1
            menu_principal()
        elif escolha_intpy == 2:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"Você usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit()
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")

# Perguntas e respostas do quiz de história e curiosidades 

quiz_2 = [
    {
        "pergunta": "Quem é o criador da linguagem Python?",
        "alternativas" : {
            "a" : "Bill Gates",
            "b" : "Guido van Rossum",
            "c" : "Steve Jobs",
            "d" : "Linus Torvalds",
            "e" : "Mark Zuckerberg"
        },
        "correta" : "b"
    },
    {
        "pergunta" : "Quando Python foi oficialmente lançado?",
        "alternativas" : {
            "a" : "1980",
            "b" : "2000",
            "c" : "1981",
            "d" : "1995",
            "e" : "1991"
        },
        "correta" : "e"
    },
    {
        "pergunta" : "Python foi nomeado com base em:",
        "alternativas" : {
            "a" : "O programa de televisão 'Monty Python's Flying Circus",
            "b" : "Uma cobra",
            "c" : "A cidade de Python na Grécia",
            "d" : "Um deus mitológico",
            "e" : "No nome do criador"
        },
        "correta" : "a"
    },
    {
        "pergunta" : "Qual o nome da filosofia que guia o design do Python, e que pode ser resumida pela frase 'Há uma maneira óbivia de fazer isso'?",
        "alternativas" : {
            "a" : "Código Limpo",
            "b" : "Refatoração Simples",
            "c" : "Pragmatic Programming",
            "d" : "Zen of Python",
            "e" : "Clean Code"
        },
        "correta" : "d"
    }
]

# Embaralha a ordem das perguntas usando o random do começo do código
random.shuffle(quiz_2)

#Função para realizar o quiz acima
def quiz_histcuri(quiz_2):
    acertos2 = 0
    for i, item in enumerate(quiz_2, 1):
        print(f"\nPergunta {i}: {item['pergunta']}")
        for chave, texto in item["alternativas"].items():
            print(f"  {chave}) {texto}")
        resposta = input("\nSua resposta: ").lower()
        if resposta == item["correta"]:
            print("Correto!")
            acertos2 += 1
        else:
            print(f"Errado! A resposta correta era: {item['correta']}) {item['alternativas'][item['correta']]}")
    print(f"\nVocê acertou {acertos2} de {len(quiz_2)} perguntas.")
    notas_quiz("História e Curiosidades", acertos2)
    acessos["menu"] += 1
    print("\nO que deseja fazer agora:")
    print("\n(1) Menu principal")
    print("(2) Sair")
    print('\n')
    
    escolha_histcuri = int(input('\nSua escolha: '))
    
    try: 
        if escolha_histcuri == 1:
            acessos["menu"] += 1
            menu_principal()
        elif escolha_histcuri == 2:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"Você usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit()
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")


# Perguntas e respostas do quiz de lista de comandos 

quiz_3 = [
    {
        "pergunta": "O que o comando print faz em Python?",
        "alternativas" : {
            "a" : "Recebe uma entrada de usuário",
            "b" : "Exibe informações na tela",
            "c" : "Converte valor para inteiro",
            "d" : "Cria uma lista de números",
            "e" : "Armazena dados na núvem"
        },
        "correta" : "b"
    },
    {
        "pergunta" : "O que o comando input faz em Python?", 
        "alternativas" : {
            "a" : "Exibe uma mensagem na tela",
            "b" : "Converte uma string em um número inteiro",
            "c" : "Imprime um valor na tela",
            "d" : "Solicita ao usuário que insira um valor",
            "e" : "Faz uma função e retorna um dado específico"
        },
        "correta" : "d"
    },
    {
        "pergunta" : "O que o comando float faz em Python?:",
        "alternativas" : {
            "a" : "Converte uma string para inteiro",
            "b" : "Cria uma lista de números flutuantes",
            "c" : "Converte um número inteiro para string",
            "d" : "Converte um valor flutuante (ponto decimal) para uma string",
            "e" : "Converte um valor para tipo flutuante (ponto decimal)"
        },
        "correta" : "e"
    },
    {
        "pergunta" : "O que o comando int faz em Python?",
        "alternativas" : {
            "a" : "Converte uma string ou outro tipo para ponto flutuante",
            "b" : "Converte uma string pra número ponto flutuante",
            "c" : "Cria uma lista de inteiros",
            "d" : "Define um valor para tipo inteiro",
            "e" : "Cria uma lista e define os valores inteiros"
        },
        "correta" : "d"
    }
]

# Embaralha a ordem das perguntas usando o random do começo do código
random.shuffle(quiz_3)

#Função para realizar o quiz acima
def quiz_listcomand(quiz_3):
    acertos3 = 0
    for i, item in enumerate(quiz_3, 1):
        print(f"\nPergunta {i}: {item['pergunta']}")
        for chave, texto in item["alternativas"].items():
            print(f"  {chave}) {texto}")
        resposta = input("\nSua resposta: ").lower()
        if resposta == item["correta"]:
            print("Correto!")
            acertos3 += 1
        else:
            print(f"Errado! A resposta correta era: {item['correta']}) {item['alternativas'][item['correta']]}")
    print(f"\nVocê acertou {acertos3} de {len(quiz_3)} perguntas.")
    notas_quiz("Lista de comandos", acertos3)
    acessos["menu"] += 1
    print("\nO que deseja fazer agora:")
    print("\n(1) Menu principal")
    print("(2) Sair")
    print('\n')
    
    escolha_listcomand = int(input('\nSua escolha: '))
    
    try: 
        if escolha_listcomand == 1:
            acessos["menu"] += 1
            menu_principal()
        elif escolha_listcomand == 2:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"Você usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit()
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")


# Perguntas e respostas do quiz de boas praticas 

quiz_4 = [
    {
        "pergunta": "O que é Cibersegurança, segundo o texto?",
        "alternativas" : {
            "a" : "É o uso de redes sociais com segurança.",
            "b" : "É a prática de vender dados pessoais de forma legal.",
            "c" : "É um conjunto de práticas para proteger redes Wi-Fi domésticas.",
            "d" : "É o conjunto de práticas que protege sistemas, redes e dados contra ameaças cibernéticas.",
            "e" : "É a proteção física de equipamentos de informática."
        },
        "correta" : "d"
    },
    {
        "pergunta" : "Qual conceito da Cibersegurança garante que apenas pessoas autorizadas acessem certas informações?" ,
        "alternativas" : {
            "a" : "Confidencialidade",
            "b" : "Integridade",
            "c" : "Disponibilidade",
            "d" : "Autonomia",
            "e" : "Acessibilidade"
        },
        "correta" : "a"
    },
    {
        "pergunta" : "O que significa “Disponibilidade” na Cibersegurança?",
        "alternativas" : {
            "a" : "Proteger os dados com criptografia.",
            "b" : "Ter senhas armazenadas em planilhas.",
            "c" : "Garantir que apenas usuários autorizados alterem os dados.",
            "d" : "Verificar a integridade de arquivos com antivírus.",
            "e" : "Garantir que dados e sistemas estejam acessíveis quando necessário."
        },
        "correta" : "e"
    },
    {
        "pergunta" : "De acordo com a LGPD, o que uma empresa precisa fazer para coletar dados de um usuário?",
        "alternativas" : {
            "a" : "Pedir autorização apenas por telefone.",
            "b" : "Coletar os dados antes e pedir consentimento depois.",
            "c" : "Informar somente o nome do sistema usado para armazenamento.",
            "d" : "Obter consentimento claro do usuário e explicar a finalidade dos dados.",
            "e" : "Pegar os dados pessoais sem informar, desde que seja uma empresa conhecida."
        },
        "correta" : "d"
    }
]

# Embaralha a ordem das perguntas usando o random do começo do código
random.shuffle(quiz_4)

#Função para realizar o quiz acima
def quiz_boas_praticas(quiz_4):
    acertos4 = 0
    for i, item in enumerate(quiz_4, 1):
        print(f"\nPergunta {i}: {item['pergunta']}")
        for chave, texto in item["alternativas"].items():
            print(f"  {chave}) {texto}")
        resposta = input("\nSua resposta: ").lower()
        if resposta == item["correta"]:
            print("Correto!")
            acertos4 += 1
        else:
            print(f"Errado! A resposta correta era: {item['correta']}) {item['alternativas'][item['correta']]}")
    print(f"\nVocê acertou {acertos4} de {len(quiz_4)} perguntas.")
    notas_quiz("Boas práticas", acertos4)
    acessos["menu"] += 1
    print("\nO que deseja fazer agora:")
    print("\n(1) Menu principal")
    print("(2) Sair")
    print('\n')
    
    escolha_boas_praticas = int(input('\nSua escolha: '))
    
    try: 
        if escolha_boas_praticas == 1:
            acessos["menu"] += 1
            menu_principal()
        elif escolha_boas_praticas == 2:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"Você usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit()
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")
            
            
# Página dedicada a gerar senhas seguras de acordo com as escolhas do usuário
# Função para gerar senha segura personalizada

def gerador_de_senha_(tamanho = 16, maiusculas = True, minusculas= True, numeros = True, caracteres_especiais = True):
    caracteres = "" #Variável que irá armazenar a senha gerada 
    
    #Testa se as opções de caracteres sáo verdadeiras de acordo com a escolha do usuário
    if maiusculas:
        caracteres += string.ascii_uppercase # Acrescenta letras maiusculas aos possíveis dígitos
    if minusculas:
        caracteres += string.ascii_lowercase # Acrescenta letras minusculas aos possíveis dígitos
    if numeros:
        caracteres += string.digits # Acrescenta números de aos possíveis dígitos
    if caracteres_especiais:
        caracteres += string.punctuation # acrescenta caracteres especiais na senha 
    if not caracteres:
        return "Nenhum tipo de caractere selecionado!"
        
    senha = ''.join(random.choices(caracteres, k=tamanho))
    return senha
    acessos["menu"] += 1
    menu_principal()
    
def gerador_de_senha():
    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha (mínimo recomendado: 12):  "))
        except ValueError:
            print("Entrada inválida. Usando o tamanho padrão de 16 caracteres!")
            tamanho = 16
        
        maiusculas = input("Deseja incluir letras MAIÚSCULAS? (s/n):  ").strip().lower() == 's'
        minusculas = input("Deseja incluir letras minusculas? (s/n):  ").strip().lower() == 's'
        numeros = input("Deseja incluir números? (s/n):  ").strip().lower() == 's'
        caracteres_especiais = input("Deseja incluir caracteres especiais? (s/n):  ").strip().lower() == 's'
    
        senha = gerador_de_senha_(tamanho, maiusculas, minusculas, numeros, caracteres_especiais)
        print("\nSenha gerada: ")
        print(senha)
        salvar_senha_gerada(senha)
        print("=" * 35)
    
    
        continuar = input("Deseja gerar outra senha? (s/n):  ").strip().lower()
        acessos["gerador"] += 1
        
        if continuar != 's':
            print("Encerrando o gerador de senha. Até mais!")
            acessos["menu"] += 1
            menu_principal()

#Transformador de senha, transforma um número para base hexadecimal, embaralha e complementa a senha com caracteres especiais 

def transformador_de_senha():
    while True:
        try:
            numero_decimal = int(input("\nDigite um número inteiro:  "))
            numero_hex = hex(numero_decimal)[2:].upper() #Transforma o numero decimal em um número hexadecimal e usando o [2:] exclui o 'Ox'
        
            lista_caracteres = list(numero_hex)
            random.shuffle(lista_caracteres)
        
            maiusculas = random.choices(string.ascii_uppercase, k = 2)
            minusculas = random.choices(string.ascii_lowercase, k = 2)
            numeros = random.choices(string.digits, k = 2)
            caracteres_especiais = random.choices(string.punctuation, k = 2)
        
# Junta todos os itens que serão usados na senha em uma única variável, embaralha e depois com o .join junta todos em uma única string sem separadores.
            senha_completa = lista_caracteres + maiusculas + minusculas + numeros + caracteres_especiais
            random.shuffle(senha_completa)
            senha_final = ''.join(senha_completa)
        
            print(f"Sua senha é:  {senha_final}")
            salvar_senha_transformada(numero_decimal, senha_final)
        
        except ValueError:
            print("Entrada inválida! Por favor digite um número inteiro válido.")

        continuar = input("Deseja transformar outra senha? (s/n):  ").strip().lower()
        acessos["transformador"] += 1
        
        if continuar != 's':
            print("Encerrando o transformador de senha. Até mais!")
            acessos["menu"] += 1
            menu_principal()
            
def relatorios(senha_segura):
    tentativar = input("Digite sua senha para acessar os relatórios: ")
    
    if tentativar == senha_segura:
        print("\nAcesso permitido. Seja bem vindo!")
    
        print("\nSelecione o relatório que deseja ter acesso:")
        print("\n1) Quantidade de acessos a cada funcionalidade")
        print("\n2) Notas de cada quiz")
        print("\n3) Senhas geradas")
        print("\n4) Senhas transformadas")
        print("\n5) Menu principal")
        print("\n6) Sair")
    
        escolha_relatórios = int(input('\nSua escolha: '))
    
        try:
            if escolha_relatórios == 1:
                acessos["acessos_funcionalidades"] += 1
                acessos_partes()
            elif escolha_relatórios == 2:
                acessos["notas"] += 1
                mostrar_notas()
            elif escolha_relatórios == 3:
                acessos["senha_gerada"] += 1
                mostrar_senhag()
            elif escolha_relatórios == 4:
                acessos["senha_transformada"] += 1
                mostrar_senhat()
            elif escolha_relatórios == 5:
                acessos["menu"] += 1
                menu_principal()
            elif escolha_relatórios == 6:
                fim_programa = datetime.now()
                duracao = fim_programa - inicio_programa
                print(f"Você usou o programa por: {duracao}[2:]")
                print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
                print("\nSaindo...")
                exit()
        
        except ValueError:
            print("Valor inválido. Digite uma opção válida!")
        
    else:
        print("\nSenha incorreta. Acesso negado.")
#Função para mostrar o resultado do contador de acessos        
def acessos_partes():
    print("\n==== RELATÓRIO DE ACESSOS =====")
    print(f"\nMenu: {acessos['menu']} vez(es)")
    print(f"\nAprender: {acessos['aprender']} vez(es)")
    print(f"\nIntrodução à Python: {acessos['intro_python']} vez(es)")
    print(f"\nHistória e Curiosidades: {acessos['hist_curi']} vez(es)")
    print(f"\nLista de comandos: {acessos['lista_comandos']} vez(es)")
    print(f"\nBoas práticas: {acessos['boas_práticas']} vez(es)")
    print(f"\nQuiz: {acessos['quiz']} vez(es)")
    print(f"\nQuiz Introdução à Python: {acessos['quiz_intro_python']} vez(es)")
    print(f"\nQuiz História e Curiosidades:: {acessos['quiz_hist_curi']} vez(es)")
    print(f"\nQuiz Lista de comandos: {acessos['quiz_lista_comandos']} vez(es)")
    print(f"\nQuiz Boas práticas: {acessos['quiz_boas_práticas']} vez(es)")
    print(f"\nGerador de senha: {acessos['gerador']} vez(es)")
    print(f"\nTransformador de senha: {acessos['transformador']} vez(es)")
    print(f"\nRelatórios: {acessos['relatórios']} vez(es)")
    print(f"\nAcesso às funcionalidades: {acessos['acessos_funcionalidades']} vez(es)")
    print(f"\nRelatório notas quiz: {acessos['notas']} vez(es)")
    print(f"\nRelatório senhas geradas: {acessos['senha_gerada']} vez(es)")
    print(f"\nRelatório senhas transformadas: {acessos['senha_transformada']} vez(es)")
    print("\nO que deseja fazer agora:")
    print("\n(1) Menu principal")
    print("(2) Sair")
    print('\n')
    
    escolha_acesso = int(input('\nSua escolha: '))
    
    try: 
        if escolha_acesso == 1:
            acessos["menu"] += 1
            menu_principal()
        elif escolha_acesso == 2:
            fim_programa = datetime.now()
            duracao = fim_programa - inicio_programa
            print(f"\nVocê usou o programa por: {duracao}")
            print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
            print("\nSaindo...")
            exit()
        else:
            print("\nErro. Digite uma opção válida!")
    except ValueError:
        print("Erro, opção inválida!")
    
 
#Funções criadas para salvar e mostrar a nota, nome e horário de cada quiz em um relatório  
def notas_quiz(nome, nota):
    horario = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    relatorio_quiz.append({
        "quiz" : nome,
        "nota" : nota,
        "horario" : horario
    })
   
   
def mostrar_notas():
    print("\n===== RELATÓRIO DE NOTAS =====")
    if not relatorio_quiz:
        print("Nenhuma nota registrada.")
        print("\nO que deseja fazer agora:")
        print("\n(1) Menu principal")
        print("(2) Sair")
        print('\n')
    
        escolha_notas = int(input('\nSua escolha: '))
    
        try: 
            if escolha_notas == 1:
                acessos["menu"] += 1
                menu_principal()
            elif escolha_notas == 2:
                fim_programa = datetime.now()
                duracao = fim_programa - inicio_programa
                print(f"\nVocê usou o programa por: {duracao}")
                print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
                print("\nSaindo...")
                exit()
            else:
                print("\nErro. Digite uma opção válida!")
        except ValueError:
            print("Erro, opção inválida!")
    else: 
        for registro in relatorio_quiz:
            print(f"{registro['quiz']} - Nota: {registro['nota']} - Feito em: {registro['horario']}")
            print("\nO que deseja fazer agora:")
            print("\n(1) Menu principal")
            print("(2) Sair")
            print('\n')
    
            escolha_notas2 = int(input('\nSua escolha: '))
    
            try: 
                if escolha_notas2 == 1:
                    acessos["menu"] += 1
                    menu_principal()
                elif escolha_notas2 == 2:
                    fim_programa = datetime.now()
                    duracao = fim_programa - inicio_programa
                    print(f"\nVocê usou o programa por: {duracao}")
                    print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
                    print("\nSaindo...")
                    exit()
                else:
                    print("\nErro. Digite uma opção válida!")
            except ValueError:
                print("Erro, opção inválida!")
            
#Funções criadas para salvar e mostrar as senhas geradas    
def salvar_senha_gerada(senhag):
    horario = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    relatorio_senha_gerada.append({
        "senha" : senhag,
        "horario" : horario
    })
    
def mostrar_senhag():
    print("\n===== RELATÓRIO SENHAS GERADAS =====")
    if not relatorio_senha_gerada:
        print("Nenhuma senha registrada.")
        print("\nO que deseja fazer agora:")
        print("\n(1) Menu principal")
        print("(2) Sair")
        print('\n')
    
        escolha_senhag = int(input('\nSua escolha: '))
    
        try: 
            if escolha_senhag == 1:
                acessos["menu"] += 1
                menu_principal()
            elif escolha_senhag == 2:
                fim_programa = datetime.now()
                duracao = fim_programa - inicio_programa
                print(f"\nVocê usou o programa por: {duracao}")
                print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
                print("\nSaindo...")
                exit()
            else:
                print("\nErro. Digite uma opção válida!")
        except ValueError:
            print("Erro, opção inválida!")
    else:
        for registro in relatorio_senha_gerada:
            print(f"{registro['senha']} - Gerada em: {registro['horario']}")
            print("\nO que deseja fazer agora:")
            print("\n(1) Menu principal")
            print("(2) Sair")
            print('\n')
    
            escolha_senhag2 = int(input('\nSua escolha: '))
    
            try: 
                if escolha_senhag2 == 1:
                    acessos["menu"] += 1
                    menu_principal()
                elif escolha_senhag2 == 2:
                    fim_programa = datetime.now()
                    duracao = fim_programa - inicio_programa
                    print(f"\nVocê usou o programa por: {duracao}")
                    print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
                    print("\nSaindo...")
                    exit()
                else:
                    print("\nErro. Digite uma opção válida!")
            except ValueError:
                print("Erro, opção inválida!")
   
#Funções criadas para salvar e mostrar os numeros inseridos e a senha final  
def salvar_senha_transformada(numeross, senhat ):
    horario = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    relatorio_senha_transformada.append({
        "numeros" : numeross, 
        "senha" : senhat,
        "horario" : horario
    })
   
def mostrar_senhat():
    print("===== RELATÓRIO SENHAS TRANSFORMADAS =====")
    if not relatorio_senha_transformada:
        print("Nenhuma senha registrada.")
        print("\nO que deseja fazer agora:")
        print("\n(1) Menu principal")
        print("(2) Sair")
        print('\n')
    
        escolha_senhat = int(input('\nSua escolha: '))
    
        try: 
            if escolha_senhat == 1:
                acessos["menu"] += 1
                menu_principal()
            elif escolha_senhat == 2:
                fim_programa = datetime.now()
                duracao = fim_programa - inicio_programa
                print(f"\nVocê usou o programa por: {duracao}")
                print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
                print("\nSaindo...")
                exit()
            else:
                print("\nErro. Digite uma opção válida!")
        except ValueError:
            print("Erro, opção inválida!")
    else:
        for registro in relatorio_senha_transformada:
            print(f"{registro['numeros']} - Transformado na senha: {registro['senha']} - Transformada em: {registro['horario']}")
            print("\nO que deseja fazer agora:")
            print("\n(1) Menu principal")
            print("(2) Sair")
            print('\n')
    
            escolha_senhat2 = int(input('\nSua escolha: '))
    
            try: 
                if escolha_senhat2 == 1:
                    acessos["menu"] += 1
                    menu_principal()
                elif escolha_senhat2 == 2:
                    fim_programa = datetime.now()
                    duracao = fim_programa - inicio_programa
                    print(f"\nVocê usou o programa por: {duracao}")
                    print("\nMuito obrigada por utilizar o nosso programa, até a próxima!")
                    print("\nSaindo...")
                    exit()
                else:
                    print("\nErro. Digite uma opção válida!")
            except ValueError:
                print("Erro, opção inválida!")

#Inicia o código com a introdução e logo em seguida o menu
introducao()
menu_principal()