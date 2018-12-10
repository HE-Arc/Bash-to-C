# coding=utf-8
import AST
from AST import addToClass

'''
Create the basic c structure
'''

# noeud de programme
# retourne la suite d'opcodes de tous les enfants
@addToClass(AST.ProgramNode)
def compile(self):
	bytecode = ""
	bytecode += "#include <stdio.h>\n"
	bytecode += "\n"
	bytecode += "int main()\n"
	bytecode += "{\n"
	for c in self.children:
		bytecode += "\t"
		bytecode += c.compile()
	bytecode += "}"

	return bytecode

# noeud terminal
# si c'est une variable : todo
# si c'est une constante : todo
@addToClass(AST.TokenNode)
def compile(self):
	bytecode = ""
	bytecode += "%s" % self.tok
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
@addToClass(AST.EchoNode)
def compile(self):
	bytecode = ""
	bytecode += "printf("
	bytecode += self.children[0].compile()
	bytecode += ");\n"
	return bytecode

# noeud de boucle while
# todo

if __name__ == "__main__":
    from parser import parse
    import sys, os
    prog = open(sys.argv[1]).read()
    ast = parse(prog)

    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0]+'.c'
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()
    print ("Wrote output to", name)
