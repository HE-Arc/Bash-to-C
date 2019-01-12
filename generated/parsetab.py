
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftADD_OPleftMUL_OPleftEQ_CMPleftNE_CMPleftLT_CMPADD_OP DO DONE ECHO ELSE EQ_CMP FI FLOAT FOR GET_VARIABLE HEADER IF IN INT LT_CMP MUL_OP NE_CMP SET_VARIABLE STRING THEN UNTIL WHILE newline programme : HEADER newline statement newline\n        | statement newline programme : HEADER newline statement newline programme\n        | statement newline programme  statement : affectation  affectation : SET_VARIABLE '=' expression  statement : ECHO expression  expression : GET_VARIABLE  expression : FLOAT\n        | INT\n        | STRING  expression : '$' '(' '(' expression ADD_OP expression ')' ')'\n                    | '$' '(' '(' expression MUL_OP expression ')' ')'  expression : expression EQ_CMP expression\n                    | expression NE_CMP expression\n                    | expression LT_CMP expression  block : statement newline  block : statement newline block  statement : IF '[' expression ']' newline THEN newline block FI  statement : IF '[' expression ']' newline THEN newline block ELSE newline block FI  statement : WHILE '[' expression ']' ';' DO newline block DONE  statement : UNTIL '[' expression ']' ';' DO newline block DONE  statement : FOR SET_VARIABLE IN '{' INT '.' '.' INT '}' ';' DO newline block DONE "
    
