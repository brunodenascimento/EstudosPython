#criando função emm python

def funcaoimprime_nome(nome):
    print("nome "+nome)


#funcao exercicio1
def exercicio1(x):
    for contador in range (0, x+1, 1):
        print()
        for contador1 in range (0, contador, 1):
            print(contador, end=" ")

#funcao exercicio2

def exercicio2(x):
    for contador in range (0, x+1, 1):
        print()
        for contador1 in range (0, contador, 1):
            print(contador1+1, end=" ")

def exercicio3(texto):
    print(f"O texto ({texto}) tem {len(texto)} caracteres.")
def exercicio4(texto):
    for contador in range (0, len(texto), 1):
        print(texto[contador], end=" ") #no python o texto funciona como um array, cada caractere é uma posição

def exercicio5(texto):
    espacos=0
    for contador in range (0,len(texto), 1):
        if texto[contador]==" ":
            espacos=espacos+1
    print(espacos)

def exercicio6(texto):
    quantidadevogais=0
    for contador in texto: #esse for é mais simplificado para analisar os caracteres do texto e o contrador vira uma string
        if contador in "aeiouAEIOU":
            quantidadevogais=quantidadevogais+1
    print(f"a frase {texto} tem {quantidadevogais} vogais")

def exercicio7(nome, quantidade, valor):
        valortotal=quantidade*valor
        return f"Você tem R${quantidade} em {nome}"

def exercicio8 (numero1, numero2):
    soma=numero1+numero2
    return soma

def exercicio9(*num):
    soma=0
    for contador in range (0, len(num), 1):
        soma=soma+num[contador]
    return soma

def exercicio10(texto1):
    tamanho=len(texto1)
    totalletras=0
    for contador in range (tamanho-1, -1, -1):
        print(texto1[contador], end="")
        if texto1[contador]!=" " and texto1[contador] !="." and texto1[contador]!=",":
            totalletras=totalletras+1
    print("\n", totalletras)

def exercicio11(text):
    print(text[::-1])

def exercicio12(lista):
    listanova = []
    for contador in lista:
        if contador not in listanova:
            listanova.append(contador)
    print(listanova)

def exercicio121(lista):
    listanova=set(lista)#esse comando automaticamente cria um conjunto que só recebe os valores que não são repetidos e em ordem crescente
    print(listanova)

def exercicio13(numero):
    if numero!=1:
        for contador in range (2, numero-1, 1):
            if numero%contador==0:
                return f"Esse número não é primo"
    return f"Esse número é primo"t









