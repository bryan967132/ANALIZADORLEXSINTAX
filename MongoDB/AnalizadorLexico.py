from Error import Error
from Token import Token
from prettytable import PrettyTable
import json

class AnalizadorLexico:
    def __init__(self):
        self.tokens = []
        self.errores = []
        self.linea = 1
        self.columna = 1
        self.estado = 0
        self.buffer = ''

    def agregarError(self,caracter):
        self.errores.append(Error(f'Caracter sin reconocer: {caracter}',self.linea,self.columna))

    def agregarToken(self,tipo,token):
        self.tokens.append(Token(tipo,token,self.linea,self.columna))
        self.i -= 1

    def verErrores(self):
        print('\nErrores')
        x = PrettyTable()
        x.field_names = ['Descripción','Linea','Columna']
        for error in self.errores:
            x.add_row([error.caracter,error.linea,error.columna])
        table_str = str(x)
        return table_str

    def verTokens(self):
        x = PrettyTable()
        x.field_names = ['#', 'Token', 'Tipo', 'Linea', 'Columna']
        for i, token in enumerate(self.tokens, 1):
            x.add_row([i, token.buffer, token.tipo, token.linea, token.columna])
        table_str = str(x)
        return table_str

    def s0(self,caracter):
        if caracter == '-':
            self.estado = 1
            self.columna += 1
            self.buffer += caracter
        elif caracter == '/':
            self.estado = 6
            self.columna += 1
            self.buffer += caracter
        elif caracter.isalpha():
            self.estado = 11
            self.columna += 1
            self.buffer += caracter
        elif caracter == '=':
            self.estado = 12
            self.columna += 1
            self.buffer += caracter
        elif caracter == '(':
            self.estado = 13
            self.columna += 1
            self.buffer += caracter
        elif caracter == ')':
            self.estado = 14
            self.columna += 1
            self.buffer += caracter
        elif caracter == ';':
            self.estado = 15
            self.columna += 1
            self.buffer += caracter
        elif caracter == ',':
            self.estado = 16
            self.columna += 1
            self.buffer += caracter
        elif caracter == '"':
            self.estado = 17
            self.columna += 1
            self.buffer += caracter
        elif caracter in [' ']:
            self.columna += 1
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter == '#':
            pass
        else:
            self.agregarError(caracter)
            self.estado = 0
            self.columna += 1
            self.buffer = ''

    def s1(self,caracter):
        if caracter == '-':
            self.estado = 2
            self.columna += 1
            self.buffer += caracter
        else:
            self.agregarError(self.buffer)
            self.estado = 0
            self.columna += 1
            self.buffer = ''

    def s2(self,caracter):
        if caracter == '-':
            self.estado = 3
            self.columna += 1
            self.buffer += caracter
        else:
            self.agregarError(self.buffer)
            self.estado = 0
            self.columna += 1
            self.buffer = ''

    def s3(self,caracter):
        if caracter != '\n':
            self.estado = 4
            self.columna += 1
            self.buffer += caracter
        else:
            # reconoce comentario ---
            self.estado = 5
            self.columna = 1
            self.linea += 1

    def s4(self,caracter):
        if caracter != '\n':
            self.estado = 4
            self.columna += 1
            self.buffer += caracter
        else:
            # reconoce comentario ---jhihu huihui
            self.estado = 5
            self.columna = 1
            self.linea += 1

    def s5(self):
        table_str = str(f'Comentario Simple: {self.buffer}')
        self.estado = 0
        self.i -= 1
        self.buffer = ''
        return table_str

    def s6(self,caracter):
        if caracter == '*':
            self.estado = 7
            self.columna += 1
            self.buffer += caracter
        else:
            self.agregarError(self.buffer)
            # self.agregarError(caracter)
            self.estado = 0
            self.columna += 1
            self.buffer = ''

    def s7(self,caracter):
        if caracter != '*':
            self.estado = 8
            self.columna += 1
            self.buffer += caracter
        else:
            self.estado = 9
            self.columna += 1
            self.buffer += caracter

    def s8(self,caracter):
        if caracter != '*':
            self.estado = 8
            self.columna += 1
            self.buffer += caracter
        else:
            self.estado = 9
            self.columna += 1
            self.buffer += caracter

    def s9(self,caracter):
        if caracter != '/':
            self.estado = 8
            self.columna += 1
            self.buffer += caracter
        else:
            self.estado = 10
            self.columna += 1
            self.buffer += caracter

    def s10(self):
        print(f'Comentario Multilinea: {self.buffer}')
        self.estado = 0
        self.i -= 1
        self.buffer = ''

    def s11(self,caracter):
        if caracter.isalpha():
            self.estado = 11
            self.columna += 1
            self.buffer += caracter
        else:
            if self.buffer in ['CrearBD','EliminarBD','CrearColeccion','EliminarColeccion','InsertarUnico','ActualizarUnico','EliminarUnico','BuscarTodo','BuscarUnico','nueva']:
                self.agregarToken(f'Resevada_{self.buffer}',self.buffer)
                self.buffer = ''
                self.estado = 0
            else:
                self.agregarToken('identificador',self.buffer)
                self.buffer = ''
                self.estado = 0

    def s12(self):
        self.agregarToken('igual',self.buffer)
        self.buffer = ''
        self.estado = 0

    def s13(self):
        self.agregarToken('parentesis_a',self.buffer)
        self.buffer = ''
        self.estado = 0

    def s14(self):
        self.agregarToken('parentesis_c',self.buffer)
        self.buffer = ''
        self.estado = 0

    def s15(self):
        self.agregarToken('punto_coma',self.buffer)
        self.buffer = ''
        self.estado = 0

    def s16(self):
        self.agregarToken('coma',self.buffer)
        self.buffer = ''
        self.estado = 0

    def s17(self,caracter):
        if caracter != '"':
            if caracter == '\n':
                self.estado = 17
                self.linea += 1
                self.columna = 1
            elif caracter == '{':
                self.estado = 20
                self.buffer = caracter
            else:
                self.estado = 18
                self.buffer += caracter
            self.columna += 1
        else:
            self.estado = 19
            self.columna += 1
            self.buffer += caracter

    def s18(self,caracter):
        if caracter != '"':
            self.estado = 18
            self.columna += 1
            self.buffer += caracter
        else:
            self.estado = 19
            self.columna += 1
            self.buffer += caracter

    def s19(self):
        self.agregarToken('cadena',self.buffer)
        self.buffer = ''
        self.estado = 0

    def s20(self,caracter):
        if caracter != '}':
            self.estado = 21
            if caracter == '\n':
                self.columna = 1
                self.linea += 1
            else:
                self.columna += 1
                self.buffer += caracter
        else:
            self.estado = 22
            self.columna += 1
            self.buffer += caracter

    def s21(self,caracter):
        if caracter != ')':
            self.estado = 21
            if caracter == '\n':
                self.columna = 1
                self.linea += 1
            else:
                self.columna += 1
                self.buffer += caracter
        else:
            self.estado = 22
            self.columna += 1

    def s22(self):
        try:
            self.buffer = self.buffer[:-1]
        except: pass
        self.agregarToken('data',self.buffer)
        self.buffer = ''
        self.estado = 0
        self.i -= 1

    def analizar (self,cadena):
        print('Analizando...')
        cadena += '\n#'
        self.i = 0
        while(self.i < len(cadena)):
            if self.estado == 0:
                self.s0(cadena[self.i])
            elif self.estado == 1:
                self.s1(cadena[self.i])
            elif self.estado == 2:
                self.s2(cadena[self.i])
            elif self.estado == 3:
                self.s3(cadena[self.i])
            elif self.estado == 4:
                self.s4(cadena[self.i])
            elif self.estado == 5:
                self.s5()
            elif self.estado == 6:
                self.s6(cadena[self.i])
            elif self.estado == 7:
                self.s7(cadena[self.i])
            elif self.estado == 8:
                self.s8(cadena[self.i])
            elif self.estado == 9:
                self.s9(cadena[self.i])
            elif self.estado == 10:
                self.s10()
            elif self.estado == 11:
                self.s11(cadena[self.i])
            elif self.estado == 12:
                self.s12()
            elif self.estado == 13:
                self.s13()
            elif self.estado == 14:
                self.s14()
            elif self.estado == 15:
                self.s15()
            elif self.estado == 16:
                self.s16()
            elif self.estado == 17:
                self.s17(cadena[self.i])
            elif self.estado == 18:
                self.s18(cadena[self.i])
            elif self.estado == 19:
                self.s19()
            elif self.estado == 20:
                self.s20(cadena[self.i])
            elif self.estado == 21:
                self.s21(cadena[self.i])
            elif self.estado == 22:
                self.s22()
            self.i += 1








            