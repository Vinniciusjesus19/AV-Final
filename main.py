from projeto.nutricionista import Nutricionista

# Instanciar objetos.
nutricionista = Nutricionista()
nutricionista.nome = input("Digite seu nome: ")
nutricionista.email = input("Digite seu email: ")
nutricionista.salario = float("Digite seu salario: ")
nutricionista.endereco.logradouro = input("Digite o logradouro: ")
nutricionista.endereco.numero = input("Digite o número da residência: ")

nutricionista.mostrar_dados_funcionarios()



