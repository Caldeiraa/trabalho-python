# Importa a biblioteca 'os' para permitir limpar a tela do terminal (prompt)
import os
import time

# --- 👕 LISTAS PRINCIPAIS COM EMOJIS 👟 ---
Roupas = ["👕 CAMISAS", "👖 CALÇAS", "🩳 BERMUDAS", "👟 SAPATOS"]
categoria = ["👶 Infantil", "👩 Feminino", "👨 Masculino"]

# Listas sem emoji para usar em prompts de input mais limpos
Roupas_sem_emoji = [s.split(" ")[1] for s in Roupas]
categoria_sem_emoji = [s.split(" ")[1] for s in categoria]

# Função que limpa a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que preenche uma "matriz" com validação contra entradas vazias
def preencher_matriz(tipo):
    matriz = []
    print(f"\n--- 📝 CADASTRO DE {tipo.upper()} ---")

    for i in range(len(Roupas)):
        linha = []
        for j in range(len(categoria)):
            while True:
                valor = input(f"  ↳ {tipo} para {Roupas[i]} - {categoria[j]}: ").strip()

                if not valor:
                    print("  ⚠️  ERRO: Este campo não pode ser vazio. Tente novamente.")
                    continue

                if tipo == "Marca":
                    if not valor.isnumeric():
                        linha.append(valor)
                        break
                    else:
                        print("  ⚠️  ERRO: Uma marca não pode ser composta apenas por números.")
                elif tipo == "Quantidade":
                    if valor.isnumeric():
                        linha.append(int(valor))
                        break
                    else:
                        print(f"  ⚠️  ERRO: Digite um valor numérico para a quantidade!")
        matriz.append(linha)
    return matriz

# Função que imprime uma matriz de forma formatada na tela
def imprimir_matriz(titulo, matriz):
    print(f"\n\n--- 📊 TABELA DE {titulo} 📊 ---")
    print(" " * 15, end="")
    for cat in categoria:
        print(f"{cat:^18}", end="")
    print("\n" + "═" * 75)

    for i in range(len(Roupas)):
        print(f"{Roupas[i]:<15}", end="")
        for j in range(len(categoria)):
            print(f"{str(matriz[i][j]):^18}", end="")
        print()
    print("═" * 75)

# Função para buscar dados a partir de roupa e categoria informados
def buscar_dados():
    print("\n--- 🔍 BUSCA/SELEÇÃO DE ITEM ---")
    while True:
        busca_roupa = input(f"  👉  Informe a roupa ({', '.join(Roupas_sem_emoji)}): ").upper()
        if busca_roupa in Roupas_sem_emoji:
            linha = Roupas_sem_emoji.index(busca_roupa)
            break
        else:
            print("  ⚠️  ERRO: Roupa inválida. Tente novamente.")

    while True:
        busca_categoria = input(f"  👉  Informe a categoria ({', '.join(categoria_sem_emoji)}): ").capitalize()
        if busca_categoria in categoria_sem_emoji:
            coluna = categoria_sem_emoji.index(busca_categoria)
            break
        else:
            print("  ⚠️  ERRO: Categoria inválida. Tente novamente.")
    return linha, coluna

