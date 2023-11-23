import ply.lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    # manejo de palabras reservadas como identificadores
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'COUT',
    'CIN',
   'GET',
   'CADENA',
  'RETURN',
   'VOID',
    'INT',
    'END',
)
tokens = reservada + (
    'IDENTIFICADOR',
    'ENTERO',
    'ASIGNAR',

    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',

   'MINUSMINUS',
   'PLUSPLUS',

    #Condiones
   'SI',
    'SINO',
    #Ciclos
   'MIENTRAS',
   'PARA',
   'SENTENCIADOBUCLE',
   'SENTENCIALOOPBUCLE',
   'SENTENCIAUNTILBUCLE',
   'SENTENCIANEXTBUCLE',


    #sentencias
    'THEN',
    'ELSEIF',
    'SELECT',
    'CASE',
    'TRY',
    'EXITTRY',
    'CATCH',
    'WHEN',
    'FINALLY',
   
    #logica
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    'XOR',
    'EQV',
    'IMP',

      #DATA
    'CHAR',
    'TIPODATOSTRING',
    'TIPODATOSINGLE',
    'TIPODATODOUBLE',
    'TIPODATODECIMAL',
    'TIPODATOSHORT',
    'TIPODATOINTEGER',
    'TIPODATOLONG',
    'BINARIO',
    'HEXADECIMAL',
    'OCTAL',
    
    #clases

    'PUBLICCLASS',
    'PUBLICPROPERTY',
    'ENDCLASS',
    #METODOS

    'SUBNEW',
    'ENDSUB',
    'PUBLICFUNCTION',
    'ENDFUNCTION',
    'OVERLOADS',
    'CLASS',
    'STRUCTURE',
    'ENDSTRUCTURE',


    # Symbolos
    'NUMERAL',

    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    
    # Otros
    'PUNTOCOMA',
    'COMA',
    'COMDOB',
    'MAYORDER', 
    'MAYORIZQ', 
    'SEPARADOR',
)

#  Expresiones Regualres para token.() "function"

t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
# t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'

t_ASIGNAR = r'='
# Expresiones Logicas
#t_AND = r'and'
#t_OR = r'\|{2}'
#t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = ';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMDOB = r'\"'
t_SEPARADOR = r':'
#Or Not Xor Eqv Imp 


#Do, Loop, Until, For, Next


def t_BINARIO(t):
    r'&B'
    return t

def t_HEXADECIMAL(t):
    r'&H'
    return t

def t_OCTAL(t):
    r'&0'
    return t

def t_SENTENCIADOBUCLE(t):
    r'Do'
    return t

def t_SENTENCIALOOPBUCLE(t):
    r'Loop'
    return t

def t_SENTENCIAUNTILBUCLE(t):
    r'Until'
    return t

def t_SENTENCIANEXTBUCLE(t):
    r'Next'
    return t

#METODOS 

def t_SUBNEW(t):
    r'Sub\sNew'
    return t

def t_ENDSUB(t):
    r'End\sSub'
    return t

def t_PUBLICFUNCTION(t):
    r'Public\sFunction'
    return t

def t_ENDFUNCTION(t):
    r'End\sFunction'
    return t

def t_OVERLOADS(t):
    r'Overloads'
    return t
    

###{Integer,Short,Long}

def t_CHAR(t):
    r'Char'
    return t

def t_TIPODATOSTRING(t):
    r'String'
    return t

def t_TIPODATOSINGLE(t):
    r'Single'
    return t

def t_TIPODATODOUBLE(t):
    r'Double'
    return t

def t_TIPODATODECIMAL(t):
    r'Decimal'
    return t

def t_TIPODATOINTEGER(t):
    r'Integer'
    return t

def t_TIPODATOSHORT(t):
    r'Short'
    return t

def t_TIPODATOLONG(t):
    r'Long'
    return t


def t_CLASS(t):
    r'Class'
    return t



def t_STRUCTURE(t):
    r'Structure'
    return t

def t_ENDSTRUCTURE(t):
    r'End\sStructure'
    return t

# ###If, Then ,ElseIf ,End If, Select ,
#Case, Else , End Select, Try , Exit Try ,Catch [ exception [ As type ] ] [
#When Finally , End Try}

def t_THEN(t):
    r'Then'
    return t

def t_ELSEIF(t):
    r'ElseIf'
    return t

def t_SELECT(t):
    r'Select'
    return t

def t_CASE(t):
    r'Case'
    return t

def t_TRY(t):
    r'Try'
    return t

def t_EXITTRY(t):
    r'Exit\sTry'
    return t

def t_CATCH(t):
    r'Catch'
    return t

def t_WHEN(t):
    r'When'
    return t

def t_FINALLY(t):
    r'Finally'
    return t


def t_PUBLICCLASS(t):
    r'Public\sClass'
    return t

def t_PUBLICPROPERTY(t):
    r'Public\sProperty'
    return t

def t_ENDCLASS(t):
    r'End\sClass'
    return t

###

def t_EQV(t):
    r'Eqv'
    return t

def t_IMP(t):
    r'Imp'
    return t

def t_XOR(t):
    r'Xor'
    return t

def t_NOT(t):
    r'Not'
    return t


def t_OR(t):
    r'Or'
    return t

def t_AND(t):
    r'AND'
    return t


def t_INCLUDE(t):
    r'include'
    return t

def t_USING(t):
    r'using'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_STD(t):
    r'std'
    return t

def t_COUT(t):
    r'cout'
    return t

def t_CIN(t):
    r'cin'
    return t

def t_GET(t):
    r'get'
    return t

def t_END(t):
    r'end'
    return t

def t_SINO(t):
    r'else'
    return t

def t_SI(t):
    r'if'
    return t

def t_RETURN(t):
   r'return'
   return t

def t_VOID(t):
   r'void'
   return t

def t_MIENTRAS(t):
    r'while'
    return t

def t_PARA(t):
    r'for'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_MAYORDER(t):
    r'<<'
    return t

def t_MAYORIZQ(t):
    r'>>'
    return t

def t_DISTINTO(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
     r'\/\/(.)*\n'
     t.lexer.lineno += 1
     print("Comentario de una linea")
t_ignore =' \t'

def t_error( t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resultado_lexema)