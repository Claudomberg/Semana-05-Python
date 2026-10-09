# Dados simulados após a etapa de validação
dados_processados = {
    "total": 150,
    "validos": 132,
    "invalidos": 18,
    "erros_detalhados": [
        {"linha": 12, "campo": "email", "motivo": "Falta caractere @"},
        {"linha": 45, "campo": "cpf", "motivo": "Formato incorreto, sem traço"},
        {"linha": 89, "campo": "data", "motivo": "Data futura não permitida"}
    ]
}

taxa_sucesso = (dados_processados["validos"] / dados_processados["total"]) * 100

print("=" * 60)
# Centralizando o título em 60 caracteres
print(f"{'RELATÓRIO DE HIGIENIZAÇÃO DE DADOS':^60}")
print("=" * 60)

# Alinhando textos e limitando casas decimais
print(f"Total de Registros  : {dados_processados['total']:<10}")
print(f"Registros Válidos   : {dados_processados['validos']:<10}")
print(f"Registros Inválidos : {dados_processados['invalidos']:<10}")
print(f"Taxa de Aprovação   : {taxa_sucesso:.2f}%\n")

print("-" * 60)
print("DETALHAMENTO DE REJEIÇÕES:")

for erro in dados_processados["erros_detalhados"]:
    # Alinhando à esquerda os campos para manter a tabela organizada
    linha_format = f"Linha {erro['linha']:03d}"
    campo_format = f"{erro['campo']:<8}"
    print(f" -> {linha_format} | Campo: {campo_format} | Erro: {erro['motivo']}")

print("=" * 60)