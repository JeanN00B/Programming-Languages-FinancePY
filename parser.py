from rply import ParserGenerator
from Boxes import (MainBox, ActionsBox, FunctionBox, IdBox, BooleanBox, MoneyBox, StateBox)

pg = ParserGenerator(
['ID_USR_ACC', 'ZERO', 'POSITIVE', 'NEGATIVE', 'STRING', 'MONEY', 'SEMICOLON', 'COMMA', '(',')', 'NEW_LINE', 
'SETTLE_ACC', 'BALANCE', 'ITEM', 'SEARCH_U', 'NEW_GROUP', 'READ_GROUP', 'ADD_USER', 'INVENTORY',
'DEPOSIT', 'BOOLEAN'])
#End of ParseGenerator
@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it was't expected" % token.gettokentype())

@pg.production("mainBox : actionsBox functionBox")
def mainBox(p):
    return MainBox(p[0],p[1])


@pg.production("actionsBox : actionsBox functionBox")
def actionsBox_assignment(p):
    return ActionsBox(p[0],p[1])

@pg.production("actionsBox : ")
def empty_actionsBox_assignment(p):
    return ActionsBox()


@pg.production("stateBox : POSITIVE")
@pg.production("stateBox : NEGATIVE")
@pg.production("stateBox : ZERO")
def statebox_action(p):
    return StateBox(p[0])


@pg.production("idBox : ID_USR_ACC")
def idbox_action(p):
    return IdBox(p[0])


@pg.production("booleanBox : BOOLEAN")
def boolean_action(p):
    return BooleanBox(p[0])


@pg.production("moneyBox : MONEY")
def moneybox_action(p):
    return MoneyBox(p[0])

#---------------------------------------------------#
#define every possible structure for a functionBox
#(self, functionNameBox = None, stateBox = None, accIdBox = None, usrIdBox = None, moneyBox = None, boolBox = None)
@pg.production("functionBox : DEPOSIT ( idBox COMMA moneyBox ) SEMICOLON")
@pg.production("functionBox : ADD_USER ( idBox COMMA moneyBox ) SEMICOLON")
def empty_functionbox(p):
    return FunctionBox(functionNameBox=p[0], stateBox=None, accIdBox=None, usrIdBox=p[2], stringBox=None, moneyBox=p[4], boolBox=None)


@pg.production("functionBox : READ_GROUP ( idBox ) SEMICOLON")
@pg.production("functionBox : NEW_GROUP ( idBox ) SEMICOLON")
def empty_functionbox(p):
    return FunctionBox(functionNameBox=p[0], stateBox=None, accIdBox=p[2], usrIdBox=None, stringBox=None, moneyBox=None, boolBox=None)


@pg.production("functionBox : ITEM ( idBox COMMA STRING COMMA moneyBox ) SEMICOLON")
def empty_functionbox(p):
    return FunctionBox(functionNameBox=p[0], stateBox=None, accIdBox=None, usrIdBox=p[2], stringBox=p[4], moneyBox=p[6], boolBox=None)

@pg.production("functionBox : ITEM ( idBox COMMA STRING COMMA moneyBox COMMA booleanBox ) SEMICOLON")
def empty_functionbox(p):
    return FunctionBox(functionNameBox=p[0], stateBox=None, accIdBox=None, usrIdBox=p[2], stringBox=p[4], moneyBox=p[6], boolBox=p[8])


@pg.production("functionBox : SEARCH_U ( idBox ) SEMICOLON")
@pg.production("functionBox : INVENTORY ( idBox ) SEMICOLON")
def empty_functionbox(p):
    return FunctionBox(functionNameBox=p[0], stateBox=None, accIdBox=None, usrIdBox=p[2], stringBox=None, moneyBox=None, boolBox=None)


@pg.production("functionBox : BALANCE ( stateBox ) SEMICOLON")
def empty_functionbox(p):
    return FunctionBox(functionNameBox=p[0], stateBox=p[2], accIdBox=None, usrIdBox=None, stringBox=None, moneyBox=None, boolBox=None)


@pg.production("functionBox : SETTLE_ACC ( ) SEMICOLON")
def empty_functionbox(p):
    return FunctionBox(functionNameBox=p[0], stateBox=None, accIdBox=None, usrIdBox=None, stringBox=None, moneyBox=None, boolBox=None)


@pg.production("functionBox : ")
def empty_functionbox(p):
    return FunctionBox(functionNameBox=None, stateBox=None, accIdBox=None, usrIdBox=None, stringBox=None, moneyBox=None, boolBox=None) 


parser = pg.build()