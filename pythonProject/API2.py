import requests #importando biblioteca do python
#consulta de ceps
def consulta(opcao):
    if opcao!=1:
        print("VEFIFICAÇÃO DE CEP's")
        cep=input("Digite o seu CEP: ")
        if len(cep)!=8:
            print("Cep Inválido")
            exit()
        consulta=requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados=consulta.json()  #o retorno será atribuido a essa variavel dados
        #print(dados)
        print(dados["cep"])
        print(dados["logradouro"])
        print(dados["bairro"])
        print(dados["localidade"])
        print(dados["uf"])
    else:
        print("FIM DO PROGRAMA")
        exit()


