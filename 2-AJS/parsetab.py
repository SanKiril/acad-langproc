
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "nonassocSTRING_IMPLICITrightASSIGNleftORANDnonassocLELTEQGEGTleftPLUSMINUSleftTIMESDIVIDErightUPLUSUMINUSNOTAND ASSIGN BOOLEAN CHAR CHARACTER DIVIDE ELSE EQ FL FLOAT FUNCTION GE GT IF INT INTEGER LE LET LT MINUS NOT NULL OR PLUS REAL RETURN STRING_EXPLICIT STRING_IMPLICIT TIMES TR TYPE WHILE\n        file : statement file\n            | block file\n            | empty\n        \n        statement : declaration ';'\n            | assignment ';'\n            | definition ';'\n            | expression ';'\n        \n        block : simple_block\n            | function\n        \n        simple_block : if_conditional\n            | while_loop\n        \n        block_body : statement block_body\n            | simple_block block_body\n            | statement\n            | simple_block\n        \n        declaration : LET declaration_content\n        \n        declaration_content : item ',' declaration_content\n            | item\n        \n        item : STRING_IMPLICIT ':' STRING_IMPLICIT\n            | STRING_IMPLICIT\n        \n        assignment : declaration ASSIGN assignment_content\n            | STRING_IMPLICIT ASSIGN assignment_content\n        \n        assignment_content : expression\n            | object\n        \n        definition : TYPE STRING_IMPLICIT ASSIGN object\n        \n        object : '{' object_content '}'\n        \n        object_content : object_item ',' object_content\n            | object_item\n            | empty\n        \n        object_item : key ':' basic_type\n            | key ':' expression\n        \n        key : STRING_EXPLICIT\n            | STRING_IMPLICIT\n        \n        type : basic_type\n            | STRING_IMPLICIT\n        \n        basic_type : INT\n            | FLOAT\n            | CHARACTER\n            | BOOLEAN\n        \n        if_conditional : IF '(' expression ')' '{' block_body '}'\n            | IF '(' expression ')' '{' block_body '}' ELSE '{' block_body '}'\n        \n        while_loop : WHILE '(' expression ')' '{' block_body '}'\n        \n        function : FUNCTION STRING_IMPLICIT '(' argument_list ')' ':' type '{' block_body RETURN expression ';' '}'\n        \n        argument_list : argument_list_nonempty\n            | empty\n        \n        argument_list_nonempty : STRING_IMPLICIT ':' type ',' argument_list_nonempty\n            | STRING_IMPLICIT ':' type\n        \n        expression : '(' expression ')'\n            | function_call\n            | object_call\n        \n        expression : INTEGER\n        \n        expression : REAL\n        \n        expression : CHAR\n        \n        expression : TR\n            | FL\n        \n        expression : NULL\n        \n        expression : STRING_IMPLICIT\n        \n        expression : PLUS expression %prec UPLUS\n        \n        expression : MINUS expression %prec UMINUS\n        \n        expression : NOT expression\n        \n        expression : expression PLUS expression\n            | expression MINUS expression\n            | expression TIMES expression\n            | expression DIVIDE expression\n            | expression AND expression\n            | expression OR expression\n            | expression LT expression\n            | expression LE expression\n            | expression EQ expression\n            | expression GE expression\n            | expression GT expression\n        \n        function_call : STRING_IMPLICIT '(' function_call_list ')'\n        \n        function_call_list : function_call_list_nonempty\n            | empty\n        \n        function_call_list_nonempty : expression ',' function_call_list_nonempty\n            | expression\n        \n        object_call : STRING_IMPLICIT object_attribute_list\n        \n        object_attribute_list : '[' STRING_EXPLICIT ']' object_attribute_list\n            | '.' STRING_IMPLICIT object_attribute_list\n            | '[' STRING_EXPLICIT ']'\n            | '.' STRING_IMPLICIT\n        \n        empty :\n        "
    
