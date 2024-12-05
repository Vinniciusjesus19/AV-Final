from dataclasses import dataclass


@dataclass
class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str = ""):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento

    def __str__(self):
        if self.complemento:
            return f"{self.logradouro}, {self.numero}, {self.complemento}"
        return f"{self.logradouro}, {self.numero}"
