from rply.token import BaseBox
import csv
import os
on_memory_file = None
class MainBox(BaseBox):
    def __init__(self, actionsBox=None):
        self.actionsBox = actionsBox
    def eval(self):
        for actionBox in self.actionsBox.getlist():
            actionBox.eval()

class ActionsBox(BaseBox):#Contiene FunctionBox a ser evaluadas
    def __init__(self, actionsBox=None, actionBox=None):
        self.actionsBox = actionsBox
        self.actionBox = actionBox
    def getlist(self):
        if self.actionsBox:
            return self.actionsBox.getlist() + [self.actionBox]
        else:
            return []

class StateBox(BaseBox):
    def __init__(self, stateToken):
        self.stateToken = stateToken
    def eval(self):
        return self.stateToken.getstr()

class TextBox(BaseBox):
    def __init__(self, stringToken):
        self.stringToken = stringToken
    def eval(self):
        return self.stringToken.getstr()

class MoneyBox(BaseBox):
    def __init__(self, moneyToken):
        self.moneyToken = moneyToken
    def eval(self):
        return float(self.moneyToken.getstr())

class BooleanBox(BaseBox):
    def __init__(self, booleanToken):
        self.booleanToken = booleanToken
    def eval(self):
        if self.booleanToken.getstr() in ['T', 't', '1', 'True']:
            return True
        elif self.booleanToken.getstr() in ['F', 'f', '0', 'False']:
            return False

class ActionBox(BaseBox):
    def __init__(self, functionNameBox=None, stateBox=None, accIdBox=None, usrIdBox=None, stringBox=None, moneyBox=None, booleanBox=None):
        self.functionNameBox = functionNameBox
        self.stateBox = stateBox
        self.accIdBox = accIdBox
        self.usrIdBox = usrIdBox
        self.stringBox = stringBox
        self.moneyBox = moneyBox
        self.booleanBox = booleanBox
    def eval(self):
        if self.functionNameBox.getstr() == "NEW_GROUP":
            print("Parser and lexer success!")
            print(self.functionNameBox.getstr() + "\n" + self.accIdBox.getstr())
        else:
            pass

#Commented code to be  replanted
"""
class FunctionBox(BaseBox):
    def __init__(self, functionNameBox=None, stateBox=None, accIdBox=None, usrIdBox=None, stringBox=None, moneyBox=None, boolBox=None):
        self.functionNameBox = functionNameBox
        self.stateBox = stateBox
        self.accIdBox = accIdBox
        self.usrIdBox = usrIdBox
        self.stringBox = stringBox
        self.moneyBox = moneyBox
        self.boolBox = boolBox

    def eval(self):
        if self.functionNameBox.getstr() == 'NEW_GROUP':
                #NEW_GROUP function in python
                with open(self.accIdBox.getstr, mode='x') as account: #Mode x creates strictly a new file
                    account_string = csv.writer(account, delimiter=',', quotechar='"')
                    account_string.writerow(['*****'])
                    account_string.writerow(['FILENAME', self.accIdBox.getstr])
                    account_string.writerow(['USERS']) #Possible to modify to the right
                    account_string.writerow(['MONEY'])
                    account_string.writerow(['BALANCE','T'])
                    account_string.writerow(['*****'])
                    account_string.writerow(['USER ID', 'ITEM ID', 'VALUE', 'TAXES']) #Possible to modify bellow

                global on_memory_file
                on_memory_file = self.accIdBox.getstr

        elif self.functionNameBox.getstr() == 'READ_GROUP':
            None
        elif self.functionNameBox.getstr() == 'ADD_USER':
            None
        elif self.functionNameBox.getstr() == 'ITEM':
            None
        elif self.functionNameBox.getstr() == 'SETTLE_ACC':
            None
        elif self.functionNameBox.getstr() == 'BALANCE':
            None
        elif self.functionNameBox.getstr() == 'SEARCH_U':
            None
        elif self.functionNameBox.getstr() == 'INVENTORY':
            None
        elif self.functionNameBox.getstr() == 'DEPOSIT':
            None
        elif self.functionNameBox.getstr() == None:
            pass

"""