import random
import time
import strings
import client_register
import companies_register
import leaving_warning
import purchase

# Variables
buy_menu = 0
home_menu = 0
login_menu = 0
more_option = 0
purchase_menu = 0
menu_title = strings.home_msg

time.sleep(5)
print('=' * 120)
print("""
            8888888b.         888   888                        888888b.         d8b     888                 
            888   Y88b        888   888                        888  "88b        Y8P     888                 
            888    888        888   888                        888  .88P                888                 
            888   d88P888  88888888888888b.  .d88b. 88888b.    8888888K. 888d888888 .d88888 .d88b.  .d88b.  
            8888888P" 888  888888   888 "88bd88""88b888 "88b   888  "Y88b888P"  888d88" 888d88P"88bd8P  Y8b 
            888       888  888888   888  888888  888888  888   888    888888    888888  888888  88888888888 
            888       Y88b 888Y88b. 888  888Y88..88P888  888   888   d88P888    888Y88b 888Y88b 888Y8b.     
            888        "Y88888 "Y888888  888 "Y88P" 888  888   8888888P" 888    888 "Y88888 "Y88888 "Y8888  
                           888                                                                  888         
                      Y8b d88P                                                             Y8b d88P         
                       "Y88P"                                                               "Y88P"            
                                                                                                            """)
print('=' * 120)
time.sleep(5)
print(strings.welcome)
while True:
    time.sleep(5)
    print("\n", menu_title)
    print(strings.home_menu)
    time.sleep(2)
    home_menu = int(input(strings.option))
    if home_menu == 1:
        print(strings.login_menu)
        login_menu = int(input(strings.option))
        client_register.login_setup(login_menu)
    elif home_menu == 2:
        print(strings.purchase_menu)
        purchase_menu = int(input(strings.option))
        purchase.purchase_options(purchase_menu)
    elif home_menu == 3:
        time.sleep(3)
        print("=" * 120)
        time.sleep(2)
        print(strings.more_details)
        time.sleep(2)
        print("=" * 120)
        time.sleep(3)
        print(strings.more_menu)
        more_menu = int(input(strings.option))
        if more_menu == 1:
            menu_title = "Menu principal"
            home_menu = 1
        else:
            leaving_warning.warning_message()
            break
    else:
        leaving_warning.warning_message()
        break



#        print(strings.buy_menu)
#        buy_menu = int(input(strings.option))
#        companies_register.search_companies(buy_menu)