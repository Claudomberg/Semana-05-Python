import csv

def processar_arquivo_seguro(caminho_arquivo):
    print("=== Iniciando Processamento ===")

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            primeira_linha = next(leitor)

            idade_texto = primeira_linha['idade']
            idade_numero = int(idade_texto)

    except FileNotFoundError:
        print("[ERRO] Arquivo não encontrado.")

    except KeyError as erro:
        print(f"[ERRO] Coluna ausente: {erro}")

    except ValueError:
        print("[ERRO] A idade não é um número válido.")

    except StopIteration:
        print("[ERRO] O arquivo não possui registros.")

    else:
        print(f"[SUCESSO] Idade processada: {idade_numero}")

    finally:
        print("[STATUS] Operação de leitura finalizada.")

processar_arquivo_seguro("dados.csv")
