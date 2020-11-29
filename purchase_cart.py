import strings
import time
import payment_methods
import leaving_warning


def cart(itens: str):
    print(strings.cart_itens, itens)
    time.sleep(2)
    print(strings.purchase_complete_menu)
    purchase = input(strings.option)
    if purchase == 1:
        payment_methods.payment_methods()
    elif purchase == 2:
        leaving_warning.warning_message()