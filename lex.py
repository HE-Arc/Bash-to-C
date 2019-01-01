#!/usr/bin/python
# -*- coding: utf-8 -*-

import ply.lex as lex

'''
TODO basic
'''

reserved_words = (
	'echo',
)

tokens = (
	# Variables
	'HEADER',
	'INT',
	'FLOAT',
	'STRING',
	'GET_VARIABLE',
	'SET_VARIABLE',
	'ADD_OP',
	'MUL_OP',
	'newline',
) + tuple(map(lambda s:s.upper(),reserved_words))

literals = '$()='

def t_HEADER(t):
	r'^(\#\!\/bin\/bash)'
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
	r'\$[A-Za-z_]{1}[A-Za-z0-9]*'
	return t

def t_SET_VARIABLE(t):
	r'[A-Za-z_]{1}[A-Za-z0-9]*'
	if t.value in reserved_words:
		t.type = t.value.upper()
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
	prog = open(sys.argv[1]).read()

	lex.input(prog)

	while 1:
		tok = lex.token()
		if not tok: break
		print ("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))
