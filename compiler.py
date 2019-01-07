#!/usr/bin/python
# -*- coding: utf-8 -*-

import AST
from AST import addToClass
import re

'''
Create the basic c structure
'''

# Dictionnaire comportant les variables du programme, sous cette forme: {NOM_VAR:[TYPE, VALEUR], ...}
vars = dict()

# Static var that represents the number of indentation for the next line to write
indentation_level = 0

def indentation_generator():
	''' return the tabs string to place after a newline'''
	return "\t" * indentation_level

comparators = {
	'-eq' : '==',
	'-ne' : '!=',
	'-lt' : '<',
}

class VarType:
	INT = "int"
	FLOAT = "float"
	STRING = "char"

# noeud de programme
# retourne la suite d'opcodes de tous les enfants
@addToClass(AST.ProgramNode)
def compile(self):
	c_code = ""
	global indentation_level
	indentation_level = 0
	c_code += "#include <stdio.h>\n"
	c_code += "\n"
	c_code += "int main()\n"
	c_code += "{\n"
	indentation_level += 1
	_identation = indentation_generator()
	for c in self.children:
		c_code += _identation
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
	var_name = self.children[0].tok
	affectation_node = self.children[1]
	affectation = affectation_node.compile()
	if var_name not in vars:
		if isinstance(affectation_node, AST.IntNode):
			vars[var_name] = [VarType.INT, affectation]
			c_code += f"int {var_name}"
		elif isinstance(affectation_node, AST.FloatNode):
			vars[var_name] = [VarType.FLOAT, affectation]
			c_code += f"float {var_name}"
		elif isinstance(affectation_node, AST.StringNode):
			vars[var_name] = [VarType.STRING, affectation]
			c_code += f"char {var_name}[]"
		elif isinstance(affectation_node, AST.OpNode):
			vars[var_name] = [VarType.FLOAT, affectation]
			c_code += f"float {var_name}"
		elif isinstance(affectation_node, AST.VariableNode):
			vars[var_name] = [vars[affectation][0], affectation]
			c_code += f"{vars[affectation][0]} "
			if vars[affectation][0] == VarType.STRING:
				c_code += "*"
			c_code += f"{var_name}"
	else:
		c_code +=  f"{var_name}"
	

	# Ecrit le code correspondant à une assignation
	c_code += f" = {affectation};\n"

	return c_code

# noeud d'affichage
# todo
# todo
@addToClass(AST.EchoNode)
def compile(self):
	c_code = ""
	c_code += "printf("
	node = self.children[0]
	c_code += convert_string_variables(str(node.tok))
	c_code += ");\n"
	return c_code

def convert_string_variables(str):
	str = str.replace("\"", "")
	regex = re.compile("\$[A-Za-z_]{1}[A-Za-z0-9_]*")
	result = regex.findall(str)
	replace_list = []
	# Recherche toutes les variables à l'intérieur de la string
	# et vérifie par la même occasion leur type
	for variable in result:
		var_name = variable[1::]
		type = vars[var_name][0]
		if type == VarType.INT:
			replace_list.append("%d")
		elif type == VarType.FLOAT:
			replace_list.append("%f")
		elif type == VarType.STRING:
			replace_list.append("%s")
	# Remplace toutes les variables à l'intérieur de la string
	for i, variable in enumerate(result):
		str = regex.sub(replace_list[i], str)
	# Créer la string valide pour le printf : STRING, PARAMETRE, PARAMETRES, etc...
	code_c = f"\"{str}\\n\""
	for variable in result:
		var_name = variable[1::]
		code_c += f",{var_name}"
	# Retourne la string convertie
	return code_c


@addToClass(AST.CmpNode)
def compile(self):
	c_code = ""
	cmp = comparators[self.cmp]
	c_code += f"{self.children[0].compile()} {cmp} {self.children[1].compile()}"
	return c_code


@addToClass(AST.CondNode)
def compile(self):
	c_code = ""
	global indentation_level
	_identation = indentation_generator()

	c_code += f"if ({self.children[0].compile()})\n"
	c_code += f"{self.children[1].compile()}\n"
	if len(self.children) > 2 :
		c_code += _identation + "else\n"		#----------------------
		c_code += f"{self.children[2].compile()}\n"
	return c_code


@addToClass(AST.BlockNode)
def compile(self):
	c_code = ""
	global indentation_level
	_identation = indentation_generator()
	
	c_code += _identation + "{\n"
	indentation_level += 1
	_identation = indentation_generator()
	for c in self.children:
		c_code += _identation
		c_code += c.compile()
	indentation_level -= 1
	_identation = indentation_generator()
	c_code += _identation + "}"
	return c_code

@addToClass(AST.WhileNode)
def compile(self):
	c_code = ""
	c_code += f"while({self.children[0].compile()})"
	c_code += f"{self.children[1].compile()}\n"	#----------------------
	return c_code

@addToClass(AST.UntilNode)
def compile(self):
	c_code = ""
	c_code += f"while(!({self.children[0].compile()}))"
	c_code += f"{self.children[1].compile()}\n"	#----------------------
	return c_code

if __name__ == "__main__":
	from parser_bash import parse
	import sys, os
	try:
		prog = open(sys.argv[1]).read()
		ast = parse(prog)

		compiled = ast.compile()
		name = os.path.splitext(sys.argv[1])[0]+'.c'
		outfile = open(name, 'w')
		outfile.write(compiled)
		outfile.close()
		print ("Wrote output to", name)
	except IndexError:
		print("An error as occured: No file to analyse")
