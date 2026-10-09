import csv

def processar_arquivo_seguro(caminho_arquivo):
    print("=== Iniciando Processamento ===")
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            primeira_linha = next(leitor)
            
            # Simulando acesso a uma coluna que pode não existir (KeyError)
            idade_texto = primeira_linha['idade']
            
            # Simulando conversão de tipo que pode falhar (ValueError)
            idade_numero = int(idade_texto)
            
    except FileNotFoundError:
        print("[ERRO] Arquivo não encontrado. Verifique o caminho especificado.")
    except KeyError as erro:
        print(f"[ERRO] Coluna ausente na estrutura do arquivo: {erro}")
    except ValueError:
        print("[ERRO] Falha de conversão. O valor fornecido não é um número válido.")
    else:
        print("[SUCESSO] O arquivo foi lido e processado sem nenhum erro!")
    finally:
        print("[STATUS] Operação de leitura finalizada.")

# Testando com um arquivo que não existe para acionar o FileNotFoundError
processar_arquivo_seguro("arquivo_inexistente.csv")