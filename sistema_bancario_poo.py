import textwrap

class Banco:
    limite_saques = 3
    agencia = "0001"

    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.usuarios = []
        self.contas = []
        self.numero_saques = 0

    def menu (self):
         menu = """\n
        ================ MENU ================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [c]\tNova conta
        [l]\tListar contas
        [u]\tNovo usuário
        [q]\tSair
        => """    
         return input(textwrap(menu))

    def depositar (self, valor):
        if valor > 0:
            self.saldo += valor 
            self.extrato += f"Depósito de R$ {valor:.2f}\n" 
            print(f"Depósito de R$ {valor} realizado com sucesso.")

        else:
            print("O valor informado não é válido! Tente novamente.\n")    

        

    def sacar (self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite 
        excedeu_saques = self.numero_saques > self.limite_saques

        if excedeu_limite:
            print("Não foi possível continuar pois não há limite disponível.")

        elif excedeu_saldo:
            print("Não foi possível continuar pois não há saldo o suficiente.")

        elif excedeu_saques:
            print("O limite de saques já foi atingido.") 

        elif valor > 0:
            self.saldo -= valor
            self.numero_saques += 1
            self.extrato += f"Saque de R$ {valor:.2f}\n" 
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.\n")    

        else:
            print("Digite um valor válido para continuar.")              

    def exibir_extrato (self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")


    def criar_usuario (self):
        cpf = input("Informe os números do CPF: ")    
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            print("O CPF informado já está cadastrado.")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("=== Usuário criado com sucesso! ===")



    def criar_conta (self):
        cpf = input("Informe os números do CPF: ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            numero_conta = len(self.contas) + 1
            print("\n=== Conta criada com sucesso! ===")
            self.contas.append({"agencia": self.agencia, "numero_conta": numero_conta, "usuario": usuario})

        else:
            print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

    def filtrar_usuario (self, cpf):
        usuarios_filtrados = [usuario for usuario in self.usuarios if usuario["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None    

    def listar_contas (self):
        for conta in self.contas:
            linha = f"""\n
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

    def main(self):
        while True:
            opcao = self.menu

            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))
                self.depositar(valor)

            elif opcao == "s":
                valor = float(input("Informe o valor do saque: "))
                self.sacar(valor)

            elif opcao == "e":
                self.exibir_extrato()

            elif opcao == "c":
                self.criar_conta()

            elif opcao == "u":
                self.criar_usuario()

            elif opcao == "l":
                self.listar_contas()

            elif opcao == "q":
                break

            else:
                print("Você digitou uma opção inválida.\nTente Novamente.")        


if __name__ == "__main__":
    banco = Banco()
    banco.iniciar()

