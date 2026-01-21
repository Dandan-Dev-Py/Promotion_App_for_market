planilha_produtos = open('/home/dangerous/Python/Promotion_App_for_market/Produtos.txt', 'a')

def Produtos(planilha, comand):

    if comand == "a":
        planilha.write(input("qual o nome do produto? ") + "\n")
        print("produto adicionado")
        planilha.close()

    return planilha   

    if comand == "v":
        print(planilha.read())
    return planilha

    if comand == "d":
        print("opção não implementada")
        break


abrir = input("deseja abrir a planilha de produtos? s/n ")

if abrir == "s":
    comando = input("deseja adicionar um produto, visualizar a planilha ou apagar um produto? a/v/d ")
    Produtos(planilha_produtos, comando)
        
print("planilha aberta com sucesso")

if abrir == "n":
    print("ok, até mais")
    break

print(abrir)