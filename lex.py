#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Project: Bash-To-C
Authors: Kim Biloni & Malik Fleury
Python version: 3.6
'''

import ply.lex as lex

reserved_words_c = (
	'auto',	'else',	'long',	'switch',
	'break',	'enum',	'register',	'typedef',
	'case',	'extern',	'return',	'union',
	'char',	'float',	'short',	'unsigned',
	'const',	'for',	'signed',	'void',
	'continue',	'goto',	'sizeof',	'volatile',
	'default',	'if',	'static',	'while',
	'do',	'int',	'struct',	'_Packed',
	'double',
)

reserved_words = (
	'echo',
	# Conditions if
	'if',
	'then',
	'else',
	'fi',
	# boucles
	'while',
	'until',
	'for',
	'in',
	'do',
	'done',
)

tokens = (
	# Header
	'HEADER',
	# Types
	'INT',
	'FLOAT',
	'STRING',
	# Accesseur/setteur variables
	'GET_VARIABLE',
	'SET_VARIABLE',
	# Comparateurs
	'EQ_CMP',		# equal
	'NE_CMP',		# not equal
	'LT_CMP',		# less than
	# Opérateurs
	'ADD_OP',
	'MUL_OP',
	'newline',

) + tuple(map(lambda s:s.upper(),reserved_words))


literals = '$()=[];{}.'


def t_HEADER(t):
	r'^\#\!bin\/bash'
	return t


def t_FLOAT(t):
	r'\d+\.\d+'
	return t


def t_INT(t):
	r'\d+'
	return t


def t_STRING(t):
	r'".*"'
	return t


def t_GET_VARIABLE(t):
	r'\$[A-Za-z_]{1}[A-Za-z0-9_]*'
	if t.value[1::] in reserved_words_c:
		t.value = '$var_' + t.value[1::]
	return t


def t_SET_VARIABLE(t):
	r'[A-Za-z_]{1}[A-Za-z0-9]*'
	if t.value in reserved_words:
		t.type = t.value.upper()
	elif t.value in reserved_words_c:
		t.value = 'var_' + t.value
	return t


def t_EQ_CMP(t):
	r'-eq|-EQ'
	return t

def t_NE_CMP(t):
	r'-ne|-NE'
	return t

def t_LT_CMP(t):
	r'-lt|-LT'
	return t


def t_ADD_OP(t):
	r'[+-]'
	return t


def t_MUL_OP(t):
	r'[\*/]'
	return t


def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	return t


t_ignore  = ' \t'


def t_error(t):
	print ("Illegal character '%s'" % repr(t.value[0]))
	t.lexer.skip(1)


lex.lex()


if __name__ == "__main__":
	import sys
	try:
		prog = open(sys.argv[1]).read()
		lex.input(prog)

		while 1:
			tok = lex.token()
			if not tok: break
			print ("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))

	except IndexError as e:
		print("An error as occured: No file to analyse")
	except FileNotFoundError as fnfe:
		print(fnfe)
