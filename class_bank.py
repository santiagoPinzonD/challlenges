#!/usr/bin/python3
""""function that creat a clieente of a bank"""


class cliente():
    """create a cliente"""
    def __init__(self, Name):
        self.name = Name
        self.cantidad = 0

    def extraer(self, extraer):
        self.cantidad -= extraer

    def depositar(self, deposito):
        self.cantidad += deposito

    def return_cantidad(self):
        print(self.cantidad)

    def datos(self):
        print("The cliente is ", self.name, "and your \
amount is : ", self.cantidad)

cliente1 = cliente("Santiago")
cliente1.depositar(100)
cliente1.return_cantidad()
cliente1.extraer(50)
cliente1.return_cantidad()
cliente1.datos()
