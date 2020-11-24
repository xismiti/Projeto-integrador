import os

print ("-" * 30)
menu = int (input("Digite:\n 1 - para a lista de todos os softwares\n 2 - para pesquisar um software\n"))
os.system('cls')

lista_nome_software = "fodase"
if menu == 1:
    print("-" * 30)
    menu_cliente = int(
        input("\n\tDigite 1 para visualizar todos softwares e 2 para ver recomendações de consultores: "))
    nome_cliente = input("\n\tDigite o nome do cliente: ")
    if menu_cliente == 1:  # exibe todos softwares
        for n in range(len(lista_nome_software)):
            print("\n\tNome Software", lista_nome_software[n])
            print("\n\tPreço software:", lista_preco_software[n])
            print("\n\tNome do fornecedor:", lista_fornecedor_software[n])
            print("\n\tInformação do software", lista_informacao_software[n])
            for o in range(len(lista_indice_recomendacao2)):
                if lista_recomendacao_cliente[o] == nome_cliente:
                    for p in range(len(lista_indice_recomendacao)):
                        if n == p:
                            print("\n\tNome do consultor:", lista_consultor_software[p])
                            print("\n\tInformações recomendação:", lista_recomendacao_software[p])
                            print("\n\tNota do software:", lista_nota_software[p])

        if menu_cliente == 2:  # exibe apenas recomendados
            for n in range(len(lista_nome_software)):
                for o in range(len(lista_indice_recomendacao2)):
                    if lista_recomendacao_cliente[o] == nome_cliente:
                        for p in range(len(lista_indice_recomendacao)):
                            if n == p:
                                print("\n\tNome Software", lista_nome_software[n])
                                print("\n\tPreço software:", lista_preco_software[n])
                                    print("\n\tNome do fornecedor:",lista_fornecedor_software[n])
                                    print("\n\tInformação do software",lista_informacao_software[n])
                                    print("\n\tNome do consultor:",lista_consultor_software[p])
                                    print("\n\tInformações recomendação:",lista_recomendacao_software[p])
                                    print("\n\tNota do software:",lista_nota_software[p])

elif menu ==2:
    print ("-" * 30)
    nome_software = input("Digite o nome do software que deseja pesquisar: ")
    os.system('cls')
    for n in range (len(lista_nome_software)):
        if lista_nome_software[n] == nome_software:
            for o in range(len(lista_indice_recomendacao2)):
                 if lista_recomendacao_cliente[o]==nome_cliente:
                     for p in range(len(lista_indice_recomendacao)):
                         if n==p:
                              print ("-" * 30)
                              print("\n\tNome Software",lista_nome_software[n])
                              print("\n\tPreço software:",lista_preco_software[n])
                              print("\n\tNome do fornecedor:",lista_fornecedor_software[n])
                              print("\n\tInformação do software",lista_informacao_software[n])
                              print("\n\tNome do consultor:",lista_consultor_software[p])
                              print("\n\tInformações recomendação:",lista_recomendacao_software[p])
                              print("\n\tNota do software:",lista_nota_software[p])
                              print ("-" * 30)

            
