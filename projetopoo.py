#A classe Biblioteca deve manter um catálogo de livros disponíveis, um registro de membros e 
#métodos para operações como empréstimo, devolução e pesquisa de livros.
#Operações da Biblioteca:
#Implementar métodos na classe Biblioteca para adicionar livros ao catálogo, adicionar membros à biblioteca, 
#permitir empréstimo de livros por membros, registrar a devolução de livros e pesquisar livros por título,
#autor ou ID.
#Interatividade com o Usuário:  

#-----------------------Classes-----------------------------

class Livro:
    def __init__(self, titulo, autor, ID):
        self.titulo = titulo
        self.autor = autor
        self.ID = ID
        self.status = 'Disponivel'

class Membro:
    def __init__(self, nome, nMembros, historico):
        self.nome = nome
        self.nMembros = nMembros
        self.historico = historico

class Biblioteca:
    def __init__(self):
        self.catalogoLivros = []
        self.registroMembros = []

#----------------------Funções-----------------------------

    def adicionarLivro(self):
        titulo = input('Digite o nome do livro:  ')
        autor = input('Digite o nome do autor:  ')
        novo_id = input('Digite o ID do livro:  ')
        livro = Livro(titulo, autor, novo_id)
        self.catalogoLivros.append(livro)
        print('Livro adicionado com sucesso')

    def adicionarMembro(self):
        nome = input('Digite o nome do Membro:  ')
        membro = Membro(nome, len(self.registroMembros) + 1, [])
        self.registroMembros.append(membro)
        print('Membro adicionado com sucesso')

    def emprestarLivro(self):
        titulo = input('Digite o título do livro que deseja emprestar:  ')
        for livro in self.catalogoLivros:
            if livro.titulo == titulo and livro.status == 'Disponivel':
                livro.status = 'Emprestado'
                print(f'O livro "{titulo}" foi emprestado com sucesso.')
                return
        print('Não possuímos esse livro disponível para empréstimo.')

    def devolverLivro(self):
        titulo = input('Digite o título do livro que deseja devolver:  ')
        for livro in self.catalogoLivros:
            if livro.titulo == titulo and livro.status == 'Emprestado':
                livro.status = 'Disponivel'
                print(f'O livro "{titulo}" foi devolvido com sucesso.')
                return
        print('Este livro não foi originalmente emprestado desta biblioteca ou já foi devolvido.')

    def pesquisarLivro(self):
        criterio = input('Digite o critério de pesquisa (titulo, autor, ID):  ').lower()
        termo = input(f'Digite o {criterio} do livro que deseja pesquisar:  ')
        for livro in self.catalogoLivros:
            if criterio == 'titulo' and livro.titulo == termo:
                print(f'O livro "{livro.titulo}" está {livro.status}.')
                break
            elif criterio == 'autor' and livro.autor == termo:
                print(f'O livro "{livro.titulo}" do autor {livro.autor} está {livro.status}.')
                break
            elif criterio == 'id' and livro.ID == termo:
                print(f'O livro "{livro.titulo}" com ID {livro.ID} está {livro.status}.')
                break
        else:
            print('Livro não encontrado.')
       
biblioteca = Biblioteca()

#------------------------Menu de interação com o Usuário-------------------------
while True:
    print('''
       ================
          Biblioteca
       ================
    Opções:  
    1 - Adicionar Livro
    2 - Adicionar Membro
    3 - Emprestar Livro
    4 - Devolver Livro
    5 - Pesquisar Livro
    x - Sair
''')

    op = input("Selecione a opção desejada: ")

    if op == 'x':
        print('Obrigado por usar a biblioteca. Até mais!')
        break
    elif op == '1':
        biblioteca.adicionarLivro()
    elif op == '2':
        biblioteca.adicionarMembro()
    elif op == '3':
        biblioteca.emprestarLivro()
    elif op == '4':
        biblioteca.devolverLivro()
    elif op == '5':
        biblioteca.pesquisarLivro()
    else:
        print('Opção inválida. Tente novamente.')