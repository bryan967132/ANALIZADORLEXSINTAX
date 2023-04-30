from Token import Token
class CrearBD:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd
        print(f"Se creó la base de datos {self.nombre_bd}")

class EliminarBD:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd
        print(f"Se eliminó la base de datos {self.nombre_bd}")

class CrearColeccion:
    def __init__(self, nombre_coleccion):
        self.nombre_coleccion = nombre_coleccion
        print(f"Se creó la colección {self.nombre_coleccion}")

class EliminarColeccion:
    def __init__(self, nombre_coleccion):
        self.nombre_coleccion = nombre_coleccion
        print(f"Se eliminó la colección {self.nombre_coleccion}")

class InsertarUnico:
    def __init__(self, nombre_coleccion, registro):
        self.nombre_coleccion = nombre_coleccion
        self.registro = registro
        print(f"Se insertó el registro {self.registro} en la colección {self.nombre_coleccion}")

class ActualizarUnico:
    def __init__(self, nombre_coleccion, filtro, valores):
        self.nombre_coleccion = nombre_coleccion
        self.filtro = filtro
        self.valores = valores
        print(f"Se actualizó el registro en la colección {self.nombre_coleccion} que cumple el filtro {self.filtro} con los valores {self.valores}")

class EliminarUnico:
    def __init__(self, nombre_coleccion, filtro):
        self.nombre_coleccion = nombre_coleccion
        self.filtro = filtro
        print(f"Se eliminó el registro en la colección {self.nombre_coleccion} que cumple el filtro {self.filtro}")

class BuscarTodo:
    def __init__(self, nombre_coleccion):
        self.nombre_coleccion = nombre_coleccion
        print(f"Se buscaron todos los registros en la colección {self.nombre_coleccion}")

class BuscarUnico:
    def __init__(self, nombre_coleccion, filtro):
        self.nombre_coleccion = nombre_coleccion
        self.filtro = filtro
        print(f"Se buscó el registro en la colección {self.nombre_coleccion} que cumple el filtro {self.filtro}")

sentencias = [
    'CrearBD("ejemplo");',
    'EliminarBD("elimina");',
    'colec = CrearColeccion("NombreColeccion");',
    'eliminacolec = EliminarColeccion("NombreColeccion");',
    'insertadoc = InsertarUnico("NombreColeccion" ,"{\\"nombre\\": \\"Obra Literaria\\", \\"autor\\": \\"Jorge Luis\\"}");',
    'actualizadoc = ActualizarUnico("NombreColeccion", "{\\"nombre\\": \\"Obra Literaria\\"}", "{$set: {\\"autor\\": \\"Mario Vargas\\"}}");',
    'eliminadoc = EliminarUnico("NombreColeccion", "{\\"nombre\\": \\"Obra Literaria\\"}");',
    'todo = BuscarTodo("NombreColeccion");',
    'unico = BuscarUnico("NombreColeccion", "{\\"nombre\\": \\"Obra Literaria\\"}");'
]

for sentencia in sentencias:
    exec(sentencia[:-1])
