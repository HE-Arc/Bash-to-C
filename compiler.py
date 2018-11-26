# coding=utf-8
import AST
from AST import addToClass

'''
Create the basic c structure
'''

operations = {
	'+' : 'ADD',
	'-' : 'SUB',
	'*' : 'MUL',
	'/' : 'DIV'
}

def whilecounter():
	whilecounter.current += 1
	return whilecounter.current
whilecounter.current = 0

# noeud de programme
# retourne la suite d'opcodes de tous les enfants
@addToClass(AST.ProgramNode)
def compile(self):
	bytecode = ""
	for c in self.children:
		bytecode += c.compile()
	return bytecode

# noeud terminal
# si c'est une variable : todo
# si c'est une constante : todo
@addToClass(AST.TokenNode)
def compile(self):
	bytecode = ""
	if isinstance(self.tok, str):
		bytecode += "PUSHV %s\n" % self.tok
	else:
		bytecode += "PUSHC %s\n" % self.tok
	return bytecode
	
# noeud d'assignation de variable
# exécute le noeud à droite du signe =
# todo
@addToClass(AST.AssignNode)
def compile(self):
	bytecode = ""
	bytecode += self.children[1].compile()
	bytecode += "SET %s\n" % self.children[0].tok
	return bytecode
	
# noeud d'affichage
# todo
# todo
@addToClass(AST.PrintNode)
def compile(self):
	bytecode = ""
	bytecode += self.children[0].compile()
	bytecode += "PRINT\n"
	return bytecode
	
# noeud d'opération arithmétique
# si c'est une opération unaire (nombre négatif), todo
# si c'est une opération binaire, todo
@addToClass(AST.OpNode)
def compile(self):
	bytecode = ""
	if len(self.children) == 1:
		bytecode += self.children[0].compile()
		bytecode += "USUB\n"
	else:
		for c in self.children:
			bytecode += c.compile()
		bytecode += operations[self.op] + "\n"
	return bytecode
	
# noeud de boucle while
# todo
@addToClass(AST.WhileNode)
def compile(self):
	counter = whilecounter()
	bytecode = ""
	bytecode += "JMP cond%s\n" % counter
	bytecode += "body%s: " % counter
	bytecode += self.children[1].compile()
	bytecode += "cond%s: " % counter
	bytecode += self.children[0].compile()
	bytecode += "JINZ body%s\n" % counter
	return bytecode
	
if __name__ == "__main__":
    from parser5 import parse
    import sys, os
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
	print(ast)
    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0]+'.vm'    
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()
    print ("Wrote output to", name)