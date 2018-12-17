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
	'HEADER',
	'SEQUENCE',
	'INT',
	'FLOAT',
	'STRING',
	'ADD',
	'MUL',
	'EVALUATE',
	'L_EVALUATE',
	'R_EVALUATE',
	'newline',
) + tuple(map(lambda s:s.upper(),reserved_words))

literals = '()=$'

def t_HEADER(t):
	r'^(\#!\/bin\/bash\n)'
	return t

def t_SEQUENCE(t):
	r'[A-Za-z_]\w*'
	if t.value in reserved_words:
		t.type = t.value.upper()
	return t

def t_INT(t):
	r'[1-9]*[0-9]'
	return t

def t_FLOAT(t):
	r'\d+\.\d+'
	return t

def t_STRING(t):
	r'\"(\\.|[^"\\])*\"'
	return t

def t_ADD(t):
	r'[+-]'
	return t

def t_MUL(t):
	r'[*/]'
	return t

def t_EVALUATE(t):
	r'\$[A-Za-z_]\w*'
	return t

def t_L_EVALUATE(t):
	r'\$\(\('
	return t

def t_R_EVALUATE(t):
	r'\)\)'
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