_lr_action_items = {'HEADER':([0,12,35,],[2,2,2,]),'ECHO':([0,11,12,35,58,59,60,73,77,83,],[5,5,5,5,5,5,5,5,5,5,]),'IF':([0,11,12,35,58,59,60,73,77,83,],[6,6,6,6,6,6,6,6,6,6,]),'WHILE':([0,11,12,35,58,59,60,73,77,83,],[7,7,7,7,7,7,7,7,7,7,]),'UNTIL':([0,11,12,35,58,59,60,73,77,83,],[8,8,8,8,8,8,8,8,8,8,]),'FOR':([0,11,12,35,58,59,60,73,77,83,],[9,9,9,9,9,9,9,9,9,9,]),'SET_VARIABLE':([0,9,11,12,35,58,59,60,73,77,83,],[10,22,10,10,10,10,10,10,10,10,10,]),'$end':([1,12,25,35,44,],[0,-2,-4,-1,-3,]),'newline':([2,3,4,13,14,15,16,17,24,34,36,37,38,40,52,53,54,65,69,70,71,72,74,75,81,82,85,],[11,12,-5,-7,-8,-9,-10,-11,35,-6,-14,-15,-16,46,58,59,60,73,-12,-13,-19,77,-21,-22,83,-20,-23,]),'GET_VARIABLE':([5,19,20,21,23,26,27,28,39,50,51,],[14,14,14,14,14,14,14,14,14,14,14,]),'FLOAT':([5,19,20,21,23,26,27,28,39,50,51,],[15,15,15,15,15,15,15,15,15,15,15,]),'INT':([5,19,20,21,23,26,27,28,39,43,50,51,61,],[16,16,16,16,16,16,16,16,16,49,16,16,68,]),'STRING':([5,19,20,21,23,26,27,28,39,50,51,],[17,17,17,17,17,17,17,17,17,17,17,]),'$':([5,19,20,21,23,26,27,28,39,50,51,],[18,18,18,18,18,18,18,18,18,18,18,]),'[':([6,7,8,],[19,20,21,]),'=':([10,],[23,]),'EQ_CMP':([13,14,15,16,17,30,31,32,34,36,37,38,45,56,57,69,70,],[26,-8,-9,-10,-11,26,26,26,26,-14,-15,-16,26,26,26,-12,-13,]),'NE_CMP':([13,14,15,16,17,30,31,32,34,36,37,38,45,56,57,69,70,],[27,-8,-9,-10,-11,27,27,27,27,27,-15,-16,27,27,27,-12,-13,]),'LT_CMP':([13,14,15,16,17,30,31,32,34,36,37,38,45,56,57,69,70,],[28,-8,-9,-10,-11,28,28,28,28,28,28,-16,28,28,28,-12,-13,]),']':([14,15,16,17,30,31,32,36,37,38,69,70,],[-8,-9,-10,-11,40,41,42,-14,-15,-16,-12,-13,]),'ADD_OP':([14,15,16,17,36,37,38,45,69,70,],[-8,-9,-10,-11,-14,-15,-16,50,-12,-13,]),'MUL_OP':([14,15,16,17,36,37,38,45,69,70,],[-8,-9,-10,-11,-14,-15,-16,51,-12,-13,]),')':([14,15,16,17,36,37,38,56,57,62,63,69,70,],[-8,-9,-10,-11,-14,-15,-16,62,63,69,70,-12,-13,]),'(':([18,29,],[29,39,]),'IN':([22,],[33,]),'{':([33,],[43,]),';':([41,42,76,],[47,48,79,]),'THEN':([46,],[52,]),'DO':([47,48,79,],[53,54,81,]),'.':([49,55,],[55,61,]),'FI':([64,73,78,80,],[71,-17,-18,82,]),'ELSE':([64,73,78,],[72,-17,-18,]),'DONE':([66,67,73,78,84,],[74,75,-17,-18,85,]),'}':([68,],[76,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programme':([0,12,35,],[1,25,44,]),'statement':([0,11,12,35,58,59,60,73,77,83,],[3,24,3,3,65,65,65,65,65,65,]),'affectation':([0,11,12,35,58,59,60,73,77,83,],[4,4,4,4,4,4,4,4,4,4,]),'expression':([5,19,20,21,23,26,27,28,39,50,51,],[13,30,31,32,34,36,37,38,45,56,57,]),'block':([58,59,60,73,77,83,],[64,66,67,78,80,84,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> HEADER newline statement newline','programme',4,'p_programme_statement','parser_bash.py',22),
  ('programme -> statement newline','programme',2,'p_programme_statement','parser_bash.py',23),
  ('programme -> HEADER newline statement newline programme','programme',5,'p_programme_recursive','parser_bash.py',33),
  ('programme -> statement newline programme','programme',3,'p_programme_recursive','parser_bash.py',34),
  ('statement -> affectation','statement',1,'p_statement','parser_bash.py',44),
  ('affectation -> SET_VARIABLE = expression','affectation',3,'p_statement_affectation','parser_bash.py',49),
  ('statement -> ECHO expression','statement',2,'p_echo','parser_bash.py',54),
  ('expression -> GET_VARIABLE','expression',1,'p_expression_var','parser_bash.py',59),
  ('expression -> FLOAT','expression',1,'p_expression_val','parser_bash.py',64),
  ('expression -> INT','expression',1,'p_expression_val','parser_bash.py',65),
  ('expression -> STRING','expression',1,'p_expression_val','parser_bash.py',66),
  ('expression -> $ ( ( expression ADD_OP expression ) )','expression',8,'p_expression_op','parser_bash.py',76),
  ('expression -> $ ( ( expression MUL_OP expression ) )','expression',8,'p_expression_op','parser_bash.py',77),
  ('expression -> expression EQ_CMP expression','expression',3,'p_expression_cmp','parser_bash.py',82),
  ('expression -> expression NE_CMP expression','expression',3,'p_expression_cmp','parser_bash.py',83),
  ('expression -> expression LT_CMP expression','expression',3,'p_expression_cmp','parser_bash.py',84),
  ('block -> statement newline','block',2,'p_block','parser_bash.py',89),
  ('block -> statement newline block','block',3,'p_block_recurssive','parser_bash.py',93),
  ('statement -> IF [ expression ] newline THEN newline block FI','statement',9,'p_condition_if','parser_bash.py',98),
  ('statement -> IF [ expression ] newline THEN newline block ELSE newline block FI','statement',12,'p_condition_if_else','parser_bash.py',103),
  ('statement -> WHILE [ expression ] ; DO newline block DONE','statement',9,'p_while','parser_bash.py',107),
  ('statement -> UNTIL [ expression ] ; DO newline block DONE','statement',9,'p_until','parser_bash.py',111),
  ('statement -> FOR SET_VARIABLE IN { INT . . INT } ; DO newline block DONE','statement',14,'p_for','parser_bash.py',115),
]