# Função para atualizar os dados de forma mais intuitiva
def atualizar_dados(marca, quantidade):
    print("\n--- 🔄  ATUALIZAÇÃO DE DADOS ---")
    print("Primeiro, vamos encontrar o item que você deseja atualizar.")
    linha, coluna = buscar_dados()
    limpar_tela()

    print("\n📋  DADOS ATUAIS DO ITEM SELECIONADO:")
    print(f"   Roupa: {Roupas[linha]}")
    print(f"   Categoria: {categoria[coluna]}")
    print(f"   Marca Atual: {marca[linha][coluna]}")
    print(f"   Quantidade Atual: {quantidade[linha][coluna]}")

    certeza = input("\n🤔 Certeza que deseja atualizar este item? (1 para Sim, 2 para Não): ")
    print("")

    if certeza == "1":
        while True:
            nova_marca = input("   ⌨️  Digite a nova marca: ").strip()
            if not nova_marca:
                print("  ⚠️ ERRO: O campo marca não pode ficar vazio!")
            elif nova_marca.isnumeric():
                print("  ⚠️ ERRO: Digite um nome de marca válido (apenas texto).")
            else:
                marca[linha][coluna] = nova_marca
                break
        while True:
            nova_quantidade = input("   ⌨️  Digite a nova quantidade: ").strip()
            if not nova_quantidade:
                print("  ⚠️ ERRO: O campo quantidade não pode ficar vazio!")
            elif nova_quantidade.isnumeric():
                quantidade[linha][coluna] = int(nova_quantidade)
                break
            else:
                print("  ⚠️ ERRO: Digite apenas números para a quantidade.")

        print("\n✅ ✨ Dados atualizados com sucesso! ✨")
        print(f"   Nova Marca para {Roupas[linha]} - {categoria[coluna]}: {marca[linha][coluna]}")
        print(f"   Nova Quantidade: {quantidade[linha][coluna]}")
    else:
        print("❌  Operação de atualização cancelada.")

# Função principal do programa (menu com as opções)
# Função principal do programa (menu com as opções)
def menu():
    marca = None
    quantidade = None

    while True:
        print("\n╔════════════════════════════════════════╗")
        print("║      👟 SISTEMA DE ESTOQUE 👟          ║")
        print("║          ✨ LOJA FASHION ✨            ║")
        print("╚════════════════════════════════════════╝")
        print("1️⃣  - Cadastrar Marcas e Quantidades")
        print("2️⃣  - Imprimir Tabelas de Estoque")
        print("3️⃣  - Buscar um Item Específico")
        print("4️⃣  - Atualizar um Item")
        print("5️⃣  - Limpar a Tela")
        print("0️⃣  - Sair do Sistema")
        escolha = input("\nDigite sua escolha ⌨️  : ")

        if escolha == '1':
            limpar_tela()
            marca = preencher_matriz("Marca")
            quantidade = preencher_matriz("Quantidade")
            print("\n✔️  Cadastro realizado com sucesso!")
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()
        elif escolha == '2':
            limpar_tela()
            if marca is None or quantidade is None:
                print("🚫  ERRO: Cadastre as marcas e quantidades primeiro (opção 1).")
            else:
                imprimir_matriz("MARCAS", marca)
                imprimir_matriz("QUANTIDADES", quantidade)
        elif escolha == '3':
            limpar_tela()
            if marca is None or quantidade is None:
                print("🚫  ERRO: Cadastre as marcas e quantidades primeiro (opção 1).")
            else:
                linha, coluna = buscar_dados()
                print("\n--- 🎯  RESULTADO DA BUSCA ---")
                print(f"  Roupa: {Roupas[linha]}")
                print(f"  Categoria: {categoria[coluna]}")
                print(f"  Marca: {marca[linha][coluna]}")
                print(f"  Quantidade: {quantidade[linha][coluna]}")
        elif escolha == '4':
            limpar_tela()
            if marca is None or quantidade is None:
                print("🚫 ERRO: Cadastre as marcas e quantidades primeiro (opção 1).")
            else:
                atualizar_dados(marca, quantidade)
        elif escolha == '5':
            limpar_tela()

        # ✅ CORREÇÃO APLICADA AQUI ✅
        elif escolha == '0':
            print("\n👋 Saindo do programa... Até mais!\n PARTICIPANTES \n Daniel, Marcos, Murilo")
            time.sleep(2) # Pausa por 2 segundos para a mensagem ser lida
            break # Encerra o loop
            
        else:
            print("\n❓ Opção inválida! Por favor, tente novamente.")

# Parte que inicia o programa
if __name__ == "__main__":
    limpar_tela()
    menu()
    # A LINHA ABAIXO FOI REMOVIDA PARA NÃO APAGAR A MENSAGEM DE DESPEDIDA
    # limpar_tela()