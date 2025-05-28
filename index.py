nomes = ["Murilo Caldeira","Daniel Amorim","Marcos Antonio Nunes"]

Roupas = ["CAMISAS", "CALÇAS", "BERMUDAS", "SAPATOS"]
categoria = ["Infantil", "Feminino", "Masculino"]

marca = [
    ["Balãozinho", "Adidas", "Nike"],
    ["Levi's", "Colcci", "Konik"],
    ["Hbs", "Hering", "Surfs"],
    ["Bibi", "Melissa", "Lacoste"]
]

quantidade = [
    [20, 80, 120],
    [12, 15, 20],
    [7, 25, 43],
    [32, 45, 14]
]

# Função para imprimir qualquer matriz com cabeçalhos
def imprimir_tabela(titulo, matriz):
    print(f"\n{titulo}")
    print(" " * 12, end="")  # Espaço para alinhar com os nomes das roupas
    for cat in categoria:
        print(f"{cat:^15}", end="")  # Cabeçalho centralizado
    print()
    
    for i in range(len(Roupas)):
        print(f"{Roupas[i]:<12}", end="")  # Roupas na vertical
        for j in range(len(categoria)):
            print(f"{str(matriz[i][j]):<15}", end="")  # Valores da matriz
        print()  # Nova linha

# Impressão separada com linha divisória
imprimir_tabela("MARCA", marca)

# Linha separadora
print("-" * 60)

imprimir_tabela("QUANTIDADE", quantidade)
