def listar_eventos(eventos):
    """Exibe os eventos cadastrados no sistema."""
    print("=== SISTEMA DE GESTÃO DE EVENTOS ===")

    for evento in eventos:
        print(f"- {evento}")


eventos = [
    "Congresso de Tecnologia",
    "Feira de Inovação",
    "Semana Acadêmica"
]

listar_eventos(eventos)