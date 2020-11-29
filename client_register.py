import strings
import leaving_warning
import time
import companies_register


def login_setup(login_option: int):
    print('=' * 120)
    if login_option == 1:
        email = input(strings.email)
        password = input(strings.cpf)
        login_infos = [email, password]
        print(email, password)
        print(strings.loading_warning)
        return login_infos
    elif login_option == 2:
        print(strings.login)
        option = int(input(strings.option))
        companies_register.search_companies(option)
    elif login_option == 3:
        print(strings.register_msg)
        nome = input(strings.name)
        cpf = input(strings.cpf)
        phone = input(strings.phone)
        email = input(strings.email)
        graduation = input(strings.graduation)
        skills = input(strings.skills)
        infos = [nome, cpf, phone, email, graduation, skills]
        print('Muito obrigado(a) pela paciência ' + str(nome) + '! \nO cadastro foi realizado com sucesso!')
        return infos
    elif login_option == 4:
        print('Vamos cadastrar seu Software!')
        time.sleep(2)
        input(strings.register_msg)
        software_name = str(input(strings.software_name))
        software_info = str(input(strings.software_info))
        software_price = str(input(strings.software_price))
        time.sleep(3)
        print(strings.software_register_message)
        type = int(input(strings.option))
        category = 0
        if type == 1:
            category = 'Saude'
        elif type == 2:
            category = 'Educacional'
        elif type == 3:
            category = 'Empresarial'
        elif type == 4:
            category = 'Banco de dados'
        elif type == 5:
            description = str(input(strings.other_type))
            category = description
        else:
            leaving_warning.warning_message()
        infos = [software_name, category, software_info, software_price]
        time.sleep(2)
        input(strings.software_thanks)
        return infos
    else:
        leaving_warning.warning_message()