for sentencia in sentencias:
    tokens = sentencia.split()
    if tokens[0] == 'CrearBD':
        identificador = tokens[1].replace(";", "")
        instancia = CrearBD()
    elif tokens[0] == 'EliminarBD':
        identificador = tokens[1].replace(";", "")
        instancia = EliminarBD()
    elif tokens[0] == 'CrearColeccion':
        identificador = tokens[2].replace("=", "").replace(";", "")
        parametro = tokens[5].replace("(", "").replace(")", "").replace('"', '')
        instancia = CrearColeccion(parametro)
    elif tokens[0] == 'EliminarColeccion':
        identificador = tokens[2].replace("=", "").replace(";", "")
        parametro = tokens[5].replace("(", "").replace(")", "").replace('"', '')
        instancia = EliminarColeccion(parametro)
    elif tokens[0] == 'InsertarUnico':
        identificador = tokens[2].replace("=", "").replace(";", "")
        parametros = tokens[5].replace("(", "").replace(")", "").replace('"', '').split(",")
        instancia = InsertarUnico(parametros[0], parametros[1])
    elif tokens[0] == 'ActualizarUnico':
        identificador = tokens[2].replace("=", "").replace(";", "")
        parametros = tokens[5].replace("(", "").replace(")", "").replace('"', '').split(",")
        instancia = ActualizarUnico(parametros[0], parametros[1], parametros[2])
    elif tokens[0] == 'EliminarUnico':
        identificador = tokens[2].replace("=", "").replace(";", "")
        parametros = tokens[5].replace("(", "").replace(")", "").replace('"', '').split(",")
        instancia = EliminarUnico(parametros[0], parametros[1])
    elif tokens[0] == 'BuscarTodo':
        identificador = tokens[2].replace("=", "").replace(";", "")
        parametro = tokens[5].replace("(", "").replace(")", "").replace('"', '')
        instancia = BuscarTodo(parametro)
    elif tokens[0] == 'BuscarUnico':
        identificador = tokens[2].replace("=", "").replace(";", "")
        parametros = tokens[5].replace("(", "").replace(")", "").replace('"', '').split(",")
        instancia = BuscarUnico(parametros[0], parametros[1])
    else:
        print("Sentencia no reconocida")
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.token_index = -1
        self.advance()

    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]

    def parse(self):
        if self.current_token.tipo == 'CREAR_BD':
            self.advance()
            if self.current_token.tipo == 'IDENTIFICADOR':
                nombre_bd = self.current_token.valor
                self.advance()
                if self.current_token.tipo == 'PUNTO_Y_COMA':
                    self.advance()
                    return CrearBD(nombre_bd)
        elif self.current_token.tipo == 'ELIMINAR_BD':
            self.advance()
            if self.current_token.tipo == 'IDENTIFICADOR':
                nombre_bd = self.current_token.valor
                self.advance()
                if self.current_token.tipo == 'PUNTO_Y_COMA':
                    self.advance()
                    return EliminarBD(nombre_bd)
        elif self.current_token.tipo == 'CREAR_COLECCION':
            self.advance()
            if self.current_token.tipo == 'IDENTIFICADOR':
                nombre_coleccion = self.current_token.valor
                self.advance()
                if self.current_token.tipo == 'PUNTO_Y_COMA':
                    self.advance()
                    return CrearColeccion(nombre_coleccion)
        elif self.current_token.tipo == 'ELIMINAR_COLECCION':
            self.advance()
            if self.current_token.tipo == 'IDENTIFICADOR':
                nombre_coleccion = self.current_token.valor
                self.advance()
                if self.current_token.tipo == 'PUNTO_Y_COMA':
                    self.advance()
                    return EliminarColeccion(nombre_coleccion)
        elif self.current_token.tipo == 'INSERTAR_UNICO':
            self.advance()
            if self.current_token.tipo == 'PARENTESIS_IZQUIERDO':
                self.advance()
                if self.current_token.tipo == 'IDENTIFICADOR':
                    nombre_coleccion = self.current_token.valor
                    self.advance()
                    if self.current_token.tipo == 'COMA':
                        self.advance()
                        if self.current_token.tipo == 'CADENA':
                            document = self.current_token.valor
                            self.advance()
                            if self.current_token.tipo == 'PARENTESIS_DERECHO':
                                self.advance()
                                if self.current_token.tipo == 'PUNTO_Y_COMA':
                                    self.advance()
                                    return InsertarUnico(nombre_coleccion, document)
        elif self.current_token.tipo == 'ACTUALIZAR_UNICO':
            self.advance()
            if self.current_token.tipo == 'PARENTESIS_IZQUIERDO':
                self.advance()
                if self.current_token.tipo == 'IDENTIFICADOR':
                    nombre_coleccion = self.current_token.valor
                    self.advance()
                    if self.current_token.tipo == 'COMA':
                        self.advance()
                        if self.current_token.tipo == 'CADENA':
                            filtro = self.current_token.valor
                            self.advance()
                            if self.current_token.tipo == 'COMA':
                                self.advance()
                                if self.current_token.tipo == 'CADENA':
                                    update = self.current_token.valor
                                    self.advance()
                                    if self.current_token.tipo == 'PARENTESIS_DERECHO':
                                        self.advance()
                                        if self.current_token.tipo == 'PUNTO_Y_COMA':
                                            self.advance()
                                            return ActualizarUnico(nombre_coleccion, filtro, update)
        elif self.current_token.tipo == 'ELIMINAR_UNICO':
            self.advance()
            if self.current_token.tipo == 'PARENTESIS_IZQUIERDO':
                self.advance()
                if self.current_token.tipo == 'IDENTIFICADOR':
                    nombre_coleccion = self.current_token.valor
                    self.advance()
                    if self.current_token.tipo == 'COMA':
                        self.advance()
                        if self.current_token.tipo == 'CADENA':
                            filtro = self.current_token.valor
                            self.advance()
                            if self.current_token.tipo == 'PARENTESIS_DERECHO':
                                self.advance()
                                if self.current_token.tipo == 'PUNTO_Y_COMA':
                                    self.advance()
                                    return EliminarUnico(nombre_coleccion, filtro)
        elif self.current_token.tipo == 'BUSCAR_TODO':
            self.advance()
            if self.current_token.tipo == 'PARENTESIS_IZQUIERDO':
                self.advance()
                if self.current_token.tipo == 'IDENTIFICADOR':
                    nombre_coleccion = self.current_token.valor
                    self.advance()
                    if self.current_token.tipo == 'PARENTESIS_DERECHO':
                        self.advance()
                        if self.current_token.tipo == 'PUNTO_Y_COMA':
                            self.advance()
                            return BuscarTodo(nombre_coleccion)
        elif self.current_token.tipo == 'BUSCAR_UNICO':
            self.advance()
            if self.current_token.tipo == 'PARENTESIS_IZQUIERDO':
                self.advance()
                if self.current_token.tipo == 'IDENTIFICADOR':
                    nombre_coleccion = self.current_token.valor
                    self.advance()
                    if self.current_token.tipo == 'PARENTESIS_DERECHO':
                        self.advance()
                        if self.current_token.tipo == 'PUNTO_Y_COMA':
                            self.advance()
                            return BuscarUnico(nombre_coleccion)