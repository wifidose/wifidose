tentativas = 0

max_tentativas = 3

while tentativas < max_tentativas:

usuario = input("digite seu usuario")

senha = input ("digite sua senha")



if usuario == "admin" and  senha == "12345":

 print("Acesso permitido")

 break

else:

  tentativas +=1

  print(f"acesso negado, {tentativas}, de, {max_tentativas}, tentativas")

