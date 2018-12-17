#!/usr/bin/python
# -*- coding: utf-8 -*-

import AST
from AST import addToClass

'''
Create the basic c structure
'''

# noeud de programme
# retourne la suite d'opcodes de tous les enfants
@addToClass(AST.ProgramNode)
def compile(self):
	c_code = ""
	c_code += "#include <stdio.h>\n"
	c_code += "\n"
	c_code += "int main()\n"
	c_code += "{\n"
	for c in self.children:
		c_code += "\t"
		c_code += c.compile()
	c_code += "}"
	return c_code

# noeud terminal
# si c'est une variable : todo
# si c'est une constante : todo
@addToClass(AST.TokenNode)
def compile(self):
	c_code = ""
	if "$" in self.tok:	# on doit enlever le dollar avant de donner la variable dans le printf
		c_code += "%s" % self.tok[1::]
	else:
		c_code += "%s" % self.tok
	return c_code

# noeud d'assignation de variable
# exécute le noeud à droite du signe =
# todo
@addToClass(AST.AssignNode)
def compile(self):
	c_code = ""
	c_code += "char %s[] = %s;\n" % (self.children[0].tok[1::], self.children[1].tok)
	return c_code

@addToClass(AST.IntDeclareNode)
def compile(self):
	c_code = ""
	c_code += "int %s = %s;\n" & self.children[0].tok[1::], self.children[1].tok
	return c_code

@addToClass(AST.FloatDeclareNode)
def compile(self):
	c_code = ""
	c_code += "float %s = %s;\n" % (self.children[0].tok[1::], self.children[1].tok)
	return c_code

@addToClass(AST.StringDeclareNode)
def compile(self):
	c_code = ""
	c_code += "char %s[] = %s;\n" % (self.children[0].tok[1::], self.children[1].tok)
	return c_code

# noeud d'affichage
# todo
# todo
@addToClass(AST.EchoNode)
def compile(self):
	c_code = ""
	c_code += "printf("
	c_code += self.children[0].compile()
	c_code += ");\n"
	return c_code

# noeud de boucle while
# todo

if __name__ == "__main__":
	from parser_bash import parse
	import sys, os
	prog = open(sys.argv[1]).read()
	ast = parse(prog)
	
	compiled = ast.compile()
	name = os.path.splitext(sys.argv[1])[0]+'.c'
	outfile = open(name, 'w')
	outfile.write(compiled)
	outfile.close()
	print ("Wrote output to", name)
