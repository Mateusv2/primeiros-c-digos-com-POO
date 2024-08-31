#Processo simulando a funcionabilidade de um Elevador utilizando POO

class Elevador:
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0

    def Subir(self):
        andar = int(input('Pressione o andar que deseja ir de 0 a {}: '.format(self.totalAndar)))
        if 0 < andar < self.totalAndar:
            print('Subindo para o andar', andar)
            self.atualAndar = andar
            self.exibir_status()
        elif andar == self.totalAndar:
            print('Você já está no último andar.')
        else:
            print('Andar inválido.')

    def Descer(self):
        andar = int(input('Pressione o andar que deseja ir de 0 a {}: '.format(self.totalAndar)))
        if 0 < andar <= self.totalAndar:
            print('Descendo para o andar', andar)
            self.atualAndar = andar
            self.exibir_status()
        elif andar == 0:
            print('Você já está no térreo.')
        else:
            print('Andar inválido.')

    def Entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print('Uma pessoa entrou no elevador.')
            self.exibir_status()
        else:
            print('O elevador está cheio.')

    def Sair(self):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            print('Uma pessoa saiu do elevador.')
            self.exibir_status()
        else:
            print('Não há ninguém no elevador.')

    def exibir_status(self):
        print('Andar atual:', self.atualAndar)
        print('Capacidade atual:', self.atualCapacidade)


usar_elevador = Elevador(7, 17) # informando o total permitido de pessoas dentro do elevador (7) e o total de andares no prédio (17).

while True:
    opcao = input("Escolha uma opção: Subir, Descer, Entrar, Sair (ou 'sair' para encerrar): ").lower()
    if opcao == 'subir':
        usar_elevador.Subir()
    elif opcao == 'descer':
        usar_elevador.Descer()
    elif opcao == 'entrar':
        usar_elevador.Entrar()
    elif opcao == 'sair':
        usar_elevador.Sair()
    else:
        print('Opção inválida.')

    continuar = input('Deseja continuar (s/n)? ').lower()
    if continuar != 's':
        break
