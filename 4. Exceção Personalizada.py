class FormatoInvalidoError(Exception):
    "Erro lançado quando o CPF está em formato inválido."
    pass

def validar_cpf(cpf):
    import re

    padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

    if not re.fullmatch(padrao, cpf):
        raise FormatoInvalidoError(
            f"CPF '{cpf}' está em formato inválido. "
            "Use 123.456.789-00."
        )

    print("Formato do CPF válido!")

try:
    validar_cpf("12345678900")
except FormatoInvalidoError as erro:
    print(f"[ERRO DE FORMATO] {erro}")
