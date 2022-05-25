email = input("Informe o email:")
dominio = email.split('@')[1]
print(dominio.split('.')[0])
