from rply import ParserGenerator
from Boxes import (MainBox, ActionsBox, ActionBox, StateBox, TextBox, MoneyBox, BooleanBox)

pg = ParserGenerator(
['ID_TOKEN', 'STRING', 'MONEY', 'BOOLEAN', 'STATE_TOKEN', 'SEMICOLON', 'COMMA', '(',')', 
'SETTLE_ACC', 'BALANCE', 'ITEM', 'SEARCH_USER', 'NEW_GROUP', 'READ_GROUP', 'ADD_USER', 'INVENTORY',
'DEPOSIT'])
#End of ParseGenerator
@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it was't expected" % token.gettokentype())

@pg.production("mainBox : actionsBox")
def mainBox_eval(p):
    return MainBox(p[0])

@pg.production("actionsBox : actionsBox actionBox")
def actionsBox_assignment(p):
    return ActionsBox(p[0],p[1])

@pg.production("actionsBox : actionBox")
def actionBox_assignment(p):
    return ActionsBox(None, p[0])

@pg.production("actionsBox : ")
def empty_actionsBox_assignment(p):
    return ActionsBox(None, None)

@pg.production("stateBox : STATE_TOKEN")
def stateBox_assignment(p):
    return StateBox(p[0])

@pg.production("textBox : STRING")
@pg.production("textBox : ID_TOKEN")
def textBox_assignment(p):
    return TextBox(p[0])

@pg.production("moneyBox : MONEY")
def moneyBox_assignment(p):
    return MoneyBox(p[0])

@pg.production("booleanBox : BOOLEAN")
def boolean_action(p):
    return BooleanBox(p[0])


#---------------------------------------------------#
#define every possible structure for a actionBox
#(self, functionNameBox = None, stateBox = None, accIdBox = None, usrIdBox = None, moneyBox = None, booleanBox = None)
@pg.production("actionBox : DEPOSIT ( textBox COMMA moneyBox ) SEMICOLON")
@pg.production("actionBox : ADD_USER ( textBox COMMA moneyBox ) SEMICOLON")
def empty_actionBox(p):
    return ActionBox(functionNameBox=p[0], stateBox=None, accIdBox=None, usrIdBox=p[2], stringBox=None, moneyBox=p[4], booleanBox=None)


@pg.production("actionBox : READ_GROUP ( textBox ) SEMICOLON")
@pg.production("actionBox : NEW_GROUP ( textBox ) SEMICOLON")
def empty_actionBox(p):
    return ActionBox(functionNameBox=p[0], stateBox=None, accIdBox=p[2], usrIdBox=None, stringBox=None, moneyBox=None, booleanBox=None)


@pg.production("actionBox : ITEM ( textBox COMMA textBox COMMA moneyBox ) SEMICOLON")
def empty_actionBox(p):
    return ActionBox(functionNameBox=p[0], stateBox=None, accIdBox=None, usrIdBox=p[2], stringBox=p[4], moneyBox=p[6], booleanBox=None)

@pg.production("actionBox : ITEM ( textBox COMMA textBox COMMA moneyBox COMMA booleanBox ) SEMICOLON")
def empty_actionBox(p):
    return ActionBox(functionNameBox=p[0], stateBox=None, accIdBox=None, usrIdBox=p[2], stringBox=p[4], moneyBox=p[6], booleanBox=p[8])


@pg.production("actionBox : SEARCH_USER ( textBox ) SEMICOLON")
@pg.production("actionBox : INVENTORY ( textBox ) SEMICOLON")
def empty_actionBox(p):
    return ActionBox(functionNameBox=p[0], stateBox=None, accIdBox=None, usrIdBox=p[2], stringBox=None, moneyBox=None, booleanBox=None)


@pg.production("actionBox : BALANCE ( stateBox ) SEMICOLON")
def empty_actionBox(p):
    return ActionBox(functionNameBox=p[0], stateBox=p[2], accIdBox=None, usrIdBox=None, stringBox=None, moneyBox=None, booleanBox=None)


@pg.production("actionBox : SETTLE_ACC ( ) SEMICOLON")
def empty_actionBox(p):
    return ActionBox(functionNameBox=p[0], stateBox=None, accIdBox=None, usrIdBox=None, stringBox=None, moneyBox=None, booleanBox=None)


@pg.production("actionBox : ")
def empty_actionBox():
    return ActionBox(functionNameBox=None, stateBox=None, accIdBox=None, usrIdBox=None, stringBox=None, moneyBox=None, booleanBox=None) 

parser = pg.build()