_lr_action_items = {'$end':([0,1,2,3,4,9,10,26,27,31,32,33,35,36,37,140,143,152,154,],[-82,0,-82,-82,-3,-8,-9,-10,-11,-1,-2,-4,-5,-6,-7,-40,-42,-41,-43,]),'LET':([0,2,3,9,10,26,27,33,35,36,37,121,122,135,136,140,143,145,148,152,154,],[11,11,11,-8,-9,-10,-11,-4,-5,-6,-7,11,11,11,11,-40,-42,11,11,-41,-43,]),'STRING_IMPLICIT':([0,2,3,9,10,11,13,14,23,24,25,26,27,28,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,56,64,65,69,81,82,92,104,115,116,119,121,122,133,135,136,138,140,143,145,148,149,152,154,],[12,12,12,-8,-9,51,57,59,59,59,59,-10,-11,63,-4,59,-5,-6,-7,59,59,59,59,59,59,59,59,59,59,59,59,59,89,59,59,100,51,102,108,59,100,59,130,12,12,130,12,12,108,-40,-42,12,12,59,-41,-43,]),'TYPE':([0,2,3,9,10,26,27,33,35,36,37,121,122,135,136,140,143,145,148,152,154,],[13,13,13,-8,-9,-10,-11,-4,-5,-6,-7,13,13,13,13,-40,-42,13,13,-41,-43,]),'(':([0,2,3,9,10,12,14,23,24,25,26,27,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,59,63,64,65,104,116,121,122,135,136,140,143,145,148,149,152,154,],[14,14,14,-8,-9,53,14,14,14,14,-10,-11,64,65,-4,14,-5,-6,-7,14,14,14,14,14,14,14,14,14,14,14,14,14,53,92,14,14,14,14,14,14,14,14,-40,-42,14,14,14,-41,-43,]),'INTEGER':([0,2,3,9,10,14,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,64,65,104,116,121,122,135,136,140,143,145,148,149,152,154,],[17,17,17,-8,-9,17,17,17,17,-10,-11,-4,17,-5,-6,-7,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-40,-42,17,17,17,-41,-43,]),'REAL':([0,2,3,9,10,14,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,64,65,104,116,121,122,135,136,140,143,145,148,149,152,154,],[18,18,18,-8,-9,18,18,18,18,-10,-11,-4,18,-5,-6,-7,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-40,-42,18,18,18,-41,-43,]),'CHAR':([0,2,3,9,10,14,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,64,65,104,116,121,122,135,136,140,143,145,148,149,152,154,],[19,19,19,-8,-9,19,19,19,19,-10,-11,-4,19,-5,-6,-7,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-40,-42,19,19,19,-41,-43,]),'TR':([0,2,3,9,10,14,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,64,65,104,116,121,122,135,136,140,143,145,148,149,152,154,],[20,20,20,-8,-9,20,20,20,20,-10,-11,-4,20,-5,-6,-7,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-40,-42,20,20,20,-41,-43,]),'FL':([0,2,3,9,10,14,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,64,65,104,116,121,122,135,136,140,143,145,148,149,152,154,],[21,21,21,-8,-9,21,21,21,21,-10,-11,-4,21,-5,-6,-7,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-40,-42,21,21,21,-41,-43,]),'NULL':([0,2,3,9,10,14,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,64,65,104,116,121,122,135,136,140,143,145,148,149,152,154,],[22,22,22,-8,-9,22,22,22,22,-10,-11,-4,22,-5,-6,-7,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-40,-42,22,22,22,-41,-43,]),'PLUS':([0,2,3,8,9,10,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,58,59,60,61,62,64,65,67,70,71,72,73,74,75,76,77,78,79,80,87,89,91,93,94,103,104,105,106,116,118,121,122,125,135,136,140,143,145,148,149,151,152,154,],[23,23,23,38,-8,-9,-57,23,-49,-50,-51,-52,-53,-54,-55,-56,23,23,23,-10,-11,-4,23,-5,-6,-7,23,23,23,23,23,23,23,23,23,23,23,23,23,-77,38,-57,-58,-59,-60,23,23,38,-61,-62,-63,-64,38,38,38,38,38,38,38,38,-81,-48,38,38,-72,23,-80,-79,23,-78,23,23,38,23,23,-40,-42,23,23,23,38,-41,-43,]),'MINUS':([0,2,3,8,9,10,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,58,59,60,61,62,64,65,67,70,71,72,73,74,75,76,77,78,79,80,87,89,91,93,94,103,104,105,106,116,118,121,122,125,135,136,140,143,145,148,149,151,152,154,],[24,24,24,39,-8,-9,-57,24,-49,-50,-51,-52,-53,-54,-55,-56,24,24,24,-10,-11,-4,24,-5,-6,-7,24,24,24,24,24,24,24,24,24,24,24,24,24,-77,39,-57,-58,-59,-60,24,24,39,-61,-62,-63,-64,39,39,39,39,39,39,39,39,-81,-48,39,39,-72,24,-80,-79,24,-78,24,24,39,24,24,-40,-42,24,24,24,39,-41,-43,]),'NOT':([0,2,3,9,10,14,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,64,65,104,116,121,122,135,136,140,143,145,148,149,152,154,],[25,25,25,-8,-9,25,25,25,25,-10,-11,-4,25,-5,-6,-7,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-40,-42,25,25,25,-41,-43,]),'FUNCTION':([0,2,3,9,10,26,27,33,35,36,37,140,143,152,154,],[28,28,28,-8,-9,-10,-11,-4,-5,-6,-7,-40,-42,-41,-43,]),'IF':([0,2,3,9,10,26,27,33,35,36,37,121,122,135,136,140,143,145,148,152,154,],[29,29,29,-8,-9,-10,-11,-4,-5,-6,-7,29,29,29,29,-40,-42,29,29,-41,-43,]),'WHILE':([0,2,3,9,10,26,27,33,35,36,37,121,122,135,136,140,143,145,148,152,154,],[30,30,30,-8,-9,-10,-11,-4,-5,-6,-7,30,30,30,30,-40,-42,30,30,-41,-43,]),';':([5,6,7,8,12,15,16,17,18,19,20,21,22,49,50,51,54,59,60,61,62,66,67,68,70,71,72,73,74,75,76,77,78,79,80,83,89,91,101,102,103,105,106,107,114,118,151,],[33,35,36,37,-57,-49,-50,-51,-52,-53,-54,-55,-56,-16,-18,-20,-77,-57,-58,-59,-60,-21,-23,-24,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-22,-81,-48,-17,-19,-72,-80,-79,-25,-26,-78,153,]),'ASSIGN':([5,12,49,50,51,57,101,102,],[34,52,-16,-18,-20,90,-17,-19,]),'TIMES':([8,12,15,16,17,18,19,20,21,22,54,58,59,60,61,62,67,70,71,72,73,74,75,76,77,78,79,80,87,89,91,93,94,103,105,106,118,125,151,],[40,-57,-49,-50,-51,-52,-53,-54,-55,-56,-77,40,-57,-58,-59,-60,40,40,40,-63,-64,40,40,40,40,40,40,40,40,-81,-48,40,40,-72,-80,-79,-78,40,40,]),'DIVIDE':([8,12,15,16,17,18,19,20,21,22,54,58,59,60,61,62,67,70,71,72,73,74,75,76,77,78,79,80,87,89,91,93,94,103,105,106,118,125,151,],[41,-57,-49,-50,-51,-52,-53,-54,-55,-56,-77,41,-57,-58,-59,-60,41,41,41,-63,-64,41,41,41,41,41,41,41,41,-81,-48,41,41,-72,-80,-79,-78,41,41,]),'AND':([8,12,15,16,17,18,19,20,21,22,54,58,59,60,61,62,67,70,71,72,73,74,75,76,77,78,79,80,87,89,91,93,94,103,105,106,118,125,151,],[42,-57,-49,-50,-51,-52,-53,-54,-55,-56,-77,42,-57,-58,-59,-60,42,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,42,-81,-48,42,42,-72,-80,-79,-78,42,42,]),'OR':([8,12,15,16,17,18,19,20,21,22,54,58,59,60,61,62,67,70,71,72,73,74,75,76,77,78,79,80,87,89,91,93,94,103,105,106,118,125,151,],[43,-57,-49,-50,-51,-52,-53,-54,-55,-56,-77,43,-57,-58,-59,-60,43,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,43,-81,-48,43,43,-72,-80,-79,-78,43,43,]),'LT':([8,12,15,16,17,18,19,20,21,22,54,58,59,60,61,62,67,70,71,72,73,74,75,76,77,78,79,80,87,89,91,93,94,103,105,106,118,125,151,],[44,-57,-49,-50,-51,-52,-53,-54,-55,-56,-77,44,-57,-58,-59,-60,44,-61,-62,-63,-64,44,44,None,None,None,None,None,44,-81,-48,44,44,-72,-80,-79,-78,44,44,]),'LE':([8,12,15,16,17,18,19,20,21,22,54,58,59,60,61,62,67,70,71,72,73,74,75,76,77,78,79,80,87,89,91,93,94,103,105,106,118,125,151,],[45,-57,-49,-50,-51,-52,-53,-54,-55,-56,-77,45,-57,-58,-59,-60,45,-61,-62,-63,-64,45,45,None,None,None,None,None,45,-81,-48,45,45,-72,-80,-79,-78,45,45,]),'EQ':([8,12,15,16,17,18,19,20,21,22,54,58,59,60,61,62,67,70,71,72,73,74,75,76,77,78,79,80,87,89,91,93,94,103,105,106,118,125,151,],[46,-57,-49,-50,-51,-52,-53,-54,-55,-56,-77,46,-57,-58,-59,-60,46,-61,-62,-63,-64,46,46,None,None,None,None,None,46,-81,-48,46,46,-72,-80,-79,-78,46,46,]),'GE':([8,12,15,16,17,18,19,20,21,22,54,58,59,60,61,62,67,70,71,72,73,74,75,76,77,78,79,80,87,89,91,93,94,103,105,106,118,125,151,],[47,-57,-49,-50,-51,-52,-53,-54,-55,-56,-77,47,-57,-58,-59,-60,47,-61,-62,-63,-64,47,47,None,None,None,None,None,47,-81,-48,47,47,-72,-80,-79,-78,47,47,]),'GT':([8,12,15,16,17,18,19,20,21,22,54,58,59,60,61,62,67,70,71,72,73,74,75,76,77,78,79,80,87,89,91,93,94,103,105,106,118,125,151,],[48,-57,-49,-50,-51,-52,-53,-54,-55,-56,-77,48,-57,-58,-59,-60,48,-61,-62,-63,-64,48,48,None,None,None,None,None,48,-81,-48,48,48,-72,-80,-79,-78,48,48,]),'[':([12,59,89,105,],[55,55,55,55,]),'.':([12,59,89,105,],[56,56,56,56,]),')':([15,16,17,18,19,20,21,22,53,54,58,59,60,61,62,70,71,72,73,74,75,76,77,78,79,80,84,85,86,87,89,91,92,93,94,103,105,106,109,110,111,117,118,126,127,128,129,130,131,132,144,],[-49,-50,-51,-52,-53,-54,-55,-56,-82,-77,91,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,103,-73,-74,-76,-81,-48,-82,112,113,-72,-80,-79,120,-44,-45,-75,-78,-36,-37,-38,-39,-35,-47,-34,-46,]),',':([15,16,17,18,19,20,21,22,50,51,54,59,60,61,62,70,71,72,73,74,75,76,77,78,79,80,87,89,91,96,102,103,105,106,118,124,125,126,127,128,129,130,131,132,],[-49,-50,-51,-52,-53,-54,-55,-56,81,-20,-77,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,104,-81,-48,115,-19,-72,-80,-79,-78,-30,-31,-36,-37,-38,-39,-35,138,-34,]),'}':([15,16,17,18,19,20,21,22,26,27,33,35,36,37,54,59,60,61,62,69,70,71,72,73,74,75,76,77,78,79,80,89,91,95,96,97,103,105,106,115,118,123,124,125,126,127,128,129,134,135,136,137,140,141,142,143,150,152,153,],[-49,-50,-51,-52,-53,-54,-55,-56,-10,-11,-4,-5,-6,-7,-77,-57,-58,-59,-60,-82,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-81,-48,114,-28,-29,-72,-80,-79,-82,-78,-27,-30,-31,-36,-37,-38,-39,140,-14,-15,143,-40,-12,-13,-42,152,-41,154,]),'RETURN':([26,27,33,35,36,37,135,136,140,141,142,143,147,152,],[-10,-11,-4,-5,-6,-7,-14,-15,-40,-12,-13,-42,149,-41,]),'{':([34,52,90,112,113,126,127,128,129,130,132,139,146,],[69,69,69,121,122,-36,-37,-38,-39,-35,-34,145,148,]),':':([51,98,99,100,108,120,],[82,116,-32,-33,119,133,]),'STRING_EXPLICIT':([55,69,115,],[88,99,99,]),']':([88,],[105,]),'INT':([116,119,133,],[126,126,126,]),'FLOAT':([116,119,133,],[127,127,127,]),'CHARACTER':([116,119,133,],[128,128,128,]),'BOOLEAN':([116,119,133,],[129,129,129,]),'ELSE':([140,],[146,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'file':([0,2,3,],[1,31,32,]),'statement':([0,2,3,121,122,135,136,145,148,],[2,2,2,135,135,135,135,135,135,]),'block':([0,2,3,],[3,3,3,]),'empty':([0,2,3,53,69,92,115,],[4,4,4,86,97,111,97,]),'declaration':([0,2,3,121,122,135,136,145,148,],[5,5,5,5,5,5,5,5,5,]),'assignment':([0,2,3,121,122,135,136,145,148,],[6,6,6,6,6,6,6,6,6,]),'definition':([0,2,3,121,122,135,136,145,148,],[7,7,7,7,7,7,7,7,7,]),'expression':([0,2,3,14,23,24,25,34,38,39,40,41,42,43,44,45,46,47,48,52,53,64,65,104,116,121,122,135,136,145,148,149,],[8,8,8,58,60,61,62,67,70,71,72,73,74,75,76,77,78,79,80,67,87,93,94,87,125,8,8,8,8,8,8,151,]),'simple_block':([0,2,3,121,122,135,136,145,148,],[9,9,9,136,136,136,136,136,136,]),'function':([0,2,3,],[10,10,10,]),'function_call':([0,2,3,14,23,24,25,34,38,39,40,41,42,43,44,45,46,47,48,52,53,64,65,104,116,121,122,135,136,145,148,149,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'object_call':([0,2,3,14,23,24,25,34,38,39,40,41,42,43,44,45,46,47,48,52,53,64,65,104,116,121,122,135,136,145,148,149,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'if_conditional':([0,2,3,121,122,135,136,145,148,],[26,26,26,26,26,26,26,26,26,]),'while_loop':([0,2,3,121,122,135,136,145,148,],[27,27,27,27,27,27,27,27,27,]),'declaration_content':([11,81,],[49,101,]),'item':([11,81,],[50,50,]),'object_attribute_list':([12,59,89,105,],[54,54,106,118,]),'assignment_content':([34,52,],[66,83,]),'object':([34,52,90,],[68,68,107,]),'function_call_list':([53,],[84,]),'function_call_list_nonempty':([53,104,],[85,117,]),'object_content':([69,115,],[95,123,]),'object_item':([69,115,],[96,96,]),'key':([69,115,],[98,98,]),'argument_list':([92,],[109,]),'argument_list_nonempty':([92,138,],[110,144,]),'basic_type':([116,119,133,],[124,132,132,]),'type':([119,133,],[131,139,]),'block_body':([121,122,135,136,145,148,],[134,137,141,142,147,150,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> file","S'",1,None,None,None),
  ('file -> statement file','file',2,'p_file','ajs_parser.py',30),
  ('file -> block file','file',2,'p_file','ajs_parser.py',31),
  ('file -> empty','file',1,'p_file','ajs_parser.py',32),
  ('statement -> declaration ;','statement',2,'p_statement','ajs_parser.py',38),
  ('statement -> assignment ;','statement',2,'p_statement','ajs_parser.py',39),
  ('statement -> definition ;','statement',2,'p_statement','ajs_parser.py',40),
  ('statement -> expression ;','statement',2,'p_statement','ajs_parser.py',41),
  ('block -> simple_block','block',1,'p_block','ajs_parser.py',47),
  ('block -> function','block',1,'p_block','ajs_parser.py',48),
  ('simple_block -> if_conditional','simple_block',1,'p_simple_block','ajs_parser.py',54),
  ('simple_block -> while_loop','simple_block',1,'p_simple_block','ajs_parser.py',55),
  ('block_body -> statement block_body','block_body',2,'p_block_body','ajs_parser.py',61),
  ('block_body -> simple_block block_body','block_body',2,'p_block_body','ajs_parser.py',62),
  ('block_body -> statement','block_body',1,'p_block_body','ajs_parser.py',63),
  ('block_body -> simple_block','block_body',1,'p_block_body','ajs_parser.py',64),
  ('declaration -> LET declaration_content','declaration',2,'p_declaration','ajs_parser.py',69),
  ('declaration_content -> item , declaration_content','declaration_content',3,'p_declaration_content','ajs_parser.py',75),
  ('declaration_content -> item','declaration_content',1,'p_declaration_content','ajs_parser.py',76),
  ('item -> STRING_IMPLICIT : STRING_IMPLICIT','item',3,'p_item','ajs_parser.py',81),
  ('item -> STRING_IMPLICIT','item',1,'p_item','ajs_parser.py',82),
  ('assignment -> declaration ASSIGN assignment_content','assignment',3,'p_assignment','ajs_parser.py',88),
  ('assignment -> STRING_IMPLICIT ASSIGN assignment_content','assignment',3,'p_assignment','ajs_parser.py',89),
  ('assignment_content -> expression','assignment_content',1,'p_assignment_content','ajs_parser.py',94),
  ('assignment_content -> object','assignment_content',1,'p_assignment_content','ajs_parser.py',95),
  ('definition -> TYPE STRING_IMPLICIT ASSIGN object','definition',4,'p_definition','ajs_parser.py',101),
  ('object -> { object_content }','object',3,'p_object','ajs_parser.py',106),
  ('object_content -> object_item , object_content','object_content',3,'p_object_content','ajs_parser.py',112),
  ('object_content -> object_item','object_content',1,'p_object_content','ajs_parser.py',113),
  ('object_content -> empty','object_content',1,'p_object_content','ajs_parser.py',114),
  ('object_item -> key : basic_type','object_item',3,'p_object_item','ajs_parser.py',119),
  ('object_item -> key : expression','object_item',3,'p_object_item','ajs_parser.py',120),
  ('key -> STRING_EXPLICIT','key',1,'p_key','ajs_parser.py',125),
  ('key -> STRING_IMPLICIT','key',1,'p_key','ajs_parser.py',126),
  ('type -> basic_type','type',1,'p_type','ajs_parser.py',132),
  ('type -> STRING_IMPLICIT','type',1,'p_type','ajs_parser.py',133),
  ('basic_type -> INT','basic_type',1,'p_basic_type','ajs_parser.py',139),
  ('basic_type -> FLOAT','basic_type',1,'p_basic_type','ajs_parser.py',140),
  ('basic_type -> CHARACTER','basic_type',1,'p_basic_type','ajs_parser.py',141),
  ('basic_type -> BOOLEAN','basic_type',1,'p_basic_type','ajs_parser.py',142),
  ('if_conditional -> IF ( expression ) { block_body }','if_conditional',7,'p_if_conditional','ajs_parser.py',148),
  ('if_conditional -> IF ( expression ) { block_body } ELSE { block_body }','if_conditional',11,'p_if_conditional','ajs_parser.py',149),
  ('while_loop -> WHILE ( expression ) { block_body }','while_loop',7,'p_while_loop','ajs_parser.py',154),
  ('function -> FUNCTION STRING_IMPLICIT ( argument_list ) : type { block_body RETURN expression ; }','function',13,'p_function','ajs_parser.py',159),
  ('argument_list -> argument_list_nonempty','argument_list',1,'p_argument_list','ajs_parser.py',164),
  ('argument_list -> empty','argument_list',1,'p_argument_list','ajs_parser.py',165),
  ('argument_list_nonempty -> STRING_IMPLICIT : type , argument_list_nonempty','argument_list_nonempty',5,'p_argument_list_nonempty','ajs_parser.py',170),
  ('argument_list_nonempty -> STRING_IMPLICIT : type','argument_list_nonempty',3,'p_argument_list_nonempty','ajs_parser.py',171),
  ('expression -> ( expression )','expression',3,'p_expression','ajs_parser.py',176),
  ('expression -> function_call','expression',1,'p_expression','ajs_parser.py',177),
  ('expression -> object_call','expression',1,'p_expression','ajs_parser.py',178),
  ('expression -> INTEGER','expression',1,'p_int','ajs_parser.py',187),
  ('expression -> REAL','expression',1,'p_float','ajs_parser.py',193),
  ('expression -> CHAR','expression',1,'p_character','ajs_parser.py',199),
  ('expression -> TR','expression',1,'p_boolean','ajs_parser.py',205),
  ('expression -> FL','expression',1,'p_boolean','ajs_parser.py',206),
  ('expression -> NULL','expression',1,'p_null','ajs_parser.py',212),
  ('expression -> STRING_IMPLICIT','expression',1,'p_string_implicit','ajs_parser.py',218),
  ('expression -> PLUS expression','expression',2,'p_plus','ajs_parser.py',231),
  ('expression -> MINUS expression','expression',2,'p_minus','ajs_parser.py',242),
  ('expression -> NOT expression','expression',2,'p_not','ajs_parser.py',253),
  ('expression -> expression PLUS expression','expression',3,'p_binary_expression','ajs_parser.py',264),
  ('expression -> expression MINUS expression','expression',3,'p_binary_expression','ajs_parser.py',265),
  ('expression -> expression TIMES expression','expression',3,'p_binary_expression','ajs_parser.py',266),
  ('expression -> expression DIVIDE expression','expression',3,'p_binary_expression','ajs_parser.py',267),
  ('expression -> expression AND expression','expression',3,'p_binary_expression','ajs_parser.py',268),
  ('expression -> expression OR expression','expression',3,'p_binary_expression','ajs_parser.py',269),
  ('expression -> expression LT expression','expression',3,'p_binary_expression','ajs_parser.py',270),
  ('expression -> expression LE expression','expression',3,'p_binary_expression','ajs_parser.py',271),
  ('expression -> expression EQ expression','expression',3,'p_binary_expression','ajs_parser.py',272),
  ('expression -> expression GE expression','expression',3,'p_binary_expression','ajs_parser.py',273),
  ('expression -> expression GT expression','expression',3,'p_binary_expression','ajs_parser.py',274),
  ('function_call -> STRING_IMPLICIT ( function_call_list )','function_call',4,'p_function_call','ajs_parser.py',285),
  ('function_call_list -> function_call_list_nonempty','function_call_list',1,'p_function_call_list','ajs_parser.py',290),
  ('function_call_list -> empty','function_call_list',1,'p_function_call_list','ajs_parser.py',291),
  ('function_call_list_nonempty -> expression , function_call_list_nonempty','function_call_list_nonempty',3,'p_function_call_list_nonempty','ajs_parser.py',296),
  ('function_call_list_nonempty -> expression','function_call_list_nonempty',1,'p_function_call_list_nonempty','ajs_parser.py',297),
  ('object_call -> STRING_IMPLICIT object_attribute_list','object_call',2,'p_object_call','ajs_parser.py',302),
  ('object_attribute_list -> [ STRING_EXPLICIT ] object_attribute_list','object_attribute_list',4,'p_object_attribute_list','ajs_parser.py',307),
  ('object_attribute_list -> . STRING_IMPLICIT object_attribute_list','object_attribute_list',3,'p_object_attribute_list','ajs_parser.py',308),
  ('object_attribute_list -> [ STRING_EXPLICIT ]','object_attribute_list',3,'p_object_attribute_list','ajs_parser.py',309),
  ('object_attribute_list -> . STRING_IMPLICIT','object_attribute_list',2,'p_object_attribute_list','ajs_parser.py',310),
  ('empty -> <empty>','empty',0,'p_empty','ajs_parser.py',315),
]
