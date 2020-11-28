controle = 1
while True:
    print('1-Atualizar Cadastro \n2-Sair')
    controle = int(input('Escolha uma opção: '))

    if controle == 2:
        print('Obrigada pela visita')
        print('-' * 60, end = '\n')
        break
    else:
        print('-' * 60, end = '\n')
        print('Vamos atualizar o cadastro do fornecedor')
        print('-' * 60, end = '\n')
        email = input('Razão Social: ')
        senha = int(input('Digite o CNPJ: '))
        print('-' * 60, end = '\n')
        print('Descreva abaixo os dados á atualizar')
        print('-' * 60, end = '\n')

        empresa = input('Razão Social: ')
        atividade = input('Atividade econômica: ')
        cel = int(input('Nº de contato (comercial ou celular): '))
        email = input('E-mail: ')
        cpf = input('CPF do proprietário: ')
        cnpj = input('CNPJ: ')

        print('Certo! Agora vamos adicinar a nova localização')

        local = input('Estado onde a empresa fica localizada: ')
        cid = input('Cidade: ')
        bairro = input('Bairro: ')
        rua = input('Rua: ')
        num = int(input('Nº: '))

        print('Obrigado(a) pela paciência! \nAtualização feita com sucesso.')
        break
