#peça a senha do usuario e se ele errar a senha 3 vezes bloquear a senha

#no python o while pode ter else
contador=1
password=123456
senha=int(input("Digite a sua senha: "))
while contador<3 and senha!=password:
    senha=int(input("Senha incorreta. Digite novamente: "))
    contador=contador+1
if contador==3 and senha!=password:
    print("Acesso bloqueado")
else:
    print("Acesso permitido.")
