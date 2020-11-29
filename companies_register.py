import strings
import leaving_warning

def search_companies(option: int):
    print(strings.line)
    if option == 1:
        email = input(strings.email)
        password = input(strings.cnpj)
        info = [email, password]
        print(strings.loading_warning)
        return info
    elif option == 2:
        print(strings.buy_register)
        name = input(strings.name)
        age = input(strings.age)
        phone = input(strings.phone)
        email = input(strings.email)
        cpf = input(strings.cpf)
        cnpj = input(strings.cnpj)
        print('\nFornecedor ' + str(name) + '! \n', strings.location_msg)
        state = input('Diga o estado onde empresa fica localizada: ')
        city = input(strings.city)
        district = input(strings.district)
        street = input(strings.street)
        street_number = input(strings.street_number)
        infos = [name, age, phone, email, cpf, cnpj, state, city, district, street, street_number]
        print('Muito obrigado(a) pela preferencia' + str(name) + '! \nO cadastro foi realizado com sucesso!')
        print("=" * 120)
        return infos
    else:
        leaving_warning.warning_message()
