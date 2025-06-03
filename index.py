import os  # Importa a biblioteca 'os' para limpar a tela

# Lista com os tipos de roupas
Roupas = ["CAMISAS", "CALÇAS", "BERMUDAS", "SAPATOS"]

# Lista com as categorias
categoria = ["Infantil", "Feminino", "Masculino"]

# Criar matriz vazia para armazenar as marcas
marca = []
print("Digite as MARCAS para cada roupa e categoria:")

# Loop para preencher a matriz de marcas
for i in range(len(Roupas)):
    linha = []
    for j in range(len(categoria)):
        while True:
            valor = input(f"Marca para {Roupas[i]} - {categoria[j]}: ")
            if not valor.isnumeric():  # Marca não pode ser número
                linha.append(valor)
                break
            else:
                print("ERRO: Digite um nome de marca, não um número!")
    marca.append(linha)

# Criar matriz vazia para armazenar as quantidades
quantidade = []
print("\nDigite as QUANTIDADES para cada roupa e categoria:")

# Loop para preencher a matriz de quantidades
for i in range(len(Roupas)):
    linha = []
    for j in range(len(categoria)):
        while True:
            valor = input(f"Quantidade para {Roupas[i]} - {categoria[j]}: ")
            if valor.isnumeric():  # Quantidade deve ser número
                linha.append(int(valor))
                break
            else:
                print("ERRO: Digite apenas números para a quantidade!")
    quantidade.append(linha)

# Limpar a tela
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Impressão da tabela de MARCAS
print("\nMARCA")
print(" " * 12, end="")
for cat in categoria:
    print(f"{cat:^15}", end="")
print()

for i in range(len(Roupas)):
    print(f"{Roupas[i]:<12}", end="")
    for j in range(len(categoria)):
        print(f"{marca[i][j]:<15}", end="")
    print()

# Linha separadora
print("-" * 60)

# Impressão da tabela de QUANTIDADES
print("\nQUANTIDADE")
print(" " * 12, end="")
for cat in categoria:
    print(f"{cat:^15}", end="")
print()

for i in range(len(Roupas)):
    print(f"{Roupas[i]:<12}", end="")
    for j in range(len(categoria)):
        print(f"{str(quantidade[i][j]):<15}", end="")
    print()

# --------------------------------------
# IMPLEMENTAÇÃO DA BUSCA DE DADOS
# --------------------------------------

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

# Limpar a tela
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Mostrar resultado da busca
print(f"\nResultado da busca:")
print(f"Roupa: {Roupas[linha]}")
print(f"Categoria: {categoria[coluna]}")
print(f"Marca: {marca[linha][coluna]}")
print(f"Quantidade: {quantidade[linha][coluna]}")

# --------------------------------------
# IMPLEMENTAÇÃO DA ATUALIZAÇÃO DE DADOS
# --------------------------------------

print("\n=== ATUALIZAÇÃO DE DADOS ===")

# Loop para validar o número da linha
while True:
    linha_input = input("Informe o número da linha (1 a 4): ")
    if linha_input.isnumeric():
        linha = int(linha_input)
        if 1 <= linha <= len(Roupas):
            linha -= 1  # Ajusta para índice da lista (0 a 3)
            break
        else:
            print("ERRO: Linha fora do intervalo. Tente novamente.")
    else:
        print("ERRO: Digite um número válido.")

# Loop para validar o número da coluna
while True:
    coluna_input = input("Informe o número da coluna (1 a 3): ")
    if coluna_input.isnumeric():
        coluna = int(coluna_input)
        if 1 <= coluna <= len(categoria):
            coluna -= 1  # Ajusta para índice da lista (0 a 2)
            break
        else:
            print("ERRO: Coluna fora do intervalo. Tente novamente.")
    else:
        print("ERRO: Digite um número válido.")

# Mostrar dados atuais
print(f"\nDados atuais:")
print(f"Marca: {marca[linha][coluna]}")
print(f"Quantidade: {quantidade[linha][coluna]}")

# Atualizar marca com validação
while True:
    nova_marca = input("Digite a nova marca: ")
    if not nova_marca.isnumeric():  # Marca não pode ser número
        marca[linha][coluna] = nova_marca
        break
    else:
        print("ERRO: Digite um nome de marca, não um número!")

# Atualizar quantidade com validação
while True:
    nova_quantidade = input("Digite a nova quantidade: ")
    if nova_quantidade.isnumeric():
        quantidade[linha][coluna] = int(nova_quantidade)
        break
    else:
        print("ERRO: Digite apenas números para a quantidade!")

# Mostrar mensagem de confirmação
print("\nDados atualizados com sucesso!")

# Mostrar os dados atualizados
print(f"Marca atualizada: {marca[linha][coluna]}")
print(f"Quantidade atualizada: {quantidade[linha][coluna]}")


if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Impressão da tabela de MARCAS
print("\nMARCA")
print(" " * 12, end="")
for cat in categoria:
    print(f"{cat:^15}", end="")
print()

for i in range(len(Roupas)):
    print(f"{Roupas[i]:<12}", end="")
    for j in range(len(categoria)):
        print(f"{marca[i][j]:<15}", end="")
    print()

# Linha separadora
print("-" * 60)

# Impressão da tabela de QUANTIDADES
print("\nQUANTIDADE")
print(" " * 12, end="")
for cat in categoria:
    print(f"{cat:^15}", end="")
print()

for i in range(len(Roupas)):
    print(f"{Roupas[i]:<12}", end="")
    for j in range(len(categoria)):
        print(f"{str(quantidade[i][j]):<15}", end="")
    print()