"""
	Este projeto requer conhecimento em: Python, lógica de programação, POO.

	Instruções iniciais:
		Desenvolver uma agenda para salvar, editar, deletar e marcar um contato como favorito. O resultado da aplicação deve ser apresentado no terminal.
    
	Requisitos: 
		- Mostrar uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
		- Implementar funcionalidades para adicionar um contato (Nome, Telefone, Email, Favorito)
		- Desenvolver visualização da lista de contatos cadastrados.
		- Criar funcionalidades para editar um contato existente.
		- Implementar opção para marcar/desmarcar um contato como favorito.
		- Desenvolver visualização da lista de contatos.
		- Criar funcionalidade para apagar um contato. 
"""

listaDeContatos = [
	{ "nome": "Sofia", "telefone": "(11) 11111-0000", "favorito": True },
	{ "nome": "Gabriel", "telefone": "(82) 99999-8888", "favorito": True },
	{ "nome": "Lucas", "telefone": "(11) 91111-2222", "favorito": True},
	{ "nome": "Marcos", "telefone": "(22) 92222-3333", "favorito": False },
	{ "nome": "Jaqueline","telefone": "(33) 93333-2222", "favorito": True },
	{ "nome": "Felipe", "telefone": "(11) 88888-2222", "favorito": False },
	{ "nome": "Iure", "telefone": "(22) 33333-2222", "favorito": False },
]

def formatTelefone(numero):
	numero = ''.join(filter(str.isdigit, numero))
	if len(numero) == 11:
		return f"({numero[:2]}) {numero[2:7]}-{numero[7:]}"
	elif len(numero) == 10:
		return f"({numero[:2]}) 9{numero[2:6]}-{numero[6:]}"
	else:
		return False

class Contacts:
	def __init__(self):
		print("Bem-vindo a sua lista de contatos!")
		self.contatos = listaDeContatos
		
		# Essa variável vai armazenar a lista em ordem alfabética.
		self.contatos_ordenados = sorted(self.contatos, key=lambda c: c["nome"].lower())

		# Aqui define um tamanho padrão para todos os nomes levando em consideração o maior nome.
		self.tamanhoPad = 0
		for i in self.contatos:
			tamanho = len(i["nome"])
			if tamanho > self.tamanhoPad:
				self.tamanhoPad = tamanho
		pass

	def listarContatos(self):
		self.contatos = listaDeContatos
		self.contatos_ordenados = sorted(self.contatos, key=lambda c: c["nome"].lower())
		for i in self.contatos:
			tamanho = len(i["nome"])
			if tamanho > self.tamanhoPad:
				self.tamanhoPad = tamanho
		
		print("\n---------------------------------")
		print("Lista de Contatos:")		
		for i in self.contatos_ordenados:
			if i["favorito"] == True:
				print(f"Nome: {i["nome"].ljust(self.tamanhoPad)} {i["telefone"]} - FAVORITADO")

		for i in self.contatos_ordenados:
			if i['favorito'] == False:
				print(f"Nome: {i["nome"].ljust(self.tamanhoPad)} {i["telefone"]}")

	def adicionarContato(self):
		nome = input("Digite o nome do contato: ")
		aux = nome.split(" ")
		if len(aux) > 1:
			nome = aux[0].capitalize() + " " + aux[-1][:3].capitalize()
		else:
			nome = aux[0].capitalize()
		telefone = input("Digite o número do contato (sem formatação):\n")
		telefone = formatTelefone(telefone)
		while telefone == False:
			print("Formatação inválida. Tente Novamente.")
			telefone = input("Digite o número do contato(sem formatação):\n")
			telefone = formatTelefone(telefone)
		
		for i in self.contatos:
			if i["telefone"] == telefone:
				return print("Não foi possível cadastrar esse número, pois ele já existe, tente cadastrar outro.") 

		favorito = input("Deseja marcar como favorito(S/N): ")
		favorito = favorito.lower()
		while favorito != "s" and favorito != "n":
			print("Não foi possível compreender.")
			favorito = input("Deseja marcar como favorito(S/N): ")
			favorito = favorito.lower()
		
		if favorito == "s":
			favorito = True
		elif favorito == "n":
			favorito = False

		self.contatos.append({"nome": nome, "telefone": telefone, "favorito": favorito})

	def modificarContato(self):
		aux = 0
		print("\n-------------------------")
		for id, contato in enumerate(self.contatos_ordenados, start=1):
			if contato["favorito"] == True:
				print(f"ID: {id} - {contato["nome"].ljust(self.tamanhoPad)} {contato["telefone"]} - FAVORITO")
				aux += 1
			elif contato["favorito"] == False:
				print(f"ID: {id} - {contato["nome"].ljust(self.tamanhoPad)} {contato["telefone"]}")
				aux += 1
				
		print("ID: 0 - sair")
		modificar = input("Digite o ID do contato que você deseja modificar: ")
		if modificar == "0":
			return
		
		try:
			modificar = int(modificar)
		except:
			print("Você digitou um valor inválido.")
			print("Tente novamente.")
			return self.modificarContato()
		
		for id, contato in enumerate(self.contatos_ordenados, start=1):
			if modificar == id:
				print(f"\nContato a ser modificado: {contato['nome']}")
				print("\nO que deseja modificar:")
				value = input("1- Nome\n2- Número\n3- Favoritar/Remover favorito\n4- Remover contato\n0- Sair\n")
				
				match value:
					case "0":
						return
					case "1":
						contato["nome"] = input("Digite o novo nome: ")
					case "2":
						contato["telefone"] = input("Digite o novo número(sem formatação): ")
						contato["telefone"] = formatTelefone(contato["telefone"])
					case "3":
						if contato["favorito"] == True:
							contato["favorito"] = False
						else:
							contato["favorito"] = True
					case "4":
						self.contatos.remove(contato)
					case _:
						print("Valor não reconhecido.")
						return self.modificarContato()

running = True
start = Contacts()
while running:
	value = input("\nEscolha uma opção abaixo:\n" \
	"1- Lista de Contatos\n" \
	"2- Cadastrar Novo Contato\n" \
	"3- Modificar Contato\n" \
	"0- Finalizar Execução\n")

	match value:
		case "0":
			print("\nFim da aplicação\n")
			running = False
		
		case "1":
			start.listarContatos()

		case "2":
			start.adicionarContato()
		
		case "3":
			start.modificarContato()

		case _:
			print("Valor desconhecido...\nTente Novamente.")
