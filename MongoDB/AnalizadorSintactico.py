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

# sentencias = [
#     'CrearBD("ejemplo");',
#     'EliminarBD("elimina");',
#     'colec = CrearColeccion("NombreColeccion");',
#     'eliminacolec = EliminarColeccion("NombreColeccion");',
#     'insertadoc = InsertarUnico("NombreColeccion" ,"{\\"nombre\\": \\"Obra Literaria\\", \\"autor\\": \\"Jorge Luis\\"}");',
#     'actualizadoc = ActualizarUnico("NombreColeccion", "{\\"nombre\\": \\"Obra Literaria\\"}", "{$set: {\\"autor\\": \\"Mario Vargas\\"}}");',
#     'eliminadoc = EliminarUnico("NombreColeccion", "{\\"nombre\\": \\"Obra Literaria\\"}");',
#     'todo = BuscarTodo("NombreColeccion");',
#     'unico = BuscarUnico("NombreColeccion", "{\\"nombre\\": \\"Obra Literaria\\"}");'
# ]

# for sentencia in sentencias:
#     exec(sentencia[:-1])
# for sentencia in sentencias:
#     tokens = sentencia.split()
#     if tokens[0] == 'CrearBD':
#         identificador = tokens[1].replace(";", "")
#         instancia = CrearBD()
#     elif tokens[0] == 'EliminarBD':
#         identificador = tokens[1].replace(";", "")
#         instancia = EliminarBD()
#     elif tokens[0] == 'CrearColeccion':
#         identificador = tokens[2].replace("=", "").replace(";", "")
#         parametro = tokens[5].replace("(", "").replace(")", "").replace('"', '')
#         instancia = CrearColeccion(parametro)
#     elif tokens[0] == 'EliminarColeccion':
#         identificador = tokens[2].replace("=", "").replace(";", "")
#         parametro = tokens[5].replace("(", "").replace(")", "").replace('"', '')
#         instancia = EliminarColeccion(parametro)
#     elif tokens[0] == 'InsertarUnico':
#         identificador = tokens[2].replace("=", "").replace(";", "")
#         parametros = tokens[5].replace("(", "").replace(")", "").replace('"', '').split(",")
#         instancia = InsertarUnico(parametros[0], parametros[1])
#     elif tokens[0] == 'ActualizarUnico':
#         identificador = tokens[2].replace("=", "").replace(";", "")
#         parametros = tokens[5].replace("(", "").replace(")", "").replace('"', '').split(",")
#         instancia = ActualizarUnico(parametros[0], parametros[1], parametros[2])
#     elif tokens[0] == 'EliminarUnico':
#         identificador = tokens[2].replace("=", "").replace(";", "")
#         parametros = tokens[5].replace("(", "").replace(")", "").replace('"', '').split(",")
#         instancia = EliminarUnico(parametros[0], parametros[1])
#     elif tokens[0] == 'BuscarTodo':
#         identificador = tokens[2].replace("=", "").replace(";", "")
#         parametro = tokens[5].replace("(", "").replace(")", "").replace('"', '')
#         instancia = BuscarTodo(parametro)
#     elif tokens[0] == 'BuscarUnico':
#         identificador = tokens[2].replace("=", "").replace(";", "")
#         parametros = tokens[5].replace("(", "").replace(")", "").replace('"', '').split(",")
#         instancia = BuscarUnico(parametros[0], parametros[1])
#     else:
#         print("Sentencia no reconocida")
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token: Token = None
        self.token_index = -1
        self.advance()

    def advance(self):
        try:
            self.token_index += 1
            self.current_token = self.tokens[self.token_index]
        except:
            self.current_token = None

    def parse(self):
        if not self.current_token:
            print('EOF')
            return
        if self.current_token.tipo == 'CREARBD':
            self.advance()
            if self.current_token.tipo == 'IDENTIFICADOR':
                nombre_bd = self.current_token.buffer
                self.advance()
                if self.current_token.tipo == 'PUNTO_Y_COMA':
                    self.advance()
                    CrearBD(nombre_bd)
        elif self.current_token.tipo == 'ELIMINARBD':
            self.advance()
            if self.current_token.tipo == 'IDENTIFICADOR':
                nombre_bd = self.current_token.buffer
                self.advance()
                if self.current_token.tipo == 'PUNTO_Y_COMA':
                    self.advance()
                    EliminarBD(nombre_bd)
        elif self.current_token.tipo == 'CREARCOLECCION':
            self.advance()
            if self.current_token.tipo == 'IDENTIFICADOR':
                nombre_coleccion = self.current_token.buffer
                self.advance()
                if self.current_token.tipo == 'PUNTO_Y_COMA':
                    self.advance()
                    CrearColeccion(nombre_coleccion)
        elif self.current_token.tipo == 'ELIMINARCOLECCION':
            self.advance()
            if self.current_token.tipo == 'IDENTIFICADOR':
                nombre_coleccion = self.current_token.buffer
                self.advance()
                if self.current_token.tipo == 'PUNTO_Y_COMA':
                    self.advance()
                    EliminarColeccion(nombre_coleccion)
        elif self.current_token.tipo == 'INSERTARUNICO':
            self.advance()
            if self.current_token.tipo == 'PARENTESIS_IZQUIERDO':
                self.advance()
                if self.current_token.tipo == 'IDENTIFICADOR':
                    nombre_coleccion = self.current_token.buffer
                    self.advance()
                    if self.current_token.tipo == 'COMA':
                        self.advance()
                        if self.current_token.tipo == 'CADENA':
                            document = self.current_token.buffer
                            self.advance()
                            if self.current_token.tipo == 'PARENTESIS_DERECHO':
                                self.advance()
                                if self.current_token.tipo == 'PUNTO_Y_COMA':
                                    self.advance()
                                    InsertarUnico(nombre_coleccion, document)
        elif self.current_token.tipo == 'ACTUALIZARUNICO':
            self.advance()
            if self.current_token.tipo == 'PARENTESIS_IZQUIERDO':
                self.advance()
                if self.current_token.tipo == 'IDENTIFICADOR':
                    nombre_coleccion = self.current_token.buffer
                    self.advance()
                    if self.current_token.tipo == 'COMA':
                        self.advance()
                        if self.current_token.tipo == 'CADENA':
                            filtro = self.current_token.buffer
                            self.advance()
                            if self.current_token.tipo == 'COMA':
                                self.advance()
                                if self.current_token.tipo == 'CADENA':
                                    update = self.current_token.buffer
                                    self.advance()
                                    if self.current_token.tipo == 'PARENTESIS_DERECHO':
                                        self.advance()
                                        if self.current_token.tipo == 'PUNTO_Y_COMA':
                                            self.advance()
                                            ActualizarUnico(nombre_coleccion, filtro, update)
        elif self.current_token.tipo == 'ELIMINARUNICO':
            self.advance()
            if self.current_token.tipo == 'PARENTESIS_IZQUIERDO':
                self.advance()
                if self.current_token.tipo == 'IDENTIFICADOR':
                    nombre_coleccion = self.current_token.buffer
                    self.advance()
                    if self.current_token.tipo == 'COMA':
                        self.advance()
                        if self.current_token.tipo == 'CADENA':
                            filtro = self.current_token.buffer
                            self.advance()
                            if self.current_token.tipo == 'PARENTESIS_DERECHO':
                                self.advance()
                                if self.current_token.tipo == 'PUNTO_Y_COMA':
                                    self.advance()
                                    EliminarUnico(nombre_coleccion, filtro)
        elif self.current_token.tipo == 'BUSCARTODO':
            self.advance()
            if self.current_token.tipo == 'PARENTESIS_IZQUIERDO':
                self.advance()
                if self.current_token.tipo == 'IDENTIFICADOR':
                    nombre_coleccion = self.current_token.buffer
                    self.advance()
                    if self.current_token.tipo == 'PARENTESIS_DERECHO':
                        self.advance()
                        if self.current_token.tipo == 'PUNTO_Y_COMA':
                            self.advance()
                            BuscarTodo(nombre_coleccion)
        elif self.current_token.tipo == 'BUSCARUNICO':
            self.advance()
            if self.current_token.tipo == 'PARENTESIS_IZQUIERDO':
                self.advance()
                if self.current_token.tipo == 'IDENTIFICADOR':
                    nombre_coleccion = self.current_token.buffer
                    self.advance()
                    if self.current_token.tipo == 'PARENTESIS_DERECHO':
                        self.advance()
                        if self.current_token.tipo == 'PUNTO_Y_COMA':
                            self.advance()
                            BuscarUnico(nombre_coleccion)
        # self.parse() # (comentado temporalmente) llamada recursiva para ejecutar el resto de comandos
