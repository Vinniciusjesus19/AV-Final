from abc import ABC, abstractmethod
from dataclasses import dataclass

from projeto.endereco import Endereco

@dataclass
class Funcionario(ABC):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco):
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        """ Método abstrato que deve ser implementado por subclasses para calcular o salário final. """
        pass

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Salário: {self.salario}, Endereço: {self.endereco}"

# Exemplo de subclassificação
class Funcionario(Funcionario):
    def salario_final(self) -> float:
        # Aqui você pode calcular o salário final de um funcionário fixo
        return self.salario

# Exemplo de uso
endereco = Endereco("Rua da Vitória", "778", "São Paulo", "SP")
funcionario1 = Funcionario("Vitoria", "vitoria@email.com", 5000.00, endereco)

print(Funcionario)
print(f"Salário final de {Funcionario.nome}: R${Funcionario.salario_final():.1f}")




