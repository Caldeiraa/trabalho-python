# Importa a biblioteca 'os' para permitir limpar a tela do terminal (prompt)
import os

# Criação de duas listas fixas:
Roupas = ["CAMISAS", "CALÇAS", "BERMUDAS", "SAPATOS"]  # Tipos de roupas disponíveis
categoria = ["Infantil", "Feminino", "Masculino"]      # Categorias de público

# Função que limpa a tela do terminal
def limpar_tela():
    # Se o sistema for Windows ('nt'), usa o comando 'cls', senão usa 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que preenche uma "matriz" com marcas ou quantidades
def preencher_matriz(tipo):
    matriz = []  # Cria uma lista vazia que será uma matriz
    print(f"\nDigite as {tipo.upper()} para cada roupa e categoria:")

    # Laço para percorrer cada tipo de roupa
    for i in range(len(Roupas)):
        linha = []  # Lista vazia que representa uma linha da matriz

        # Laço para percorrer cada categoria para aquela roupa
        for j in range(len(categoria)):
            while True:
                # Pede o valor ao usuário (marca ou quantidade)
                valor = input(f"{tipo} para {Roupas[i]} - {categoria[j]}: ")

                # Se o tipo for 'Marca', só pode aceitar letras (nenhum número)
                if tipo == "Marca" and not valor.isnumeric():
                    linha.append(valor)  # Adiciona o valor à linha
                    break
                # Se o tipo for 'Quantidade', só pode aceitar números
                elif tipo == "Quantidade" and valor.isnumeric():
                    linha.append(int(valor))  # Converte para inteiro e adiciona
                    break
                else:
                    print(f"ERRO: Digite um valor válido para {tipo}!")

        # Após preencher a linha inteira, adiciona à matriz
        matriz.append(linha)

    return matriz  # Retorna a matriz preenchida

# Função que imprime uma matriz de forma formatada na tela
def imprimir_matriz(titulo, matriz):
    print(f"\n{titulo}")  # Imprime o título
    print(" " * 12, end="")  # Espaço para alinhar com as categorias

    # Imprime o nome das categorias centralizados
    for cat in categoria:
        print(f"{cat:^15}", end="")  # ^ centraliza em 15 espaços
    print()

    # Imprime as linhas da matriz
    for i in range(len(Roupas)):
        print(f"{Roupas[i]:<12}", end="")  # Imprime o nome da roupa alinhado à esquerda
        for j in range(len(categoria)):
            print(f"{str(matriz[i][j]):<15}", end="")  # Imprime o valor da célula
        print()  # Pula para a próxima linha

    print("-" * 60)  # Linha separadora

# Função para buscar dados a partir de roupa e categoria informados
def buscar_dados():
    print("\n=== BUSCA DE DADOS ===")

    # Solicita a roupa até que seja uma válida
    while True:
        busca_roupa = input("Informe a roupa para busca (CAMISAS, CALÇAS, BERMUDAS, SAPATOS): ").upper()
        if busca_roupa in Roupas:
            linha = Roupas.index(busca_roupa)
            break
        else:
            print("ERRO: Roupa inválida. Tente novamente.")

    # Solicita a categoria até que seja uma válida
    while True:
        busca_categoria = input("Informe a categoria para busca (Infantil, Feminino, Masculino): ").capitalize()
        if busca_categoria in categoria:
            coluna = categoria.index(busca_categoria)
            break
        else:
            print("ERRO: Categoria inválida. Tente novamente.")

    return linha, coluna  # Retorna a posição (linha e coluna)

