import random
import re
import time

print ('Obrigado pela preferencia! \nEscolha um dos metodos disponis para prosseguir com a sua compra!')
print ('Metodos de pagamento disponiveis:')
print ('Cartao de credito, digite 1')
print ('Cartao de debito, digite 2')
print ('Boleto, digite 3')

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
    mensagem_pagamento = "Numero para o pagamento do seu boleto: "
    
    print("Estamos processando o seu pedido...")
    time.sleep(5)
    print("."*120)
    time.sleep(3)
    print(mensagem_pagamento, first_block, second_block, thrid_block, fourth_block, fifth_block, sixth_block, seventh_block, eighth_block, ninth_block)
    time.sleep(3)
    print("O pagamento é aprovado em até 3 dias uteis após o pagamento!")