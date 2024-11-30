#função para calcular o valor total do produto
def calcular_valor(produto, tipo, tem_frete_gratis, cupom_desconto=0):
    #valor dos frete
    frete_nacional = 15.90
    frete_internacional = 19.90
    icms = 0.17

    #calcula o valor total
    if tipo == "nacional":
        frete = 0 if tem_frete_gratis else frete_nacional
        valor_total = produto + frete
    elif tipo == "importado":
        frete = 0 if tem_frete_gratis else frete_internacional
        imposto = produto * icms
        valor_total = produto + imposto + frete
    else:
        return "Tipo de produto inválido."

    #aplica cupom de desconto
    valor_total -= cupom_desconto

    return max(valor_total, 0)  # Garantir que não tenha valor negativo


#classe para gerenciar lista de desejos e cupons
class ListaDesejos:
    def __init__(self):
        self.produtos = {}
        self.cupons_disponiveis = []

    def adicionar_produto(self, nome):
        self.produtos[nome] = False
        print(f"O produto '{nome}' foi adicionado à lista de desejos.")

    def notificar_cupom(self, produto, cupom):
        if produto in self.produtos:
            self.produtos[produto] = True
            self.cupons_disponiveis.append((produto, cupom))
            print(f"Novo cupom para '{produto}' disponível: {cupom}.")

    def listar_produtos(self):
        return self.produtos

    def listar_cupons(self):
        return self.cupons_disponiveis


#exemplo/ simulação de uso
if __name__ == "__main__":
    # Dados de exemplo
    lista_desejos = ListaDesejos()
    lista_desejos.adicionar_produto("Smartphone")
    lista_desejos.adicionar_produto("Notebook")

    lista_desejos.notificar_cupom("Smartphone", "DESCONTO10")

    #pedir dados ao usuário
    valor_produto = float(input("Digite o valor do produto: "))
    tipo_produto = input("O produto é 'nacional' ou 'importado'? ").lower()
    frete_gratis = input("Você possui cupom de frete grátis? (s/n): ").lower() == "s"
    primeiro_compra = input("É sua primeira compra? (s/n): ").lower() == "s"
    cupom_loja = float(input("Insira o valor do cupom de desconto da loja (em R$): "))

    if primeiro_compra:
        frete_gratis = True

    valor_final = calcular_valor(
        valor_produto, tipo_produto, frete_gratis, cupom_loja
    )
    print(f"O valor total do produto é: R${valor_final:.2f}")

    #mmostrar lista de desejos e cupons
    print("\nLista de desejos e notificações:")
    print("Produtos:", lista_desejos.listar_produtos())
    print("Cupons disponíveis:", lista_desejos.listar_cupons())
