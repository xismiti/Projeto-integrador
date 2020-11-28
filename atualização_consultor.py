controle=1
while True:
    print('1 - Atualização cadastral\n2 - Sair')
    controle=int(input('Escolha uma opção: '))
    if controle==2:
        print('Agradecemos pela sua visita!')
        print('-'*80, end='\n')
        break
    else:
        print('-'*80, end='\n')
        print('Vamos atualizar o cadastro do consultor')
        print('-'*80, end='\n')
        nome=input('Digite seu nome completo: ')
        senha=int(input('Digite seu CPF: '))
        print('-'*80, end='\n')
        print('Preencha abaixo os dados que deseja atualizar')
        print('-'*80, end='\n')
        telefone = input('Digite seu telefone/celular: ')
        email=input('Digite seu e-mail: ')
        formacao=input('Qual a sua formação? ')
        experiencia=input('Quais são suas experiências na área da TI? ')
        taxa_comissao=int(input('Digite quanto você cobra pela consultoria (em porcentagem): '))
        comissao=0
        print('Muito obrigado(a) pela paciência ' + str(nome) + '! \nO cadastro foi realizado com sucesso!')
        break
