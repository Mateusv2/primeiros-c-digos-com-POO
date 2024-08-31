#Demostração simples de um abastecimento de combustivel no veiculo utilizando POO

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        
    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorLitro
        self.quantidadeCombustivel -= litros_abastecidos
        print(f"Você abasteceu {litros_abastecidos:.2f} litros de {self.tipoCombustivel}.")
    
    def abastecerPorLitro(self, litros):
        valor_pagar = litros * self.valorLitro
        self.quantidadeCombustivel -= litros
        print(f"O valor a ser pago é de R$ {valor_pagar:.2f}.")
    
    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor
    
    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel
    
    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade
        
    def mostrarQuantidadeCombustivel(self):
        print(f"Quantidade de combustível restante na bomba: {self.quantidadeCombustivel} litros.")
        

bomba = BombaCombustivel('Gasolina', 5.00, 100)

# Chamando as funções desejadas 

bomba.abastecerPorValor(50) 

bomba.abastecerPorLitro(20) 

bomba.mostrarQuantidadeCombustivel()