controle = 1
while True:
    
    print('1-Fazer Login \n2-Fazer Cadastro \n3-Sair')
    controle = int(input('Escolha uma opoção acima: '))
    
    if controle == 3:
        break
    print('-'*50, end = '\n')
    
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
            tele = input ('Digite seu telefone/celular: ')
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
