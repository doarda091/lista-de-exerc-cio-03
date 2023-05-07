usuarios = []

while True:
    nome = input("Digite o nome do usuário (ou 'sair' para finalizar o cadastro): ")
    if nome.lower() == "sair":
        break
    idade = int(input("Digite a idade do usuário: "))
    email = input("Digite o e-mail do usuário: ")

    usuario = {"nome": nome, "idade": idade, "email": email}

    usuarios.append(usuario)

print("Usuários cadastrados:")
for usuario in usuarios:
    print(usuario)