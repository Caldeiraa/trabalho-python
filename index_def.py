import os  # Biblioteca para limpar a tela

# Listas fixas com os tipos de roupas e categorias
Roupas = ["CAMISAS", "CALÇAS", "BERMUDAS", "SAPATOS"]
categoria = ["Infantil", "Feminino", "Masculino"]

# Função para limpar a tela, dependendo do sistema operacional
def limpar_tela():
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Se for Linux ou Mac
        os.system('clear')

# Função para preencher uma matriz (marca ou quantidade)
def preencher_matriz(tipo):
    matriz = []
    print(f"\nDigite as {tipo.upper()} para cada roupa e categoria:")
    for i in range(len(Roupas)):
        linha = []
        for j in range(len(categoria)):
            while True:
                valor = input(f"{tipo} para {Roupas[i]} - {categoria[j]}: ")
                if tipo == "Marca" and not valor.isnumeric():
                    linha.append(valor)
                    break
                elif tipo == "Quantidade" and valor.isnumeric():
                    linha.append(int(valor))
                    break
                else:
                    print(f"ERRO: Digite um valor válido para {tipo}!")
        matriz.append(linha)
    return matriz

# Função para imprimir uma matriz formatada
def imprimir_matriz(titulo, matriz):
    print(f"\n{titulo}")
    print(" " * 12, end="")
    for cat in categoria:
        print(f"{cat:^15}", end="")
    print()
    for i in range(len(Roupas)):
        print(f"{Roupas[i]:<12}", end="")
        for j in range(len(categoria)):
            print(f"{str(matriz[i][j]):<15}", end="")
        print()
    print("-" * 60)

# Função para buscar dados via nome de roupa e categoria
def buscar_dados():
    print("\n=== BUSCA DE DADOS ===")
    while True:
        busca_roupa = input("Informe a roupa para busca (CAMISAS, CALÇAS, BERMUDAS, SAPATOS): ").upper()
        if busca_roupa in Roupas:
            linha = Roupas.index(busca_roupa)
            break
        else:
            print("ERRO: Roupa inválida. Tente novamente.")
    while True:
        busca_categoria = input("Informe a categoria para busca (Infantil, Feminino, Masculino): ").capitalize()
        if busca_categoria in categoria:
            coluna = categoria.index(busca_categoria)
            break
        else:
            print("ERRO: Categoria inválida. Tente novamente.")
    return linha, coluna

# Função para atualizar dados em uma posição específica
def atualizar_dados(marca, quantidade):
    print("\n=== ATUALIZAÇÃO DE DADOS ===")
    while True:
        linha_input = input(f"Informe o número da linha (1 a {len(Roupas)}): ")
        if linha_input.isnumeric():
            linha = int(linha_input) - 1
            if 0 <= linha < len(Roupas):
                break
            else:
                print("ERRO: Linha fora do intervalo.")
        else:
            print("ERRO: Digite um número válido.")
    while True:
        coluna_input = input(f"Informe o número da coluna (1 a {len(categoria)}): ")
        if coluna_input.isnumeric():
            coluna = int(coluna_input) - 1
            if 0 <= coluna < len(categoria):
                break
            else:
                print("ERRO: Coluna fora do intervalo.")
        else:
            print("ERRO: Digite um número válido.")
    print(f"\nDados atuais:\nMarca: {marca[linha][coluna]}\nQuantidade: {quantidade[linha][coluna]}")
    while True:
        nova_marca = input("Digite a nova marca: ")
        if not nova_marca.isnumeric():
            marca[linha][coluna] = nova_marca
            break
        else:
            print("ERRO: Digite um nome de marca, não um número!")
    while True:
        nova_quantidade = input("Digite a nova quantidade: ")
        if nova_quantidade.isnumeric():
            quantidade[linha][coluna] = int(nova_quantidade)
            break
        else:
            print("ERRO: Digite apenas números para a quantidade!")
    print("\nDados atualizados com sucesso!")
    print(f"Marca atualizada: {marca[linha][coluna]}")
    print(f"Quantidade atualizada: {quantidade[linha][coluna]}")

# Função principal que exibe o menu e executa as opções
def menu():
    marca = None
    quantidade = None
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Cadastrar Marcas e Quantidades")
        print("2 - Imprimir Tabelas")
        print("3 - Buscar Dados")
        print("4 - Atualizar Dados")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        limpar_tela()

        if escolha == '1':
            # Cadastra as matrizes marca e quantidade
            marca = preencher_matriz("Marca")
            quantidade = preencher_matriz("Quantidade")
            print("\nCadastro realizado com sucesso!")
        elif escolha == '2':
            # Imprime as matrizes se já estiverem cadastradas
            if marca is None or quantidade is None:
                print("ERRO: Cadastre as marcas e quantidades primeiro (opção 1).")
            else:
                imprimir_matriz("MARCA", marca)
                imprimir_matriz("QUANTIDADE", quantidade)
        elif escolha == '3':
            # Busca dados se matrizes já cadastradas
            if marca is None or quantidade is None:
                print("ERRO: Cadastre as marcas e quantidades primeiro (opção 1).")
            else:
                linha, coluna = buscar_dados()
                limpar_tela()
                print("\nResultado da busca:")
                print(f"Roupa: {Roupas[linha]}")
                print(f"Categoria: {categoria[coluna]}")
                print(f"Marca: {marca[linha][coluna]}")
                print(f"Quantidade: {quantidade[linha][coluna]}")
        elif escolha == '4':
            # Atualiza dados se matrizes já cadastradas
            if marca is None or quantidade is None:
                print("ERRO: Cadastre as marcas e quantidades primeiro (opção 1).")
            else:
                atualizar_dados(marca, quantidade)
        elif escolha == '0':
            print("Saindo do programa... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa chamando o menu
if __name__ == "__main__":
    limpar_tela()
    menu()
