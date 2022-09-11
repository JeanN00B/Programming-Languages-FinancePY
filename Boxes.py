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
            return [self.actionBox]

class StateBox(BaseBox):
    def __init__(self, stateToken):
        self.stateToken = stateToken
    def eval(self):
        return self.stateToken.getstr()

class TextBox(BaseBox):
    def __init__(self, stringToken):
        self.stringToken = stringToken
    def eval(self):
        self.stringToken =  self.stringToken.getstr()[1:-1] #delete ""
        return self.stringToken

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

class FunctionBox(BaseBox):
    def __init__(self, functionBox):
        self.functionBox = functionBox
    def eval(self):
        return self.functionBox.getstr()

class ActionBox(BaseBox):
    def __init__(self, functionNameBox, stateBox=None, textBox1=None, textBox2=None, moneyBox=None, booleanBox=None):
        self.functionNameBox = functionNameBox
        self.stateBox = stateBox
        self.textBox1 = textBox1    # usr | acc | usr | state |
        self.textBox2 = textBox2    # ___ | ___ | str | _____ |
        self.moneyBox = moneyBox
        self.booleanBox = booleanBox
    def eval(self):
        if self.functionNameBox == "NEW_GROUP":
            #NEW_GROUP -->  self.textBox1 = acc | self.textBox2 = None
            with open(self.textBox1, mode='x') as account: #Mode x creates strictly a new file
                account_string = csv.writer(account, delimiter=',', quotechar='"')
                account_string.writerow(['*****'])
                account_string.writerow(['FILENAME', self.textBox1])
                account_string.writerow(['USERS']) #Possible to modify to the right
                account_string.writerow(['MONEY'])
                account_string.writerow(['BALANCE','T'])
                account_string.writerow(['*****'])
                account_string.writerow(['USER ID', 'ITEM ID', 'VALUE', 'TAXES']) #Possible to modify bellow

            global on_memory_file
            on_memory_file = self.textBox1

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

#Commented code to be  replanted
"""
class FunctionBox(BaseBox):
    def __init__(self, functionNameBox=None, stateBox=None, textBox1=None, textBox2=None, stringBox=None, moneyBox=None, boolBox=None):
        self.functionNameBox = functionNameBox
        self.stateBox = stateBox
        self.textBox1 = textBox1
        self.textBox2 = textBox2
        self.stringBox = stringBox
        self.moneyBox = moneyBox
        self.boolBox = boolBox

    def eval(self):
        if self.functionNameBox.getstr() == 'NEW_GROUP':
                #NEW_GROUP function in python
                with open(self.textBox1.getstr, mode='x') as account: #Mode x creates strictly a new file
                    account_string = csv.writer(account, delimiter=',', quotechar='"')
                    account_string.writerow(['*****'])
                    account_string.writerow(['FILENAME', self.textBox1.getstr])
                    account_string.writerow(['USERS']) #Possible to modify to the right
                    account_string.writerow(['MONEY'])
                    account_string.writerow(['BALANCE','T'])
                    account_string.writerow(['*****'])
                    account_string.writerow(['USER ID', 'ITEM ID', 'VALUE', 'TAXES']) #Possible to modify bellow

                global on_memory_file
                on_memory_file = self.textBox1.getstr

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