# Função para atualizar os dados de uma posição da matriz
def atualizar_dados(marca, quantidade):
    print("\n=== ATUALIZAÇÃO DE DADOS ===")

    # Solicita o número da linha (1 até o total de roupas)
    while True:
        linha_input = input(f"Número da linha (1 a {len(Roupas)}): ")
        if linha_input.isnumeric():
            linha = int(linha_input) - 1  # Converte e ajusta para índice da lista (começa do 0)
            if 0 <= linha < len(Roupas):
                break
            else:
                print("ERRO: Linha fora do intervalo.")
        else:
            print("ERRO: Digite um número válido.")

    # Solicita o número da coluna (1 até o total de categorias)
    while True:
        coluna_input = input(f"Número da coluna (1 a {len(categoria)}): ")
        if coluna_input.isnumeric():
            coluna = int(coluna_input) - 1
            if 0 <= coluna < len(categoria):
                break
            else:
                print("ERRO: Coluna fora do intervalo.")
        else:
            print("ERRO: Digite um número válido.")

    limpar_tela()  # Limpa a tela antes de mostrar os dados atuais

    # Mostra os dados atuais daquela posição
    print(f"\nDados atuais:\nMarca: {marca[linha][coluna]}\nQuantidade: {quantidade[linha][coluna]}")

    # Confirma se o usuário deseja realmente atualizar esses dados
    certeza = input("\nCerteza que são esses dados que deseja atualizar?\n 1- Sim ou 2- Não\n")
    print("")
    if certeza == "1":
        # Solicita a nova marca (somente texto)
        while True:
            nova_marca = input("Nova marca: ").strip()
            if not nova_marca:
                print("ERRO: O campo marca não pode ficar vazio!")
            elif not nova_marca.isnumeric():
                marca[linha][coluna] = nova_marca
                break
            else:
                print("ERRO: Digite um nome de marca válido.")

        # Solicita a nova quantidade (somente números)
        while True:
            nova_quantidade = input("Nova quantidade: ").strip()
            if not nova_quantidade:
                print("ERRO: O campo quantidade não pode ficar vazio!")
            elif nova_quantidade.isnumeric():
                quantidade[linha][coluna] = int(nova_quantidade)
                break
            else:
                print("ERRO: Digite apenas números.")

        # Confirma que a atualização foi feita
        print("\nDados atualizados com sucesso!")
        print(f"Marca atualizada: {marca[linha][coluna]}")
        print(f"Quantidade atualizada: {quantidade[linha][coluna]}")
    else:
        menu()  # Volta para o menu principal

# Função principal do programa (menu com as opções)
def menu():
    marca = None       # Variável que guardará a matriz de marcas
    quantidade = None  # Variável que guardará a matriz de quantidades

    # Laço infinito até o usuário decidir sair
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Cadastrar Marcas e Quantidades")
        print("2 - Imprimir Tabelas")
        print("3 - Buscar Dados")
        print("4 - Atualizar Dados")
        print("5 - Limpar tela")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        # Opção 1: Cadastra as marcas e quantidades
        if escolha == '1':
            marca = preencher_matriz("Marca")
            quantidade = preencher_matriz("Quantidade")
            print("\nCadastro realizado com sucesso!")
            limpar_tela()

        # Opção 2: Imprime as tabelas, se já estiverem cadastradas
        elif escolha == '2':
            limpar_tela()
            if marca is None or quantidade is None:
                print("ERRO: Cadastre as marcas e quantidades primeiro (opção 1).")
            else:
                imprimir_matriz("MARCAS", marca)
                imprimir_matriz("QUANTIDADES", quantidade)

        # Opção 3: Busca dados de uma peça específica
        elif escolha == '3':
            if marca is None or quantidade is None:
                print("ERRO: Cadastre as marcas e quantidades primeiro (opção 1).")
            else:
                linha, coluna = buscar_dados()
                print("\nResultado da busca:")
                print(f"Roupa: {Roupas[linha]}")
                print(f"Categoria: {categoria[coluna]}")
                print(f"Marca: {marca[linha][coluna]}")
                print(f"Quantidade: {quantidade[linha][coluna]}")

        # Opção 4: Atualiza uma marca e quantidade
        elif escolha == '4':
            if marca is None or quantidade is None:
                print("ERRO: Cadastre as marcas e quantidades primeiro (opção 1).")
            else:
                atualizar_dados(marca, quantidade)

        # Opção 5: Apenas limpa a tela
        elif escolha == '5':
            limpar_tela()

        # Opção 0: Encerra o programa
        elif escolha == '0':
            print("Saindo do programa... Até mais!")
            break

        # Caso a pessoa digite algo inválido
        else:
            print("Opção inválida! Tente novamente.")

# Parte que inicia o programa
if __name__ == "__main__":
    menu()         # Chama o menu principal
    limpar_tela()  # Limpa a tela quando o programa finalizar
