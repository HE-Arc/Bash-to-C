import ply.yacc as yacc

from lex import tokens
import AST

'''
TODO basic
'''

vars = {}

def p_programme_statement(p):
    ''' programme : statement newline '''
    p[0] = AST.ProgramNode(p[1])

def p_programme_recursive(p):
    ''' programme : statement newline programme '''
    p[0] = AST.ProgramNode([p[1]]+p[3].children)

def p_statement(p):
    ''' statement : assignation'''
    p[0] = p[1]

def p_statement_echo(p):
    ''' statement : ECHO expression '''
    p[0] = AST.EchoNode(p[2])

def p_expression_num_or_var(p):
    ''' expression : NUMBER
        | IDENTIFIER
        | STRING '''
    p[0] = AST.TokenNode(p[1])

def p_assign(p):
    ''' assignation : SET_IDENTIFIER '=' expression '''
    p[0] = AST.AssignNode([AST.TokenNode(p[1]),p[3]])

def p_error(p):
    if p:
        print ("Syntax error in line %d" % p.lineno)
        yacc.errok()
    else:
        print ("Sytax error: unexpected end of file!")

def parse(program):
    return yacc.parse(program)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys

    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog, debug=True)
    if result:
        print (result)

        import os
        graph = result.makegraphicaltree()
        name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
        graph.write_pdf(name)
        print ("wrote ast to", name)
    else:
        print ("Parsing returned no result!")
