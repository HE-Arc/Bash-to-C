#!/usr/bin/python
# -*- coding: utf-8 -*-

import ply.yacc as yacc

from lex import tokens
import AST
from tools import *

vars = {}

def p_programme_statement(p):
    ''' programme : statement newline '''
    p[0] = AST.ProgramNode(p[1])


def p_programme_recursive(p):
    ''' programme : statement newline programme '''
    p[0] = AST.ProgramNode([p[1]]+p[3].children)


def p_statement(p):
    ''' statement : affectation '''
    p[0] = p[1]


def p_statement_affectation(p):
    ''' affectation : SET_VARIABLE '=' expression '''
    p[0] = AST.AssignNode([AST.VariableNode(p[1]), p[3]])


def p_echo(p):
    ''' statement : ECHO expression '''
    p[0] = AST.EchoNode(p[2])


def p_expression_var(p):
    ''' expression : GET_VARIABLE '''
    p[0] = AST.VariableNode(p[1])


def p_expression_val(p):
    ''' expression : FLOAT
        | INT
        | STRING '''
    if(is_int(p[1])):
        p[0] = AST.IntNode(int(p[1]))
    elif(is_float(p[1])):
        p[0] = AST.FloatNode(float(p[1]))
    else:
        p[0] = AST.StringNode(p[1])


def p_expression_op(p):
    ''' expression : '$' '(' '(' expression ADD_OP expression ')' ')'
                    | '$' '(' '(' expression MUL_OP expression ')' ')' '''
    p[0] = AST.OpNode(p[5], [p[4], p[6]])


def p_error(p):
    if p:
        print('Syntax error in line %d' % p.lineno)
        yacc.errok()
    else:
        print('Sytax error: unexpected end of file!')


def parse(program):
    ''' parser yacc '''
    return yacc.parse(program)


yacc.yacc(outputdir='generated')

if __name__ == '__main__':
    import sys

    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog, debug=True)
    if result:
        print(result)

        import os
        graph = result.makegraphicaltree()
        name = os.path.splitext(sys.argv[1])[0] + '-ast.pdf'
        graph.write_pdf(name)
        print('wrote ast to', name)
    else:
        print('Parsing returned no result!')
