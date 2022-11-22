import ply.lex as lex
import re
import codecs
import os
import sys
import pandas as pd

reservadas = [

    'IF',
    'PRINT',
    'ELSE',
    'WHILE',
    'FOR',
    'RETURN',
    'LESS_STRING',
    'GREATER_STRING',
    'LESSEQUAL_STRING',
    'GREATEREQUAL_STRING',
    'ISEQUAL_STRING',
    'NOTEQUAL_STRING',
    'COMP_STRING',
    #palabras reservadas (declaraciones)
    'MY',
    'SUB',
    #Palabras reservados(prefijos)
    'USE',
    'PACKAGE',
]

tokens = reservadas+[ 'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'AMPERSANT',
    'ID',
    #operadores
    'PLUS',
    'MINUS',
    'TIMES',
    'MODULUS',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'NOTEQUAL',
    'ISEQUAL',
    'COMP',
    'OR',
    'AND',
    'NOT',
    #simbolos asignacion
    'ASSIGN',
    'PLUS_ASSIGN',
    'MINUS_ASSIGN',
    'MULTIPLY_ASSIGN',
    'DIVIDE_ASSIGN',
    'MOD_ASSIGN',
    'POW_ASSIGN',
    #identifiers
    'DOLLAR',
    'AT',
    'PERCENT',
    #dataypes
    'STRING',
    'INTEGER',
    'FLOAT',
    'HEX',
    ]

# reservadas = {

#     'if':'IF',
#     'print':'PRINT',
#     'else':'ELSE',
#     'while':'WHILE',
#     'for':'FOR',
#     'return':'RETURN',
#     'lt' : 'LESS_STRING',
#     'gt' : 'GREATER_STRING',
#     'le' : 'LESSEQUAL_STRING',
#     'ge' : 'GREATEREQUAL_STRING',
#     'eq' : 'ISEQUAL_STRING',
#     'ne' : 'NOTEQUAL_STRING',
#     'cmp' : 'COMP_STRING',
#     #palabras reservadas (declaraciones)
#     'my':'MY',
#     'sub':'SUB',
#     #Palabras reservados(prefijos)
#     'use':'USE',
#     'package':'PACKAGE',
# }

# tokens = tokens + list(reservadas.values())


def t_KEYWORD(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value not in reservadas:
        t.type = 'ID'
        return t
    t.type = reservadas.get(t.value,'STRING')
    return t


#asignacion
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'


#Reglas (Operadores)
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_LESS   = r'<'
t_MODULUS = r'%'

#identifiers

t_DOLLAR = r'\$'
t_AT = r'@'
t_PERCENT = r'%'

#operadores
t_GREATER = r'>'
t_OR = r'\|'
t_AND = r'\&'
t_NOT = r'!'
t_AMPERSANT = r'\&'

def t_NOTEQUAL(t):
    r'!='
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_COMP(t):
    r'<=>'
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

#operadores asging

t_ASSIGN  = r'='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_MULTIPLY_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='
t_POW_ASSIGN = r'\*\*='




#dataype

t_STRING = r'(\'[^\']*\')|(\"[^\"]*\")'
t_INTEGER = r'[-+]?([1-9][0-9]*)'
t_FLOAT = r'[-+]?([0-9]*\.[0-9]+|[0-9]+)'
t_HEX = r'0[xX][0-9a-fA-F]+'

#ignora

t_ignore = ' \t'

def ID(t):
    r'[a-zA-Z0-9_#!<?]+'
    return t

#coommnet
def t_comments(t):
    r'\#(.)*\n'
    t.lexer.lineno += 1

#new line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#error line
def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

#RESERVADAS

#Reglas (Estructuras de control)
def t_IF(t):
    r'if'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t

def t_RETURN(t):
	r'return'
	return t


#Reglas (Declaraciones)
def t_MY(t):
    r'my'
    return t

def t_SUB(t):
    r'sub'
    return t

#Reglas (Prefijos)

def t_PACKAGE(t):
    r'package'
    return t

def t_DO(t):
    r'do'
    return t


# def buscarFicheros(directorio):
#     ficheros=[]
#     numArchivo = '' 
#     respuesta = False
#     cont = 1

#     for base, dirs, files in os.walk(directorio):
#         ficheros.append(files)

#     for file in files:
#         print(str(cont) + ". "+file) 
#         cont = cont+1
    
#     while respuesta == False:
#         numArchivo = input('\n numero del test: ')
#         for file in files:
#             if file == files[int(numArchivo)-1]:
#                 respuesta = True
#                 break
#     print ( "has escogido \"%s\" \n" %files[int(numArchivo)-1])

#     return files[int(numArchivo)-1]             


# directorio = r'C:\\Users\\Jhorman\\Documents\\Universidad\\Semestre 6\\Compiladores\\Compilador lenguaje perl\\Compiler-Perl\test'
# archivo = buscarFicheros(directorio)
# test =  directorio+archivo
# fp = open(test,'r')
# cadena = fp.read()

# print(cadena)

# # fp.close()

# analizador = lex.lex()

# analizador.input(cadena)

# while True:
#     tok = analizador.token()
#     if not tok : break
#     print(tok)

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

#Funcion main
if __name__ == '__main__':
	if (len(sys.argv) > 1):#Si se escribe un fichero por la linea de comandos. Ejemplo: python perl-lexer.py archivo.pl
		source = sys.argv[1]
	else:#Si no se escribe el fichero en la linea de comandos, el archivo por defecto es...
		source = 'prueba1.pl'
	f = open(source, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()