arq = open("banco.txt", "w")
arq.close()

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

        arq = open("banco.txt","a")
        arq.close()

        print("----------------------------------", end="\n")


print("----------------------------------", end="\n")
print("Fim do Cadastro do Fornecedor")
