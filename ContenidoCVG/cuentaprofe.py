from datetime import datetime

#-----HELPERS----------------------
def ahora_str() -> str:
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


def limpiar_texto(valor=None) -> str:
    return "" if valor is None else valor.strip()


def colapsar_espacios(valor) -> str:
    return " ".join(valor.split())


def pasar_a_numero(valor) -> float:
    try:
        return float(str(valor).replace(",", "."))
    except ValueError:
        return 0.0


def solo_digitos(valor) -> str:
    return "".join(ch for ch in valor if ch.isdigit())


def es_numero_cuenta_valido(valor) -> bool:
    return len(valor) == 14 and valor.isdigit()


def es_cbu_valido(valor) -> bool:
    return len(valor) == 22 and valor.isdigit()


def es_nombre_valido(valor) -> bool:
    permitidos = set("áéíóúüñÁÉÍÓÚÜÑ'- ")
    return 1 <= len(valor) <= 100 and all(ch.isalpha() or ch in permitidos for ch in valor)    


def es_cuil_valido(valor) -> bool:
    return len(valor) == 11 and valor.isdigit()


def es_alias_valido(valor) -> bool:
    return 6 <= len(valor) <= 20 and all(ch.isalnum() or ch in "-." for ch in valor)


def es_monto_valido(valor) -> bool:
    return float(valor) > 0.0


def pedir_numero_cuenta_hasta_valido(valor) -> str:
    numero = limpiar_texto(valor)
    while not es_numero_cuenta_valido(numero):
        if numero:
            print("Ingrese un número de cuenta de 14 digitos: ")
        numero = limpiar_texto(input("Introdujo valor invalido, vuelva a intentarlo: "))
    return numero


def pedir_cbu_hasta_valido(valor) -> str:
    numero = limpiar_texto(valor)
    while not es_cbu_valido(numero):
        if numero:
            print("Ingrese un CBU de 22 digitos: ")
        numero = limpiar_texto(input("Introdujo valor invalido, vuelva a intentarlo: "))
    return numero


def pedir_titular_hasta_valido(valor) -> str:
    nombre = colapsar_espacios(limpiar_texto(valor))
    while not es_nombre_valido(nombre):
        if nombre:
            print("Ingrese un nombre válido: ")
        nombre = colapsar_espacios(limpiar_texto(input("Introdujo valor invalido, vuelva a intentarlo: ")))
    return nombre.upper()


def pedir_cuil_hasta_valido(valor) -> str:
    cuil = solo_digitos(limpiar_texto(valor))
    while not es_cuil_valido(cuil):
        if cuil:
            print("Ingrese un CUIL de 11 digitos: ")
        cuil = limpiar_texto(input("Introdujo valor invalido, vuelva a intentarlo: "))
    return cuil


def pedir_alias_hasta_valido(valor) -> str:
    alias = limpiar_texto(valor)
    while not es_alias_valido(alias):
        if alias:
            print("Ingrese un alias válido, palabras separadas por . o -: ")
        alias = limpiar_texto(input("Introdujo valor invalido, vuelva a intentarlo: "))
    return alias


def pedir_monto_hasta_valido(valor) -> float:
    monto = pasar_a_numero(valor)
    while not es_monto_valido(monto):
        if monto:
            print("Ingrese un monto válido: ")
        monto = pasar_a_numero(input("Introdujo valor invalido, vuelva a intentarlo: "))
    return monto


#-----CLASE---------------
class Cuenta:
    def __init__(self, numero, cbu, alias, titular, cuil, saldo=0.0) -> None:
        self.__numero_cuenta = pedir_numero_cuenta_hasta_valido(numero)
        self.__cbu = pedir_cbu_hasta_valido(cbu)
        self.__alias = pedir_alias_hasta_valido(alias)
        self.__titular = pedir_titular_hasta_valido(titular)
        self.__cuil = pedir_cuil_hasta_valido(cuil)
        self.__saldo = pedir_monto_hasta_valido(saldo)

    #---------GETTERS--------------
    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def numero_cuenta_formateado(self):
        return f"CA $ {self.__numero_cuenta}"

    @property
    def cbu(self):
        return self.__cbu

    @property
    def alias(self):
        return self.__alias
    
    @property
    def titular_formateado(self):
        return " ".join(p.capitalize() for p in self.__titular.split())

    @property
    def titular(self):
        return self.__titular

    @property
    def cuil(self):
        return self.__cuil

    @property
    def cuil_formateado(self):
        return f"{self.__cuil[:2]}-{self.__cuil[2:10]}-{self.__cuil[10:]}"

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def saldo_formateado(self):
        return f"${self.__saldo:.2f}"

    #-----METODOS---------------------------
    def cambiar_alias(self, nuevo_alias):
        self.__alias = pedir_alias_hasta_valido(nuevo_alias)

    def __imprimir_movimiento(self, ch, monto):
        motivo = input("Ingrese el motivo de la operación: ").strip()
        if ch == "-":
            tipo_operacion = "Extracción"
        else:
            tipo_operacion = "Depósito"
        print(f"Movimiento ejecutado:\nN° cuenta {self.numero_cuenta_formateado} - Nombre del titular: {self.titular_formateado}\nFecha: {ahora_str()} - Motivo: {motivo} - Monto: {ch}{monto:.2f}")

    def ver_datos_cuenta(self):
        print("#Consulta de datos:")
        print(f"#Nombre del titular: {self.titular_formateado} – CUIL: {self.cuil_formateado}")
        print(f"#N° de cuenta: {self.numero_cuenta_formateado} – Alias: {self.alias} – CBU: {self.cbu}")

    def ver_saldo(self):
        print("#Consulta de saldo:")
        print(f"#Nombre del titular: {self.titular_formateado} – N° de cuenta: {self.numero_cuenta_formateado} – Saldo: {self.saldo_formateado}")

    def depositar(self, monto) -> bool:
        monto_valido = pedir_monto_hasta_valido(monto)
        self.__saldo += monto_valido
        self.__imprimir_movimiento("+", monto_valido)
        return True
    
    def extraer(self, monto) -> bool:
        monto_valido = pedir_monto_hasta_valido(monto)
        if monto_valido > self.__saldo:
            print("Fondos insuficientes.")
            return False
        self.__saldo -= monto_valido
        self.__imprimir_movimiento("-", monto_valido)
        return True

    #--------------FORMATO-------------------
    def __str__(self) -> str:
        return f"Cuenta N°: {self.__numero_cuenta} - CBU: {self.__cbu}\nAlias: {self.__alias} - Titular: {self.__titular}\nCUIL: {self.__cuil} - Saldo: ${self.__saldo:.2f}"


#------------------MAIN--------------------------
