print('='*30,'\nBem-vindo ao Python Bridge!')
print('='*30)
input()
op=1
while True:
    print('Para começar, escolha uma das opções abaixo:\n1- Cadastrar-se\n2- Comprar software\n3- Nossa historia\n4- Sair')
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
                controle = int(input('Escolha uma opoção acima: '))

                if controle == 3:
                    break
                print('-' * 50, end='\n')

                if controle == 1:
                    email = input('Digite razão social: ')
                    senha = input('Digite seu CNPJ: ')



                    print ("-" * 30)
                    menu = int (input("Digite:\n 1 - para a lista de todos os softwares\n 2 - para pesquisar um software\n"))


                    if menu == 1:
                       print ("-" * 30)
                       menu_cliente=int(input("\n\tDigite 1 para visualizar todos softwares e 2 para ver recomendações de consultores: "))
                       nome_cliente = input("\n\tDigite o nome do cliente: ")
                       if menu_cliente==1: #exibe todos softwares
                            print("\n\tNome Software",nome_software)
                            print("\n\tPreço software:",preco_software)
                            print("\n\tNome do fornecedor:",fornecedor_software)
                            print("\n\tInformação do software",informacao_software)
                            if recomendacao_cliente==nome_cliente:                          
                                print("\n\tNome do consultor:",consultor_software)
                                print("\n\tInformações recomendação:",recomendacao_software)
                                print("\n\tNota do software:",nota_software)


                      if menu_cliente==2: #exibe apenas recomendados
               
  
                        if recomendacao_cliente==nome_cliente:
                        
                                     
                             print("\n\tNome Software",nome_software)
                             print("\n\tPreço software:",preco_software)
                             print("\n\tNome do fornecedor:",fornecedor_software)
                             print("\n\tInformação do software",informacao_software)
                             print("\n\tNome do consultor:",consultor_software)
                             print("\n\tInformações recomendação:",recomendacao_software)
                             print("\n\tNota do software:",nota_software)

                  elif menu ==2:
                     print ("-" * 30)
                    nome_software = input("Digite o nome do software que deseja pesquisar: ")
                    if recomendacao_cliente==nome_cliente:
             
                        print ("-" * 30)
                        print("\n\tNome Software",nome_software)
                        print("\n\tPreço software:",preco_software)
                        print("\n\tNome do fornecedor:",fornecedor_software)
                        print("\n\tInformação do software",informacao_software)
                        print("\n\tNome do consultor:",consultor_software)
                        print("\n\tInformações recomendação:",recomendacao_software)
                        print("\n\tNota do software:",nota_software)
                        print ("-" * 30)

                    
                    
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
        elif op2==4:
            print('='*30)
            print('Vamos cadastrar seu Software!')
        else:
            break
