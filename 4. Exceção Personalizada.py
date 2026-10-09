class IdadeInvalidaError(Exception):
    """Exceção lançada quando a idade informada está fora do limite permitido (ex: menores de 18)."""
    def __init__(self, idade_informada, mensagem="Acesso negado: Usuário menor de idade."):
        self.idade_informada = idade_informada
        self.mensagem = f"{mensagem} (Idade informada: {self.idade_informada})"
        super().__init__(self.mensagem)

def registrar_cliente(nome, idade):
    print(f"\nTentando registrar: {nome}...")
    if idade < 18:
        raise IdadeInvalidaError(idade)
    print("Cliente registrado com sucesso!")

# Bloco de execução para capturar a exceção personalizada
try:
    registrar_cliente("Carlos", 25)  # Funciona
    registrar_cliente("Ana", 16)     # Dispara o IdadeInvalidaError
except IdadeInvalidaError as erro:
    print(f"[ERRO DE NEGÓCIO] {erro}")