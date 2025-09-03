import re 
from datetime import datetime


def solo_digitos(s: str) -> str:
    return "".join(ch for ch in str(s) if ch.isdigit())


def es_cadena_n_digitos(s: str, n: int) -> bool:
    return len(s) == n and s.isdigit()


def validar_numero_cuenta14(s: str) -> str:
    d = solo_digitos(s)
    if not es_cadena_n_digitos(d, 14):
        raise ValueError("numero_cuenta debe tener 14 digitos")
    return d


def normalizar_titular(s: str) -> str:
    s = str(s).strip()
    if not (1 <= len(s) <= 100):
        raise ValueError("Titular inválido")
    return s.upper()


def normalizar_cuil(s: str) -> str:
    d = solo_digitos(s)
    if not es_cadena_n_digitos(d, 11):
        raise ValueError("el cuil debe tener 11 digitos")
    return d


_ALIAS_RE = re.compile(r"^[A-Za-z0-9.\-]{6,20}$")


def validar_alias(s: str) -> str:
    s = str(s).strip()
    if not _ALIAS_RE.fullmatch(s):
        raise ValueError(
            "el alias es invalido, debe tener (6-20 caracteres alfanumericos)"
        )
    return s


def formato_monto(m: float) -> str:
    signo = "+" if m >= 0 else "-"
    return f"{signo}{abs(m):.2f}"


def ahora_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


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
        (
            self.__numero_cuenta,
            self.__titular,
            self.__cuil,
            self.__cbu,
            self.__alias,
            self.__saldo,
        ) = (
            validar_numero_cuenta14(numero_cuenta),
            normalizar_titular(titular),
            normalizar_cuil(cuil),
            cbu if es_cadena_n_digitos(cbu, 22) else ValueError("CBU invalido"),
            validar_alias(alias),
            max(0.0, saldo),
        )

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

    def imprimir_datos(self):
        print(f"Nombre del titular: {self.__titular} - CUIL: {self.__cuil}")
        print(
            f"N° de cuenta: CA $ {self.__numero_cuenta} - Alias: {self.__alias} - CBU: {self.__cbu}"
        )

    def imprimir_movimiento(self, motivo: str, monto: float):
        print(
            f"N° de cuenta: CA $ {self.__numero_cuenta} - Nombre del titular: {self.__titular}"
        )
        print(
            f"Fecha: {ahora_str()} - motivo: {motivo} - Monto: {formato_monto(monto)}"
        )

    def consultar_saldo(self):
        print(
            f"Nombre del titular: {self.__titular} - N° de cuenta: CA $ {self.__numero_cuenta} - Saldo: {self.__saldo:.2f}"
        )


class CuentaAhorro(Cuenta):
    pass


class CuentaCorriente(Cuenta):
    def __init__(
        self, numero_cuenta, titular, cuil, cbu, alias, saldo=0.0, descubierto=0.0
    ) -> None:
        super().__init__(numero_cuenta, titular, cuil, cbu, alias, saldo)
        self.__descubierto = self.__validar_descubierto(descubierto)

    @staticmethod
    def __validar_descubierto(valor) -> float:
        v = pasar_a_numero(valor)
        if v < 0.0:
            print("El descubierto no puede ser negativo")
            v = 0.0
        return v

    @property
    def descubierto(self) -> float:
        return self.__descubierto
