import random
import strings
import leaving_warning
import time


def payment_methods():
    print(strings.line, "\n", strings.payment_message)
    time.sleep(2)
    print(strings.payment_menu)
    payment = int(input(strings.option))
    if payment == 1:
        name = input(strings.card_name)
        number = input(strings.card_number)
        security_code = input(strings.card_security_code)
        due_date = input(strings.card_due_date)
        if name and number and security_code and not due_date:
            print(strings.payment_approved)
        else:
            print(strings.payment_failed)
    elif payment == 2:
        name = input(strings.card_name)
        number = input(strings.card_number)
        security_code = input(strings.card_security_code)
        due_date = input(strings.card_due_date)
        if name and number and security_code and not due_date:
            print(strings.payment_approved)
        else:
            print(strings.payment_failed)
    elif payment == 3:
        first_block = random.randrange(100, 999)
        second_block = random.randrange(10, 99)
        thrid_block = random.randrange(10000, 99999)
        fourth_block = random.randrange(10000, 99999)
        fifth_block = random.randrange(100000, 999999)
        sixth_block = random.randrange(10000, 99999)
        seventh_block = random.randrange(10000, 99999)
        eighth_block = random.randrange(1, 9)
        ninth_block = random.randrange(100000000000000, 999999999999999)

        print("Numero para o pagamento do seu boleto: ", first_block, second_block, thrid_block, fourth_block, fifth_block,
              sixth_block, seventh_block, eighth_block, ninth_block)
        print(strings.ticket_message)
    else:
        leaving_warning.warning_message()