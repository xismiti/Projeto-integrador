import strings
import payment_methods
import leaving_warning
import time
import purchase_cart


def purchase_options(option: int):
    helpApp = ["HelpApp", "Saúde", "R$10,000", "10/10", "Descrição bla bla bla"]

    software_rate: str = "Nenhuma"
    print(strings.line)
    if option == 1:
        print('Atualmente possuimos estes softwares cadastrados: \n', helpApp[0], '\nSua categoria é: ', helpApp[1],
              '\nSeu preço é: ', helpApp[2], '\nSua avaliação é: ', helpApp[3])
        print(strings.purchase_complete_menu)
        purchase_status = int(input(strings.option))
        purchase_cart.cart(f"\nNome:, {helpApp[0]}, \nPreço:, {helpApp[2]}")
    elif option == 2:
        print(strings.type_search)
        type_search = input(strings.option)
        if type_search == helpApp[1]:
            print("Atualmente nesta categoria possuimos estes softwares: \n", "Nome: ", helpApp[0],
                  "\n Sua descrição é: ", helpApp[4])
            time.sleep(3)
            print(strings.purchase_complete_menu)
            purchase_status = int(input(strings.option))
            if purchase_status == 1:
                payment_methods.payment_methods()
            else:
                leaving_warning.warning_message()
    elif option == 3:
        name = input(strings.name)
        print(strings.rate_menu)
        chose_type = input(strings.option)
        if chose_type == helpApp[1]:
            print("Atualmente nesta categoria possuimos estes softwares:", "\nSeu nome é :", helpApp[0],
                  "\nSua descrição é:", helpApp[3])
            time.sleep(2)
            rate_description = input(strings.rate_description)
            time.sleep(2)
    else:
        leaving_warning.warning_message()
