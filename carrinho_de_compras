"""Programa administra uma lista de compras"""

compra =[]

print("-----------------------")
print("- Carrinho de Compras -")
print("_________")
print()

while True:
    print("1.  Adicionar Produto.")
    print("2.  Mostrar a Lista de Compras. ")
    print("3.  Eliminar Produto. ")
    print("4.  Sair do Programa. ")
    print()
    opção = input("--> ")
    print()

    if opção == "1":
        produto = input("Adicionar o produto: ").capitalize()
        if produto in compra:
            print(" Esse produto já está na lista")
        else:
            compra.append(produto)

    elif opção == "2":
        print(" Lista de Compras: ")
        for e in compra:
            print(" -", e)
            
    elif opção == "3":
        produto = input("Eliminar o produto: ").capitalize()
        if produto not in compra:
            print(" Esse produto não está na lista.")
        else:
            compra.remove(produto)

    elif opção == "4":
        break
    else:
        print("Adicionar a opção correta.")

    print()
