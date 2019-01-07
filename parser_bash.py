#!/usr/bin/python
# -*- coding: utf-8 -*-

import ply.yacc as yacc

from lex import tokens
import AST
from tools import *


vars = {}
header_found = False

def p_programme_statement(p):
    ''' programme : HEADER newline statement newline 
        | statement newline'''
    global header_found
    if len(p) == 5 :
        header_found = True
        p[0] = AST.ProgramNode(p[3])
    else:
        p[0] = AST.ProgramNode(p[1])


def p_programme_recursive(p):
    ''' programme : HEADER newline statement newline programme 
        | statement newline programme '''
    global header_found
    if len(p) == 6 :
        header_found = True
        p[0] = AST.ProgramNode([p[3]]+p[5].children)
    else:
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


def p_expression_cmp(p):
    ''' expression : expression EQ_CMP expression
                    | expression NE_CMP expression
                    | expression LT_CMP expression '''
    p[0] = AST.CmpNode(p[2], [p[1], p[3]])


def p_block(p):
    ''' block : statement newline '''
    p[0] = AST.BlockNode(p[1])

def p_block_recurssive(p):
    ''' block : statement newline block '''
    p[0] = AST.BlockNode([p[1]]+p[3].children)


def p_condition_if(p):
    ''' statement : IF '[' expression ']' newline THEN newline block FI '''
    p[0] = AST.CondNode([p[3], p[8]])


def p_condition_if_else(p):
    ''' statement : IF '[' expression ']' newline THEN newline block ELSE newline block FI '''
    p[0] = AST.CondNode([p[3], p[8], p[11]])

def p_while(p):
    ''' statement : WHILE '[' expression ']' ';' DO newline block DONE '''
    p[0] = AST.WhileNode([p[3], p[8]])

def p_until(p):
    ''' statement : UNTIL '[' expression ']' ';' DO newline block DONE '''
    p[0] = AST.UntilNode([p[3], p[8]])

def p_for(p):
    ''' statement : FOR SET_VARIABLE IN '{' INT '.' '.' INT '}' DO newline block DONE '''
    var1 = AST.VariableNode(p[2])
    var2 = AST.VariableNode(p[2])
    init_var = AST.AssignNode([var1, AST.IntNode(int(p[5]))])
    condition = AST.CmpNode('-lt', [var2, AST.IntNode(int(p[8]))])
    p[0] = AST.ForNode([init_var, condition, p[12]])

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
    try:
        prog = open(sys.argv[1]).read()
        result = yacc.parse(prog, debug=False)
        if result:
            if not header_found:
                print(f"WARNING: No Header found")
            print(result)

            import os
            graph = result.makegraphicaltree()
            name = os.path.splitext(sys.argv[1])[0] + '-ast.pdf'
            graph.write_pdf(name)
            print('wrote ast to', name)
        else:
            print('Parsing returned no result!')
    except IndexError:
        print("An error as occured: No file to analyse")
    except Exception as e:
        print(e)
