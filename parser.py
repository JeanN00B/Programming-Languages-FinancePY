from rply import ParserGenerator
from Boxes import (MainBox, ActionsBox, ActionBox, StateBox, TextBox, MoneyBox, BooleanBox, FunctionBox)

pg = ParserGenerator(
['ID_TOKEN', 'STRING', 'MONEY', 'BOOLEAN', 'STATE_TOKEN', 'SEMICOLON', 'COMMA', '(',')', 
'SETTLE_ACC', 'BALANCE', 'ITEM', 'NEW_GROUP', 'READ_GROUP', 'ADD_USER', 'INVENTORY','DEPOSIT'])

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

@pg.production("stateBox : STATE_TOKEN")
def stateBox_assignment(p):
    return StateBox(p[0]).eval()

@pg.production("textBox : STRING")
@pg.production("textBox : ID_TOKEN")
def textBox_assignment(p):
    return TextBox(p[0]).eval()

@pg.production("moneyBox : MONEY")
def moneyBox_assignment(p):
    return MoneyBox(p[0]).eval()

@pg.production("booleanBox : BOOLEAN")
def boolean_action(p):
    return BooleanBox(p[0]).eval()

@pg.production("functionBox : DEPOSIT")
@pg.production("functionBox : ADD_USER")
@pg.production("functionBox : READ_GROUP")
@pg.production("functionBox : ITEM")
@pg.production("functionBox : INVENTORY")
@pg.production("functionBox : BALANCE")
@pg.production("functionBox : SETTLE_ACC")
@pg.production("functionBox : NEW_GROUP")
def functionBox_eval(p):
    return FunctionBox(p[0]).eval()

@pg.production("parametersBox : stateBox")
def param_eval(p):
    return p[0], None, None, None, None
@pg.production("parametersBox : textBox")
def param_eval2(p):
    return None, p[0], None, None, None
@pg.production("parametersBox : textBox COMMA textBox COMMA moneyBox COMMA booleanBox")
def param_eval3(p):
    return None, p[0], p[2], p[4], p[6]
@pg.production("parametersBox : textBox COMMA textBox COMMA moneyBox")
def textBox_eval4(p):
    return None, p[0], p[2], p[4], None
@pg.production("parametersBox : textBox COMMA moneyBox")
def textBox_eval4(p):
    return None, p[0], None, p[2], None
@pg.production("parametersBox : ")
def textBox_eval5(p):
    return None, None, None, None, None

@pg.production("actionBox : functionBox ( parametersBox ) SEMICOLON")
def final_eval(p):
    return ActionBox(p[0], p[2][0], p[2][1], p[2][2], p[2][3], p[2][4])

parser = pg.build()
