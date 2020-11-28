import time

print('='*30)
avaliação=('Nenhuma avaliação foi criada para este produto.')
while True:
    print('\nEscolha uma opção:\n\n1- Fazer avaliação deste produto.\n\n2- Vizualizar avaliação anterior\n\n3-Retornar')
    print()
    opção_selecionada=int(input('Digite sua escolha: '))
    if opção_selecionada == 1:
        avaliação = str(input('Digite sua avaliação: '))
        print()
        print('Obrigado pelo feedback! Aguarde o retorno.')
        time.sleep(2)
    elif opção_selecionada == 2 :
        print('='*30)
        print()
        print('Este produto possui a seguinte avaliação:\n\n{}'.format(avaliação))
        print('=' * 30)
        print()
        input('Para retornar pressione ENTER')
    else:
         break
