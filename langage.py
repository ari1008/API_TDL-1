import ply.yacc as yacc
import ply.lex as lex

import convertLangage

reserved = {
    "FIND": "FIND",
    "WHERE": "WHERE",
    "LIMIT": "LIMIT",
    "CP": "CP",
    "TYPE": "TYPE",
    "AND": "AND",
}

# Tokens

t_OR = r'\|'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_EQUAL = r'='
t_BIGGER = r'>'
t_SMALLER = r'<'




tokens = [
             'NUMBER', 'MINUS', 'NAME'
             'PLUS', 'TIMES', 'DIVIDE',
             'LPAREN', 'RPAREN', 'TRUE', 'FALSE',  'OR',
             'SEMICOLON', 'NAME', 'EQUAL', 'BIGGER', 'SMALLER',
             'LPARA', 'RPARA', "APO", "MARK", 'COMMA', "ENTITY",
         ] + list(reserved.values())


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Ignored characters
t_ignore = " \t"


def t_ENTITY(t):
    r"""DESC|URL_INFO|ID|PLACE|TITLE|\*"""
    return t


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9-]*'
    t.type = reserved.get(t.value, 'NAME')  # Check for reserved words
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer


# lexer = lex.lex(debug=1) #add
lex.lex()


def p_start(p):
    """start : statement """
    p[0] = ('START', p[1])
    convertLangage.convertLanguage(p[1])


def p_satement_expr(p):
    """statement :  FIND  ENTITIES WHERE CONDITION SEMICOLON
    | FIND  ENTITIES WHERE CONDITION  LIMIT NUMBER SEMICOLON """
    if len(p) == 6:
        p[0] = ('FIND', p[2], p[4])
    else:
        p[0] = ('FIND', p[2], p[4], p[6])


def p_expression_condition(p):
    '''CONDITION  : CP EQUAL NUMBER AND TYPE EQUAL NAME '''
    p[0] = ("CONDITION", p[3], p[7])


def p_expression_expr(p):
    '''ENTITIES : ENTITY
    | ENTITIES COMMA ENTITY '''
    if len(p) == 2:
        p[0] = ("ENTITY", p[1], "EMPTY")
    else:
        p[0] = ("ENTITY", p[1], p[3])


yacc.yacc()
#yacc.yacc(tabmodule="foo")  # after
s5: str = " FIND * WHERE  CP = 78300 AND TYPE = aide-personnes-handicapees  ;"
# s = input('calc > ')
yacc.parse(s5)
