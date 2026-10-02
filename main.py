def main():
	estoque = {}

	while True:
		print("\n======================================\nSistema de Estoque\n ======================================\n")
		print("1. Adicionar produto ao estoque")
		print("2. Consultar estoque")
		print("3. Sair")

		opcao = input("Escolha uma opcao: ").strip()

		if opcao == "1":
			nome = input("Nome do produto: ").strip()
			if not nome:
				print("O nome do produto nao pode ficar vazio.")
				continue

			try:
				quantidade = int(input("Quantidade a adicionar: "))
			except ValueError:
				print("Digite uma quantidade inteira valida.")
				continue

			if quantidade <= 0:
				print("A quantidade deve ser maior que zero.")
				continue

			estoque[nome] = estoque.get(nome, 0) + quantidade
			print(f"Estoque atualizado: {nome} - {estoque[nome]} unidade(s).")

		elif opcao == "2":
			if not estoque:
				print("O estoque esta vazio.")
				continue

			print("\nProdutos em estoque:")
			for nome, quantidade in sorted(estoque.items()):
				print(f"- {nome}: {quantidade} unidade(s)")

		elif opcao == "3":
			print("Sistema encerrado.")
			break

		else:
			print("Opcao invalida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
	main()
