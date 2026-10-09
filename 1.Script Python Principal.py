import csv
nome_do_arquivo = 'dados_basicos.csv'
with open(nome_do_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['email', 'cpf', 'telefone', 'data'])
    escritor.writerow(['joao@email.com', '123.456.789-00', '(11) 99999-9999', '10/05/2023'])
    escritor.writerow(['maria@email.com', '987.654.321-11', '(21) 98888-8888', '15/08/2023'])

registros_lidos = []
with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        registros_lidos.append(linha)
        print(linha)

print("=== Dados Extraídos do Arquivo ===")
for registro in registros_lidos:
    print(registro)