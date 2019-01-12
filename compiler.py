#!/usr/bin/python
# -*- coding: utf-8 -*-

import AST
from AST import addToClass
import re

'''
Create the basic c structure
'''

# Dictionary containing the variables of the program like : {NOM_VAR:[TYPE, VALEUR], ...}
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

@addToClass(AST.ProgramNode)
def compile(self):
	''' Program Node Compilation: 
		return the c code of the program node and of all its children
	''' 
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

@addToClass(AST.VariableNode)
def compile(self):
	''' Variable Node Compilation: 
		return the name of the variable
	'''
	return self.tok[1::]

@addToClass(AST.IntNode)
def compile(self):
	''' Int Node Compilation: 
		return an int value
	'''
	return self.tok

@addToClass(AST.FloatNode)
def compile(self):
	''' Int Node Compilation: 
		return a float value
	'''
	return self.tok

@addToClass(AST.StringNode)
def compile(self):
	''' String Node Compilation: 
		return a string value
	'''
	return self.tok

@addToClass(AST.OpNode)
def compile(self):
	''' Operator Node Compilation: 
		return the c code of an arithmetic operation
	'''
	c_code = ""
	operator = self.op
	operand_1 = self.children[0].compile()
	operand_2 = self.children[1].compile()
	c_code += f"{operand_1} {operator} {operand_2}"
	return c_code

@addToClass(AST.AssignNode)
def compile(self):
	''' Assign Node Compilation: 
		return the c code of a variable declaration or assignment
	'''
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

	# Write the corresponding code of an assignment
	c_code += f" = {affectation};\n"

	return c_code

@addToClass(AST.EchoNode)
def compile(self):
	''' Echo Node compilation:
		return the c code of a echo as a print function use
	'''
	c_code = ""
	c_code += "printf("
	node = self.children[0]
	c_code += convert_string_variables(str(node.tok))
	c_code += ");\n"
	return c_code

def convert_string_variables(str):
	''' convert a string for the use of the printf function '''
	str = str.replace("\"", "")
	regex = re.compile("\$[A-Za-z_]{1}[A-Za-z0-9_]*")
	result = regex.findall(str)
	replace_list = []

	# Search all the variables inside the string str
	# and verify the type in the mean time
	for variable in result:
		var_name = variable[1::]
		type = vars[var_name][0]
		if type == VarType.INT:
			replace_list.append("%d")
		elif type == VarType.FLOAT:
			replace_list.append("%f")
		elif type == VarType.STRING:
			replace_list.append("%s")

	# Replace all the variable insite the string str
	for i, variable in enumerate(result):
		str = regex.sub(replace_list[i], str)

	# Create the valid string for the printf function :
	# STRING, PARAMETRE, PARAMETRES, etc...
	code_c = f"\"{str}\\n\""
	for variable in result:
		var_name = variable[1::]
		code_c += f",{var_name}"

	# Return the converted string
	return code_c


@addToClass(AST.CmpNode)
def compile(self):
	''' Comparator Node compilation:
		return the c code of a comparaison
	'''
	c_code = ""
	cmp = comparators[self.cmp]
	c_code += f"{self.children[0].compile()} {cmp} {self.children[1].compile()}"
	return c_code


@addToClass(AST.CondNode)
def compile(self):
	''' Condition Node compilation:
		return the c code of a condition
	'''
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
	''' Bloc Node compilation:
		return the c code of a block
	'''
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
	''' While Node compilation:
		return the c code of while loop
	'''
	c_code = ""
	c_code += f"while({self.children[0].compile()})"
	c_code += f"{self.children[1].compile()}\n"	#----------------------
	return c_code

@addToClass(AST.UntilNode)
def compile(self):
	''' Until Node compilation:
		return the c code of until loop
	'''
	c_code = ""
	c_code += f"while(!({self.children[0].compile()}))"
	c_code += f"{self.children[1].compile()}\n"	#----------------------
	return c_code

@addToClass(AST.ForNode)
def compile(self):
	''' For Node compilation:
		return the c code of for loop
	'''
	c_code = ""
	c_code += f"for({self.children[0].compile()[:-2]};{self.children[1].compile()};{self.children[2].compile()[:-2]})\n"
	c_code += f"{self.children[3].compile()}\n"
	return c_code

if __name__ == "__main__":
	from parser_bash import parse
	import sys, os
	try:
		prog = open(sys.argv[1]).read()
		ast = parse(prog)
		from parser_bash import header_found
		if not header_found:
			print("WARNING: No Header found")

		compiled = ast.compile()
		name = os.path.splitext(sys.argv[1])[0]+'.c'
		outfile = open(name, 'w')
		outfile.write(compiled)
		outfile.close()
		print ("Wrote output to", name)
	except IndexError:
		print("An error as occured: No file to analyse")
	except SyntaxError as se:
		print(se)
	except AttributeError as ae:
		print("Error : file is invalid")
		print(ae)
	except FileNotFoundError as fnfe:
		print(fnfe)
