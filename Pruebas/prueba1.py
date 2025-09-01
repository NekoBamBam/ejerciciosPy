class Cuenta:
    def __init__(self,nombre,cbu=None):
        self.__nombre = nombre
        self.__cbu = pedir_cbu_hasta_valido(cbu)
        return "" if valor is None else str(valor).strip()