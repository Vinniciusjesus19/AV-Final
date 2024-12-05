from dataclasses import dataclass

from projeto.endereco import Endereco
from projeto.funcionario import Funcionario


@dataclass
class Engenheiro(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco, crea: str):
        super().__init__(nome, email, salario, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        # Para o exemplo, vamos tornar o salário final igual ao salário base,
        # mas você pode personalizar esta lógica como preferir.
        return self.salario

    def __str__(self):
        return f"{super().__str__()}, CREA: {self.crea}"


        