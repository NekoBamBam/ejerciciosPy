
class Cuenta:
    def __init__(
        self,
        numero_cuenta: int,
        titular: str,
        cuil: int,
        cbu: int,
        alias: str,
        saldo: float,
    ):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__cuil = cuil
        self.__cbu = cbu
        self.__alias = alias
        self.__saldo = saldo

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def titular(self):
        return self.__titular

    @property
    def cuil(self):
        return self.__cuil

    @property
    def cbu(self):
        return self.__cbu

    @property
    def alias(self):
        return self.__alias

    @property
    def saldo(self):
        return self.__saldo

