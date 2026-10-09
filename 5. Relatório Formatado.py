dados_processados = {
    "total": 150,
    "validos": 132,
    "invalidos": 18
}

total = dados_processados["total"]
validos = dados_processados["validos"]
invalidos = dados_processados["invalidos"]

taxa_aprovacao = (validos / total) * 100
taxa_rejeicao = (invalidos / total) * 100

print("=" * 60)
print(f"{'RELATÓRIO FINAL DE VALIDAÇÃO DE DADOS':^60}")
print("=" * 60)

print(f"{'Total de registros analisados:':<35} {total:>10}")
print(f"{'Registros válidos:':<35} {validos:>10}")
print(f"{'Registros inválidos:':<35} {invalidos:>10}")

print("-" * 60)
print(f"{'Taxa de aprovação:':<35} {taxa_aprovacao:>9.2f}%")
print(f"{'Taxa de rejeição:':<35} {taxa_rejeicao:>9.2f}%")

print("=" * 60)

if invalidos == 0:
    print("Status: Todos os registros foram aprovados!")
else:
    print(f"Status: {invalidos} registros precisam de correção.")

print("=" * 60)
