import ply.lex as lex

'''
TODO basic
'''

reserved_words = (
	'echo'
)

tokens = (
	'HEADER',
	'SET_IDENTIFIER',
	'IDENTIFIER',
	'STRING',
	'NUMBER',
	'newline',
) + tuple(map(lambda s:s.upper(),reserved_words))

literals = '()=$'

def t_HEADER(t):
	r'^(\#!\/bin\/bash)'
	return t

def t_SET_IDENTIFIER(t):
	r'[A-Za-z_]\w*'
	return t

def t_IDENTIFIER(t):
	r'\$[A-Za-z_]\w*'
	if t.value in reserved_words:
		t.type = t.value.upper()
	return t

def t_STRING(t):
	r'\"(\\.|[^"\\])*\"'
	return t

def t_NUMBER(t):
	r'((\d+(\.\d+)*))'
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
