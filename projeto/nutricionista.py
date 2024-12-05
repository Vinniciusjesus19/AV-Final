from dataclasses import dataclass

from projeto.nutricionista import Endereco
from projeto.funcionario import Funcionario


@dataclass
class Nutricionista(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco, crn: str):
        super().__init__(nome, email, salario, endereco)
        self.crn = crn

    def salario_final(self) -> float:
        # Para o exemplo, vamos considerar que o salário final é o salário base
        return self.salario

    def __str__(self):
        return f"{super().__str__()}, CRN: {self.crn}"