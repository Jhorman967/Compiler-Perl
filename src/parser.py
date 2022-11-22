# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import ply.yacc as yacc
from analizadorlexico  import tokens
import analizadorlexico
import re
import os
import sys
from sys import stdin


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
	pass

def p_program_declaration_list(p):
	"""
	declaration_list : declaration_list declaration
	"""
	pass

def p_program_declaration(p):
	"""
	declaration_list : declaration
	"""
	pass

def p_declaration_import(p):
	"""
	declaration : USE ID SEMICOLON
                | PACKAGE ID SEMICOLON
	"""
	pass

def p_declaration_function(p):
	"""
	declaration : SUB ID LPAREN param_list RPAREN LBLOCK statement_list RBLOCK
	"""
	pass

def p_declaration_statement(p):
	"""
	declaration : statement SEMICOLON
				| command
	"""
	pass

def p_param_list(p):
	"""
	param_list : var_type comma_var_type
			   | empty
	"""
	pass

def p_comma_var_type(p):
	"""
	comma_var_type : comma_var_type COMMA var_type
				   | COMMA var_type
				   | empty
	"""

def p_var_type(p):
	"""
	var_type : DOLLAR ID
			 | AT ID
			 | PERCENT ID
	"""
	pass

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
	pass

def p_statement_list(p):
	"""
	statement_list : statement_list statement SEMICOLON
	"""
	pass

def p_statement_list_statement(p):
	"""
	statement_list : statement SEMICOLON
	"""
	pass

def p_statement_list_empty(p):
	"""
	statement_list : empty
	"""
	pass

def p_statement_list_command(p):
	"""
	statement_list : statement_list command
					| command
	"""
	pass

def p_statement_var(p):
	"""
	statement : var_declaration
			|	var_assignment
	"""
	pass

def p_statement_var_declaration(p):
	"""
	var_declaration : MY var_type
				| MY var_type assign_type expression
				| MY LPAREN param_list RPAREN
				| MY LPAREN param_list RPAREN assign_type expression
				| MY var_type assign_type LPAREN expression_list RPAREN
				| MY LPAREN param_list RPAREN assign_type LPAREN expression_list RPAREN
	"""
	pass

def p_statement_var_assignment(p):
	"""
	var_assignment : var_type assign_type expression
			|	var_type LBRACKET expression RBRACKET assign_type expression
			|	var_type assign_type LPAREN expression_list RPAREN
			|	LPAREN param_list RPAREN assign_type LPAREN expression_list RPAREN
	"""
	pass

def p_statement_return(p):
	"""
	statement : RETURN LPAREN expression_list RPAREN
	"""
	pass

def p_command_if(p):
	"""
	command : IF LPAREN relop RPAREN LBLOCK statement_list RBLOCK
	"""
	pass

def p_command_if_else(p):
	"""
	command : IF LPAREN relop RPAREN LBLOCK statement_list RBLOCK ELSE LBLOCK statement_list RBLOCK
	"""
	pass

def p_statement_print(p):
	"""
	statement : PRINT STRING
	"""
	pass

def p_command_while(p):
	"""
	command : WHILE LPAREN relop RPAREN LBLOCK statement_list RBLOCK
	"""
	pass

def p_command_for(p):
	"""
	command : FOR LPAREN var_declaration SEMICOLON relop SEMICOLON var_assignment RPAREN LBLOCK statement_list RBLOCK
			| FOR LPAREN var_assignment SEMICOLON relop SEMICOLON var_assignment RPAREN LBLOCK statement_list RBLOCK
	"""
	pass

def p_statement_call(p):
	"""
	statement :  ID LPAREN expression_list RPAREN
			|	AMPERSANT ID LPAREN expression_list RPAREN
	"""
	pass

def p_expression_list(p):
	"""
	expression_list : expression comma_expression
			   | empty
	"""
	pass

def p_comma_expression(p):
	"""
	comma_expression : comma_expression COMMA expression
				   | COMMA expression
				   | empty
	"""

def p_expression(p):
	"""
	expression : expression PLUS expression
			   | expression MINUS expression
			   | expression TIMES expression
			   | expression DIVIDE expression
			   | expression MODULUS expression
	"""
	pass

def p_datatype_expression(p):
	"""
	expression : INTEGER
			   | HEX
			   | FLOAT
			   | STRING
	"""
	pass

def p_on_paren_expression(p):
	"""
	expression : LPAREN expression RPAREN
	"""
	pass

def p_call_expression(p):
	"""
	expression : ID LPAREN expression_list RPAREN %prec UMINUS
	"""

def p_expression_array_access(p):
	"""
	expression : DOLLAR ID LBRACKET expression RBRACKET
	"""
	pass


def p_var_type_expression(p):
	"""
	expression : var_type
	"""

def p_expression_uminus_minus(p):
	"""
	expression : MINUS expression %prec UMINUS
	"""
	pass

def p_expression_uminus_plus(p):
	"""
	expression : PLUS expression %prec UMINUS
	"""
	pass

def p_relop(p):
	"""
	relop : relop_number
			|	relop_string
	"""
	pass

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
	pass

def p_relop_binary(p):
	"""
	relop : relop AND relop
		|	relop OR relop
		|	NOT relop
	"""
	pass

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
	pass

def p_empty(p):
	'empty :'
	pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')


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



parser = yacc.yacc()


archivo = buscarFicheros('../test')

fp = open('../test/'+archivo,"r")
cadena = fp.read()
fp.close()

yacc.yacc()
result = yacc.parse(cadena, tracking=True)

# result.imprimir(" ")
#print result.traducir()
# traducir(result)



# print (result)
