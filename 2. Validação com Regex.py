import re

def validar_email(email):
    # \w aceita alfanuméricos; \. escapa o ponto
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(padrao, email))

def validar_cpf(cpf):
    # \d{3} exige três dígitos numéricos exatos
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return bool(re.match(padrao, cpf))

def validar_telefone(telefone):
    # \( e \) validam os parênteses do DDD; \s exige um espaço
    padrao = r'^\(\d{2}\)\s9\d{4}-\d{4}$'
    return bool(re.match(padrao, telefone))

def validar_data(data):
    # \d{2} e \d{4} validam o dia, mês e ano
    padrao = r'^\d{2}/\d{2}/\d{4}$'
    return bool(re.match(padrao, data))

# Testes das funções
print("=== Testes de Validação ===")
print(f"E-mail 'teste@teste.com' : {validar_email('teste@teste.com')}")
print(f"CPF '12345678900'        : {validar_cpf('12345678900')} (Faltam pontos)")
print(f"Telefone '(11) 91234-5678': {validar_telefone('(11) 91234-5678')}")
print(f"Data '2024-01-01'        : {validar_data('2024-01-01')} (Formato errado)")