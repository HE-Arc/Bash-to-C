
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ADD_OP DO DONE ECHO ELSE EQ_CMP FI FLOAT GET_VARIABLE HEADER IF INT LT_CMP MUL_OP NE_CMP SET_VARIABLE STRING THEN UNTIL WHILE newline programme : statement newline  programme : statement newline programme  statement : affectation  affectation : SET_VARIABLE '=' expression  statement : ECHO expression  expression : GET_VARIABLE  expression : FLOAT\n        | INT\n        | STRING  expression : '$' '(' '(' expression ADD_OP expression ')' ')'\n                    | '$' '(' '(' expression MUL_OP expression ')' ')'  expression : expression EQ_CMP expression\n                    | expression NE_CMP expression\n                    | expression LT_CMP expression  block : statement newline  block : statement newline block  statement : IF '[' expression ']' newline THEN newline block FI  statement : IF '[' expression ']' newline THEN newline block ELSE newline block FI  statement : WHILE '[' expression ']' ';' DO newline block DONE  statement : UNTIL '[' expression ']' ';' DO newline block DONE "
    
_lr_action_items = {'ECHO':([0,9,47,48,49,60,63,],[4,4,4,4,4,4,4,]),'IF':([0,9,47,48,49,60,63,],[5,5,5,5,5,5,5,]),'WHILE':([0,9,47,48,49,60,63,],[6,6,6,6,6,6,6,]),'UNTIL':([0,9,47,48,49,60,63,],[7,7,7,7,7,7,7,]),'SET_VARIABLE':([0,9,47,48,49,60,63,],[8,8,8,8,8,8,8,]),'$end':([1,9,20,],[0,-1,-2,]),'newline':([2,3,10,11,12,13,14,28,29,30,31,33,42,43,44,53,56,57,58,59,61,62,66,],[9,-3,-5,-6,-7,-8,-9,-4,-12,-13,-14,37,47,48,49,60,-10,-11,-17,63,-19,-20,-18,]),'GET_VARIABLE':([4,16,17,18,19,21,22,23,32,40,41,],[11,11,11,11,11,11,11,11,11,11,11,]),'FLOAT':([4,16,17,18,19,21,22,23,32,40,41,],[12,12,12,12,12,12,12,12,12,12,12,]),'INT':([4,16,17,18,19,21,22,23,32,40,41,],[13,13,13,13,13,13,13,13,13,13,13,]),'STRING':([4,16,17,18,19,21,22,23,32,40,41,],[14,14,14,14,14,14,14,14,14,14,14,]),'$':([4,16,17,18,19,21,22,23,32,40,41,],[15,15,15,15,15,15,15,15,15,15,15,]),'[':([5,6,7,],[16,17,18,]),'=':([8,],[19,]),'EQ_CMP':([10,11,12,13,14,25,26,27,28,29,30,31,36,45,46,56,57,],[21,-6,-7,-8,-9,21,21,21,21,21,21,21,21,21,21,-10,-11,]),'NE_CMP':([10,11,12,13,14,25,26,27,28,29,30,31,36,45,46,56,57,],[22,-6,-7,-8,-9,22,22,22,22,22,22,22,22,22,22,-10,-11,]),'LT_CMP':([10,11,12,13,14,25,26,27,28,29,30,31,36,45,46,56,57,],[23,-6,-7,-8,-9,23,23,23,23,23,23,23,23,23,23,-10,-11,]),']':([11,12,13,14,25,26,27,29,30,31,56,57,],[-6,-7,-8,-9,33,34,35,-12,-13,-14,-10,-11,]),'ADD_OP':([11,12,13,14,29,30,31,36,56,57,],[-6,-7,-8,-9,-12,-13,-14,40,-10,-11,]),'MUL_OP':([11,12,13,14,29,30,31,36,56,57,],[-6,-7,-8,-9,-12,-13,-14,41,-10,-11,]),')':([11,12,13,14,29,30,31,45,46,50,51,56,57,],[-6,-7,-8,-9,-12,-13,-14,50,51,56,57,-10,-11,]),'(':([15,24,],[24,32,]),';':([34,35,],[38,39,]),'THEN':([37,],[42,]),'DO':([38,39,],[43,44,]),'FI':([52,60,64,65,],[58,-15,-16,66,]),'ELSE':([52,60,64,],[59,-15,-16,]),'DONE':([54,55,60,64,],[61,62,-15,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programme':([0,9,],[1,20,]),'statement':([0,9,47,48,49,60,63,],[2,2,53,53,53,53,53,]),'affectation':([0,9,47,48,49,60,63,],[3,3,3,3,3,3,3,]),'expression':([4,16,17,18,19,21,22,23,32,40,41,],[10,25,26,27,28,29,30,31,36,45,46,]),'block':([47,48,49,60,63,],[52,54,55,64,65,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement newline','programme',2,'p_programme_statement','parser_bash.py',15),
  ('programme -> statement newline programme','programme',3,'p_programme_recursive','parser_bash.py',20),
  ('statement -> affectation','statement',1,'p_statement','parser_bash.py',25),
  ('affectation -> SET_VARIABLE = expression','affectation',3,'p_statement_affectation','parser_bash.py',30),
  ('statement -> ECHO expression','statement',2,'p_echo','parser_bash.py',35),
  ('expression -> GET_VARIABLE','expression',1,'p_expression_var','parser_bash.py',40),
  ('expression -> FLOAT','expression',1,'p_expression_val','parser_bash.py',45),
  ('expression -> INT','expression',1,'p_expression_val','parser_bash.py',46),
  ('expression -> STRING','expression',1,'p_expression_val','parser_bash.py',47),
  ('expression -> $ ( ( expression ADD_OP expression ) )','expression',8,'p_expression_op','parser_bash.py',57),
  ('expression -> $ ( ( expression MUL_OP expression ) )','expression',8,'p_expression_op','parser_bash.py',58),
  ('expression -> expression EQ_CMP expression','expression',3,'p_expression_cmp','parser_bash.py',63),
  ('expression -> expression NE_CMP expression','expression',3,'p_expression_cmp','parser_bash.py',64),
  ('expression -> expression LT_CMP expression','expression',3,'p_expression_cmp','parser_bash.py',65),
  ('block -> statement newline','block',2,'p_block','parser_bash.py',70),
  ('block -> statement newline block','block',3,'p_block_recurssive','parser_bash.py',74),
  ('statement -> IF [ expression ] newline THEN newline block FI','statement',9,'p_condition_if','parser_bash.py',79),
  ('statement -> IF [ expression ] newline THEN newline block ELSE newline block FI','statement',12,'p_condition_if_else','parser_bash.py',84),
  ('statement -> WHILE [ expression ] ; DO newline block DONE','statement',9,'p_while','parser_bash.py',88),
  ('statement -> UNTIL [ expression ] ; DO newline block DONE','statement',9,'p_until','parser_bash.py',92),
]
