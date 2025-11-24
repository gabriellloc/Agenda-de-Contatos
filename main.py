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
		pass

	def listarContatos(self):
		# Essa variável vai armazenar a lista em ordem alfabética.
		contatos_ordenados = sorted(self.contatos, key=lambda c: c["nome"].lower())

		print("\n---------------------------------")
		print("Lista de Contatos:")

		# Aqui define um tamanho padrão para todos os nomes levando em consideração o maior nome.
		tamanhoPad = 0
		for i in self.contatos:
			tamanho = len(i["nome"])
			if tamanho > tamanhoPad:
				tamanhoPad = tamanho
		
		for i in contatos_ordenados:
			if i["favorito"] == True:
				print(f"Nome: {i["nome"].ljust(tamanhoPad)} {i["telefone"]} - FAVORITADO")

		for i in contatos_ordenados:
			if i['favorito'] == False:
				print(f"Nome: {i["nome"].ljust(tamanhoPad)} {i["telefone"]}")

	def adicionarContato(self):
		nome = input("Digite o nome do contato: ")
		aux = nome.split(" ")
		nome = aux[0].capitalize() + " " + aux[-1][:3].capitalize()
		telefone = input("Digite o número do contato(sem formatação):\n")
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

	



running = True
start = Contacts()
while running:
	value = input("\nEscolha uma opção abaixo:\n" \
	"1- Lista de Contatos\n" \
	"2- Cadastrar Novo Contato\n" \
	"0- Finalizar Execução.\n")

	match value:
		case "0":
			print("\nFim da aplicação\n")
			running = False
		
		case "1":
			start.listarContatos()

		case "2":
			start.adicionarContato()

		case _:
			print("Valor desconhecido...\nTente Novamente.")
