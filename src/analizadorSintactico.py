# -*- coding: utf-8 -*-
import ply.yacc as yacc
from analizadorlexico  import tokens
import analizadorlexico
import re
import os
import sys
from sys import stdin
from analisisSemantica import *

VERBOSE = 1

precedence = (
	('left','OR'),
	('left','AND'),
	('left','NOT'),
	('left','LESS','LESSEQUAL','GREATER','GREATEREQUAL','ISEQUAL','NOTEQUAL'),
	('left','LESS_STRING','LESSEQUAL_STRING','GREATER_STRING','GREATEREQUAL_STRING','ISEQUAL_STRING','NOTEQUAL_STRING'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	('right', 'UMINUS')
)

def p_program(p):
	"""
	program : declaration_list
	"""
    
	p[0] = program(p[1],"program")


def p_program_declaration_list(p):
    """
    declaration_list : declaration_list declaration
    """
    p[0] = program_declaration_list(p[1],p[2],"program_declaration_list")
	

def p_program_declaration(p):
	"""
	declaration_list : declaration
	"""
	p[0] = program_declaration(p[1],"program_declaration")

def p_declaration_import(p):
	"""
	declaration : USE ID SEMICOLON
                | PACKAGE ID SEMICOLON
	"""
	p[0] = declaration_import(Id(p[2]),"declaration_import")

def p_declaration_function(p):
	"""
	declaration : SUB ID LPAREN param_list RPAREN LBLOCK statement_list RBLOCK
	"""
	p[0] = declaration_function(Id(p[2]),p[4],p[7],"declaration_function")

def p_declaration_statement(p):
	"""
	declaration : statement SEMICOLON
				| command
	"""
	p[0] = declaration_statement(p[1],"declaration_statement")

def p_param_list(p):
	"""
	param_list : var_type comma_var_type
			   | empty
	"""
	p[0] = param_list(p[1],p[2],"param_list")

def p_comma_var_type(p):
    """
    comma_var_type : comma_var_type COMMA var_type
                    | COMMA var_type
                    | empty
    """
    p[0] = comma_var_type(p[1],p[3],"comma_var_type")


def p_var_type(p):
	"""
	var_type : DOLLAR ID
			 | AT ID
			 | PERCENT ID
	"""
	p[0] = var_type(Id(p[2]),"var_type")


def p_assign_type(p):
	"""
	assign_type : ASSIGN
                | PLUS_ASSIGN
                | MINUS_ASSIGN
				| MULTIPLY_ASSIGN
				| DIVIDE_ASSIGN
				| MOD_ASSIGN
				| POW_ASSIGN
	"""
	p[0] = assign_type(Assign(p[1]),"assign_type")

def p_statement_list(p):
	"""
	statement_list : statement_list statement SEMICOLON
	"""
	p[0] = statement_list(p[1],p[2],"statement_list")

def p_statement_list_statement(p):
	"""
	statement_list : statement SEMICOLON
	"""
	p[0] = statement_list_statement(p[1],"statement_list_statement")

def p_statement_list_empty(p):
	"""
	statement_list : empty
	"""
	p[0] = null()
	

def p_statement_list_command(p):
	"""
	statement_list : statement_list command
					| command
	"""
	p[0] = statement_list_command(p[1],p[2],"statement_list_command")

def p_statement_var(p):
	"""
	statement : var_declaration
			|	var_assignment
	"""
	p[0] = statement_var(p[1],"statement_var")

def p_statement_var_declaration(p):
	"""
	var_declaration : MY var_type
				| MY var_type assign_type expression
				| MY LPAREN param_list RPAREN
				| MY LPAREN param_list RPAREN assign_type expression
				| MY var_type assign_type LPAREN expression_list RPAREN
				| MY LPAREN param_list RPAREN assign_type LPAREN expression_list RPAREN
	"""
	p[0] = statement_var_declaration(p[2],"statement_var_declaration")

def p_statement_var_assignment(p):
	"""
	var_assignment : var_type assign_type expression
			|	var_type LBRACKET expression RBRACKET assign_type expression
			|	var_type assign_type LPAREN expression_list RPAREN
			|	LPAREN param_list RPAREN assign_type LPAREN expression_list RPAREN
	"""
	p[0] = statement_var_assignment(p[1],p[2],p[3],"statement_var_assignment")

def p_statement_return(p):
	"""
	statement : RETURN LPAREN expression_list RPAREN
	"""
	p[0] = statement_return(p[3],"statement_return")

def p_command_if(p):
	"""
	command : IF LPAREN relop RPAREN LBLOCK statement_list RBLOCK
	"""
	p[0] = command_if(p[1],[2],"command_if")

def p_command_if_else(p):
	"""
	command : IF LPAREN relop RPAREN LBLOCK statement_list RBLOCK ELSE LBLOCK statement_list RBLOCK
	"""
	p[0] = command_if_else(p[3],p[6],p[10],"command_if_else")

def p_statement_print(p):
	"""
	statement : PRINT STRING
	"""
	p[0] = statement_print(String(p[2]),"statement_print")

def p_command_while(p):
	"""
	command : WHILE LPAREN relop RPAREN LBLOCK statement_list RBLOCK
	"""
	p[0] = command_while(p[3],p[6],"command_while")
	

def p_command_for(p):
	"""
	command : FOR LPAREN var_declaration SEMICOLON relop SEMICOLON var_assignment RPAREN LBLOCK statement_list RBLOCK
			| FOR LPAREN var_assignment SEMICOLON relop SEMICOLON var_assignment RPAREN LBLOCK statement_list RBLOCK
	"""
	p[0] = command_for(p[3],p[5],p[7],p[10],"command_for")

def p_statement_call(p):
	"""
	statement :  ID LPAREN expression_list RPAREN
			|	AMPERSANT ID LPAREN expression_list RPAREN
	"""
	p[0] = statement_call(Id(p[1]),p[3],"statement_call")

def p_expression_list(p):
	"""
	expression_list : expression comma_expression
			   | empty
	"""
	p[0] = expression_list(p[1],p[2],"expression_list")

def p_comma_expression(p):
	"""
	comma_expression : comma_expression COMMA expression
				   | COMMA expression
				   | empty
	"""
	p[0] = comma_expression(p[1],p[3],"comma_expression")

def p_expression(p):
	"""
	expression : expression PLUS expression
			   | expression MINUS expression
			   | expression TIMES expression
			   | expression DIVIDE expression
			   | expression MODULUS expression
	"""
	p[0] = expression(p[1],Plus(p[2]),p[3],"expression")

def p_datatype_expression(p):
	"""
	expression : INTEGER
			   | HEX
			   | FLOAT
			   | STRING
	"""
	p[0] = datatype_expression(Integer(p[1]),"datatype_expression")

def p_on_paren_expression(p):
	"""
	expression : LPAREN expression RPAREN
	"""
	p[0] = on_paren_expression(p[2],"on_paren_expression")

def p_call_expression(p):
	"""
	expression : ID LPAREN expression_list RPAREN %prec UMINUS
	"""
	p[0] = call_expression(Id(p[1]),p[3],Uminus(p[6]),"call_expression")

def p_expression_array_access(p):
	"""
	expression : DOLLAR ID LBRACKET expression RBRACKET
	"""
	p[0] = expression_array_access(Id(p[2],p[4],"expression_array_access"))


def p_var_type_expression(p):
	"""
	expression : var_type
	"""
	p[0] = var_type_expression(p[1],"var_type_expression")

def p_expression_uminus_minus(p):
	"""
	expression : MINUS expression %prec UMINUS
	"""
	p[0] = expression_uminus_minus(Minus(p[1]),p[2],Uminus(p[4]),"expression_uminus_minus")

def p_expression_uminus_plus(p):
	"""
	expression : PLUS expression %prec UMINUS
	"""
	p[0] = expression_uminus_plus(Plus(p[1]),p[2],Uminus(p[4],"expression_uminus_plus"))

def p_relop(p):
	"""
	relop : relop_number
			|	relop_string
	"""
	p[0] = relop(p[1],"relop")

def p_relop_number(p):
	"""
	relop_number :	expression ISEQUAL expression
				|	expression NOTEQUAL expression
				|	expression GREATER expression
				|	expression GREATEREQUAL expression
				|	expression LESS expression
				|	expression LESSEQUAL expression
				|	expression COMP expression
	"""
	p[0] = relop_number(p[1],Isequal(p[2]),p[3],"relop_number")

def p_relop_binary(p):
	"""
	relop : relop AND relop
		|	relop OR relop
		|	NOT relop
	"""
	p[0] = relop_binary(p[1],p[3],"relop_binary")

def p_relop_string(p):
	"""
	relop_string :	 expression ISEQUAL_STRING expression
				|	 expression NOTEQUAL_STRING expression
				|	 expression GREATER_STRING expression
				|	 expression GREATEREQUAL_STRING expression
				|	 expression LESS_STRING expression
				|	 expression LESSEQUAL_STRING expression
				|	 expression COMP_STRING expression
	"""
	p[0] = relop_string(p[1],p[3],"relop_string")

def p_empty(p):
	'empty :'''
	pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA:  " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA:  " + str(p.minus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')





  
   
    
    


#aqui comienza




# funcion para que me recora los ficheros 
# def buscarFicheros(source):
#     ficheros=[]
#     numArchivo=''
#     respuestas=False
#     cont = 1
#     nameFile=""

#     for base, dirs, files in os.walk(source):
#                     ficheros.append(files)

#     for file in files:
#         print(str(cont)+". "+file)
#         cont = cont+1
                
#     while respuestas == False:
#         numArchivo = input('\n numero del archivo ')
#         for file in files:
#             if file == files[int(numArchivo)-1]:
#                 respuestas= True
#                 nameFile= str(files[int(numArchivo)-1])
#                 break
#     return nameFile


# def traducir(result):
# 	graphFile = open('graphviztrhee.vz','w')
# 	graphFile.write(result.traducir())
# 	graphFile.close()
# 	print ("El programa traducido se guardo en \"graphviztrhee.vz\"")

# parser = yacc.yacc()
# # Funcion main si se escribe un argumento pasa de primero 
# if __name__ == '__main__':
# 	if (len(sys.argv) > 1):#Si se escribe un fichero por la linea de comandos. Ejemplo: python perl-lexer.py archivo.pl
# 		source = sys.argv[1]
# 	else:#Si no se escribe el fichero en la linea de comandos, el archivo por defecto es...
# 		source = buscarFicheros('../test')
        
            
# 	f = open('../test/'+source, 'r')
# 	data = f.read()
# 	print (data)
# 	result = parser.parse(data,tracking=True)
# 	print("Tu parser reconoció correctamente todo")
	
# result.imprimir(" ")
# print result.traducir()
# traducir(result)



# print (result)

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Has escogido \"%s\"" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

def traducir(result):
	graphFile = open('graphviztrhee.vz','w')
	graphFile.write(result.traducir())
	graphFile.close()
	print ("El programa traducido se guardo en \"graphviztrhee.vz\"")


archivo = buscarFicheros('../test')

fp = open('../test/'+archivo,"r")
cadena = fp.read()
fp.close()

yacc.yacc()
result = yacc.parse(cadena, tracking=True)

# result.imprimir(" ")
#print result.traducir()
traducir(result)



# print (result)
