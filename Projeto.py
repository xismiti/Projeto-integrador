#variaveis "op" e "op2" são referentes ao menus de opções

print('='*30,'\nBem-vindo ao Pyrhon Bridge!')
print('='*30)
input()
op=1
while True:
    print('Para começar, escolha uma das opções abaixo:\n1- Cadastrar-se\n2- Comprar software\n3- Nossa historia\n4- Sair')
    print('=' * 30)
    op = int(input('Digite sua opção: '.strip()))
    if op==1:
        print('Voce deseja:\n1-Cadastrar-se como cliente\n2-Cadastrar-se como empresa\n3- Cadastrar-se como consultor\n4-Sair')
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
            controle = int(input('Escolha uma opoção acima: '))

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

                nome = input('Digite a razão social da empresa: ')
                idade = input('Digite atividade econômica da empresa: ')
                tele = input('Digite o número de contato ( comercial ou celular): ')
                email = input('Digite o e-mail: ')
                cpf = input('Digite o CPF do proprietário: ')
                Cnpj = input('Digite o CNPJ: ')
                print('\nFornecedor ' + str(nome) + '! \nAgora  fale  localização abaixo:')
                estado = input('Diga o estado onde empresa fica localizada: ')
                cidade = input('Diga qual cidade: ')
                bairro = input('Bairro: ')
                rua = input('Rua: ')
                numero = input('Nº  da empresa: ')

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
                tele = input('Digite seu telefone/celular: ')
                email = input('Digite seu e-mail: ')
                formacao = input('Qual a sua formação? ')
                experiencia = input('Quais são suas experiências na área da TI? ')
                print('Muito obrigado(a) pela paciência ' + str(nome) + '! \nO cadastro foi realizado com sucesso!')
                break
    else:
        break










