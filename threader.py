#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Project: Bash-To-C
Authors: Kim Biloni & Malik Fleury
Python version: 3.6
'''

import AST
from AST import addToClass


@addToClass(AST.Node)
def thread(self, lastNode):
    ''' Node thread: thread a Node '''
    for c in self.children:
        lastNode = c.thread(lastNode)
    lastNode.addNext(self)
    return self


@addToClass(AST.CondNode)
def thread(self, lastNode):
    ''' Cond Node thread: thread a CondNode '''
    exitIfNode = self.children[0].thread(lastNode)
    exitIfNode.addNext(self)
    exitBodyIfNode = self.children[1].thread(self)
    # Check for ELSE
    try:
        exitBodyElseNode = self.children[2].thread(self)
        exitBodyElseNode.addNext(self)
    except:
        None
    exitBodyIfNode.addNext(self)
    return self


@addToClass(AST.WhileNode)
@addToClass(AST.UntilNode)
def thread(self, lastNode):
    ''' While/Until Node thread: thread a While/UntilNode '''
    beforeCond = lastNode
    exitCond = self.children[0].thread(lastNode)
    exitCond.addNext(self)
    exitBody = self.children[1].thread(self)
    exitBody.addNext(beforeCond.next[-1])
    return self


@addToClass(AST.ForNode)
def thread(self, lastNode):
    ''' For Node thread: thread a ForNode '''
    beforeCond = lastNode
    exitInit = self.children[0].thread(lastNode)
    exitInit.addNext(self)
    exitCond = self.children[1].thread(self)
    exitCond.addNext(self)
    exitBody = self.children[3].thread(self)
    exitBody.addNext(self)
    exitInc = self.children[2].thread(self)
    exitInc.addNext(beforeCond.next[-1])
    return self


def thread(tree):
    ''' Thread an ASTTree '''
    entry = AST.EntryNode()
    tree.thread(entry)
    return entry


if __name__ == "__main__":
    from parser_bash import parse
    import sys, os
    try:
        prog = open(sys.argv[1]).read()
        ast = parse(prog)
        from parser_bash import header_found
        if not header_found:
            print("WARNING: No Header found")
        print(ast)
        entry = thread(ast)

        graph = ast.makegraphicaltree()
        entry.threadTree(graph)

        name = os.path.splitext(sys.argv[1])[0]+'-ast-threaded.pdf'
        graph.write_pdf(name)
        print ("wrote threaded ast to", name)
    except SyntaxError as se:
        print(se)
    except AttributeError as ae:
        print("Error : file is invalid")
    except FileNotFoundError as fnfe:
        print(fnfe)
