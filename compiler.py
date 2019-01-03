#!/usr/bin/python
# -*- coding: utf-8 -*-

import AST
from AST import addToClass
from tools import *

'''
Create the basic c structure
'''

# Dictionnaire comportant les variables du programme, sous cette forme: {NOM_VAR:[TYPE, VALEUR], ...}
vars = dict()

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
@addToClass(AST.VariableNode)
def compile(self):
	return self.tok[1::]

@addToClass(AST.IntNode)
def compile(self):
	return self.tok

@addToClass(AST.FloatNode)
def compile(self):
	return self.tok

@addToClass(AST.StringNode)
def compile(self):
	return self.tok

@addToClass(AST.OpNode)
def compile(self):
	c_code = ""
	operator = self.op
	operand_1 = self.children[0].compile()
	operand_2 = self.children[1].compile()
	if operator == "+":
		c_code += f"{operand_1} + {operand_2}"
	elif operator == "-":
		c_code += f"{operand_1} - {operand_2}"
	elif operator == "*":
		c_code += f"{operand_1} * {operand_2}"
	elif operator == "/":
		c_code += f"{operand_1} / {operand_2}"
	return c_code

# noeud d'assignation de variable
# exécute le noeud à droite du signe =
# todo
@addToClass(AST.AssignNode)
def compile(self):
	c_code = ""
	var_name = self.children[0].tok;
	affectation_node = self.children[1]
	affectation = affectation_node.compile();

	# Dans le cas où la variable n'existe pas, on déclare le type
	if var_name not in vars:
		if isinstance(affectation_node, AST.IntNode):
			c_code += f"int {var_name}";
		elif isinstance(affectation_node, AST.FloatNode):
			c_code += f"float {var_name}";
		elif isinstance(affectation_node, AST.StringNode):
			c_code += f"char {var_name}[]";
		elif isinstance(affectation_node, AST.OpNode):
			c_code += f"float {var_name}";
		else:
			c_code += f"char {var_name}[]";

	# Ecrit le code correspondant à une assignation
	c_code += f" = {affectation};\n"

	# Ajoute la nouvelle variable dans le dictionnaire
	if isinstance(self.children[1], AST.VariableNode):
		vars[var_name] = vars[affectation_node.tok[1::]][1]
	else:
		vars[var_name] = affectation

	return c_code

# noeud d'affichage
# todo
# todo
@addToClass(AST.EchoNode)
def compile(self):
	c_code = ""
	c_code += "printf("
	node = self.children[0]
	c_code += node.compile()
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
