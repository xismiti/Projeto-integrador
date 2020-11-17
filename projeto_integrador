import random

print('='*30,'\nBem-vindo ao Python Bridge!')
print('='*30)
input()
op=1
while True:
    print('=' * 30)
    print('Para começar, escolha uma das opções abaixo:\n1- Cadastrar-se\n2- Comprar software\n3- Saiba mais\n4- Sair')
    print('=' * 30)
    op = int(input('Digite sua opção: '.strip()))
    if op==1:
        print('Voce deseja:\n1-Cadastrar-se como cliente\n2-Cadastrar-se como empresa\n3-Cadastrar-se como consultor\n4-Cadastrar Software\n5-Sair')
        op2=int(input('Digite sua opção:'))
        if op2==1:
            controle = 1
            while True:

                print('1-Fazer Login \n2-Fazer Cadastro \n3-Sair')
                controle = int(input('Escolha uma opoção acima: '))

                if controle == 3:
                    break
                print('-' * 50, end='\n')

                if controle == 1:
                    email = input('Digite seu e-mail: ')
                    senha = input('Digite seu CPF: ')
                    print(email, senha)
                    print('Aguarde uns segundos...')
                    break
                elif controle == 2:
                    print('\n\nOlá, vamos realizar seu cadastro!\nAbaixo nos informe os dados solicitados')

                    nome = input('Digite seu nome completo: ')
                    idade = input('Digite sua idade: ')
                    tele = input('Digite seu telefone/celular: ')
                    email = input('Digite seu e-mail: ')
                    cpf = input('Digite seu CPF: ')
                    print('\nOlá ' + str(nome) + '! \nAgora nos fale sua localização abaixo:')
                    estado = input('Diga o estado onde você mora: ')
                    cidade = input('Qual sua cidade: ')
                    bairro = input('Bairro: ')
                    rua = input('Rua: ')
                    numero = input('Nº da casa: ')
                    print('Muito obrigado(a) pela paciência ' + str(nome) + '! \nSeu cadastro foi realizado com sucesso!')
                    break
        elif op2==2:
            print('='*30)
            controle = 1
            while True:
                print('1-Buscar empresas cadastradas \n2-Fazer Cadastro \n3-Sair')
                controle = int(input('Escolha uma opção acima: '))

                if controle == 3:
                    break
                print('-' * 50, end='\n')

                if controle == 1:
                    email = input('Digite razão social: ')
                    senha = input('Digite seu CNPJ: ')

                    print('Aguarde uns segundos...')
                    break
                elif controle == 2:
                    print('\n\nOlá, vamos realizar o cadastro!\nAbaixo nos informe os dados solicitados')

                    nome_empresa = input('Digite a razão social da empresa: ')
                    atividade = input('Digite atividade econômica da empresa: ')
                    tele = input('Digite o número de contato ( comercial ou celular): ')
                    email = input('Digite o e-mail: ')
                    cpf_proprietario = input('Digite o CPF do proprietário: ')
                    Cnpj = input('Digite o CNPJ: ')
                    print('\nFornecedor ' + str(nome) + '! \nAgora  fale  localização abaixo:')
                    estado_empresa = input('Diga o estado onde empresa fica localizada: ')
                    cidade_empresa = input('Diga qual cidade: ')
                    bairro_empresa = input('Bairro: ')
                    rua_empresa = input('Rua: ')
                    numero_empresa = input('Nº  da empresa: ')

                    print('Muito obrigado(a) pela paciência ' + str(nome) + '! \nO cadastro foi realizado com sucesso!')

                    arq = open("banco.txt", "a")
                    arq.close()

                    print("----------------------------------", end="\n")
                    print("Fim do Cadastro do Fornecedor")
                    break
        elif op2==3:
            controle = 1
            while True:
                print('Cadastro de consultor\n 1 - Para cadastrar novo consultor\n 2 - Para sair')
                controle = int(input('Escolha uma opção: '))
                if (controle == 2):
                    break
                print('-' * 80, end='\n')
                if controle == 1:
                    print('\n\nOlá, vamos realizar o seu cadastro! \nInforme abaixo os dados solicitados')
                    nome = input('Digite seu nome completo: ')
                    cpf = input('Digite seu CPF: ')
                    telefone = input('Digite seu telefone/celular: ')
                    email = input('Digite seu e-mail: ')
                    formacao = input('Qual a sua formação? ')
                    experiencia = input('Quais são suas experiências na área da TI? ')
                    print('Muito obrigado(a) pela paciência ' + str(nome) + '! \nO cadastro foi realizado com sucesso!')
                    break
        elif op2==4:
            op3=1
            while True:
                print('='*30)
                print('Vamos cadastrar seu Software!')
                input()
                nome_software=str(input('Digite o nome do seu software: '))
                info_software=str(input('Faça um breve resumo de seu software: '))
                preco_software=float(input('Qual preço pretende vende-lo: '))
                input()
                print('Excelente nome :D! Agora nos diga em qual categoria abaixo seu software se encaixa melhor:\n1-Saude\n2-Educacional\n3-Empresarial\n4-Banco de dados')
                op3=int(input('Digite sua alternativa: '))
                catg=0
                if op3==1:
                    catg='Saude'
                elif op3==2:
                    catg='Educacional'
                elif op3==3:
                    catg='Empresarial'
                elif op3==4:
                    catg='Banco de dados'

                software=[nome_software,catg,info_software,preco_software,]
                input()
                print('='*30)
                input('Obrigado por cadastrar seu software, para sair pressione ENTER:')
                break
        elif op==5:
            break
    elif op==2:
        print("-" * 30)
        menu = int(input("Digite:\n 1 - para a lista de todos os softwares \n 2 - para pesquisar um software \n3 - Avaliar software "))
        avaliacao_software = 'Nenhuma'
        if menu==3:
            while True:
                print('='*30)
                nome_avaliador=input('Digite seu nome de avaliador:')
                print('Qual categoria de software voce quer avaliar:\n1-Saude\n2-Educacional\n3-Empresarial\n4-Banco de dados')
                software_procurado_1 = input('Digite sua opção:')
                if True:
                    software_procurado_1 == software
                    print('Atualmente nesta categoria possuimos estes softwares:','Seu nome é :', software[0],'Sua descrição é: ','\n',software[2])
                    input()
                    avaliacao_software=input('Digite sua avaliação para este software: ')
                    input()
                    break
        elif menu==1:
            print('Atualmente possuimos estes softwares cadastrados: \n',software[0],'\nSua categoria é: ',software[1],'\nSeu preço é: ',software[3],'\nSua avaliação é: ',avaliacao_software)
            input()
            print('Se deseja compra-lo digite 1, se não o quiser digite 2')
            op4 = int(input('Digite sua opção: '))
            if op4 == 1:
                print('='*30)
                input()
                print('Obrigado pela preferencia! \nEscolha um dos metodos disponis para prosseguir com a sua compra!')
                print('Metodos de pagamento disponiveis:')
                print('Cartao de credito, digite 1')
                print('Cartao de debito, digite 2')
                print('Boleto, digite 3')

                payment = int(input('Digite o numero condizente com método de pagamento: '))
                if payment == 1:
                    name = input('digite o nome impresso no cartao: ')
                    number = input('digite o numero do cartao: ')
                    security_code = input('digite o codigo de segurança do cartao: ')
                    due_date = input('Digite a data de vencimento do cartão: ')
                    if name and number and security_code and due_date != None:
                        print('Transação aprovada!')
                    else:
                        print('Seus dados estão incompletos, tente novamente por favor!')

                if payment == 2:
                    name = input('digite o nome impresso no cartao: ')
                    number = input('digite o numero do cartao: ')
                    security_code = input('digite a senha do cartao: ')
                    due_date = input('Digite a data de vencimento do cartão: ')
                    if name and number and security_code and due_date != None:
                        print('Transação aprovada!')
                    else:
                        print('Seus dados estão incompletos, tente novamente por favor!')

                if payment == 3:
                    first_block = random.randrange(100, 999)
                    second_block = random.randrange(10, 99)
                    thrid_block = random.randrange(10000, 99999)
                    fourth_block = random.randrange(10000, 99999)
                    fifth_block = random.randrange(100000, 999999)
                    sixth_block = random.randrange(10000, 99999)
                    seventh_block = random.randrange(10000, 99999)
                    eighth_block = random.randrange(1, 9)
                    ninth_block = random.randrange(100000000000000, 999999999999999)

                    print("Numero para o pagamento do seu boleto: ", first_block, second_block, thrid_block,
                          fourth_block, fifth_block, sixth_block, seventh_block, eighth_block, ninth_block)
                    print("O pagamento é aprovado em até 3 dias uteis apos o pagamento do boleto!")
                    input('Digite ENTER para fechar: ')
            elif op4 == 2:
                break
        elif menu == 2:
            print('Selecione a categoria do software que voce procura:\n1-Saude\n2-Educacional\n3-Empresarial\n4-Banco de dados')
            software_procurado = input('Digite sua opção:')
            if True:
                    software_procurado == software
                    print('Uma escelente escolha é o', software[0])
                    input()
            print('Se deseja compra-lo digite 1, se não o quiser digite 2')
            op4 = int(input('Digite sua opção: '))
            if op4 == 1:
                print(
                    'Obrigado pela preferencia! \nEscolha um dos metodos disponis para prosseguir com a sua compra!')
                print('Metodos de pagamento disponiveis:')
                print('Cartao de credito, digite 1')
                print('Cartao de debito, digite 2')
                print('Boleto, digite 3')

                payment = int(input('Digite o numero condizente com método de pagamento: '))
                if payment == 1:
                    name = input('digite o nome impresso no cartao: ')
                    number = input('digite o numero do cartao: ')
                    security_code = input('digite o codigo de segurança do cartao: ')
                    due_date = input('Digite a data de vencimento do cartão: ')
                    if name and number and security_code and due_date != None:
                        print('Transação aprovada!')
                    else:
                        print('Seus dados estão incompletos, tente novamente por favor!')

                if payment == 2:
                    name = input('digite o nome impresso no cartao: ')
                    number = input('digite o numero do cartao: ')
                    security_code = input('digite a senha do cartao: ')
                    due_date = input('Digite a data de vencimento do cartão: ')
                    if name and number and security_code and due_date != None:
                        print('Transação aprovada!')
                    else:
                        print('Seus dados estão incompletos, tente novamente por favor!')

                if payment == 3:
                    first_block = random.randrange(100, 999)
                    second_block = random.randrange(10, 99)
                    thrid_block = random.randrange(10000, 99999)
                    fourth_block = random.randrange(10000, 99999)
                    fifth_block = random.randrange(100000, 999999)
                    sixth_block = random.randrange(10000, 99999)
                    seventh_block = random.randrange(10000, 99999)
                    eighth_block = random.randrange(1, 9)
                    ninth_block = random.randrange(100000000000000, 999999999999999)

                    print("Numero para o pagamento do seu boleto: ", first_block, second_block, thrid_block,
                          fourth_block, fifth_block, sixth_block, seventh_block, eighth_block, ninth_block)
                    print("O pagamento é aprovado em até 3 dias uteis apos o pagamento do boleto!")
            elif op4 == 2:
                break

    elif op==3:
        while True:
            print('='*30)
            input()
            print('Python Bridge surgiu através ada necessidade um intermediador e um facilitador para empresas que procuram implantar softwares.\nNossa equipe altamente dedicada e atensiosa tem como objetivo facilitar sua vida\ne lhe mostrar oque ha de melhor no mercado atual.')
            print('=' * 30)
            input()
            break
    else:
        break
