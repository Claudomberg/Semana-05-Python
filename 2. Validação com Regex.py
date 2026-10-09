from datetime import datetime
import re

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.fullmatch(padrao, email))

def validar_cpf(cpf):
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return bool(re.fullmatch(padrao, cpf))

def cpf_sem_pontuacao(cpf):
    return bool(re.fullmatch(r'\d{11}', cpf))

def validar_telefone(telefone):
    padrao = r'^\(\d{2}\)\s9\d{4}-\d{4}$'
    return bool(re.fullmatch(padrao, telefone))

def telefone_sem_pontuacao(telefone):
    return bool(re.fullmatch(r'\d{11}', telefone))

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def data_sem_formato(data):
    for formato in ("%d-%m-%Y", "%d.%m.%Y", "%d%m%Y"):
        try:
            datetime.strptime(data, formato)
            return True
        except ValueError:
            pass
    return False

email = input("Insira o E-mail que gostaria de validar:")
cpf = input("Insira o CPF que gostaria de validar:")
numero = input("Insira o Telefone que gostaria de validar:")
data = input("Insira a Data que gostaria de validar:")


print("=== Testes de Validação ===")

if validar_email(email):
    print(f"E-mail '{email}': Válido")
else:
    print(f"E-mail '{email}': Formato inválido")

if validar_cpf(cpf):
    print(f"CPF '{cpf}': Formato válido")
elif cpf_sem_pontuacao(cpf):
    print(f"CPF '{cpf}': Faltam pontos e(ou) hífen. Exemplo: 123.456.789-00")
else:
    print(f"CPF '{cpf}': Formato inválido. Use como exemplo: 123.456.789-00")

if validar_telefone(numero):
    print(f"Telefone '{numero}': Formato válido")
elif telefone_sem_pontuacao(numero):
    print(f"Telefone '{numero}': Faltam parênteses, espaço e(ou) hífen. Exemplo: (99) 99999-9999")
else:
    print(f"Telefone '{numero}': Formato inválido")

if validar_data(data):
    print(f"Data '{data}': Válida")
elif data_sem_formato(data):
    print(f"Data '{data}': Formato incorreto. Use DD/MM/AAAA. Exemplo: 10/05/2023")
else:
    print(f"Data '{data}': Data inválida ou formato incorreto. Use DD/MM/AAAA. Exemplo: 10/05/2023")
