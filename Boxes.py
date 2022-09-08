from rply.token import BaseBox
import csv
import os
"""
# MainBox (todo)
    # ActionsBox (Todas las líneas de código)
        # ActionsBox
            # ...
        # FunctionBox
            # ...
    # FunctionBox (Linea de código hasta el ';')
        # IdBox (usr_id, ac_id, item_id)
        # BooleanBox (T/F)
        # MoneyBox ($$$)
        # ...
"""
on_memory_file = None

class MainBox(BaseBox):#Contiene FunctionBox a ser evaluadas
    def __init__(self, actionsBox, functionBox):
        self.actionsBox = actionsBox
        self.functionBox = functionBox
    
    def eval(self):
        for actions in self.actionsBox.getlist():
            x = actions.eval()
            for i in range(x):
                for action in self.actionsBox.getlist():
                    action.eval()

class ActionsBox(BaseBox):
    def __init__(self, actionsBox=None, functionBox=None):
        self.actionsBox = actionsBox
        self.functionBox = functionBox

    def getlist(self):
        if self.actionsBox:
            return self.actionsBox.getlist() + [self.functionBox]
        else:
            return []

class IdBox(BaseBox):
    def __init__(self, idBox):
        self.idBox = idBox
    
    def eval(self):
        try:
            return self.idBox.getstr()
        except:
            return None

class BooleanBox(BaseBox):
    def __init__(self, booleanBox):
        self.booleanBox = booleanBox
    
    def eval(self):
        if self.booleanBox in ['T','t','1','True']:
            return True
        elif self.booleanBox in ['F','t','0','False']:
            return False
        else:
            return False

class MoneyBox(BaseBox):
    def __init__(self, moneyBox):
        self.moneyBox = moneyBox
    
    def eval(self):
        try:
            return float(self.moneyBox)
        except:
            return None

class StateBox(BaseBox):
    def __init__(self, stateBox):
        self.stateBox = stateBox

    def getstr(self):
        if self.stateBox in ['zero', 'positive', 'negative']:
            return self.stateBox.getstr()

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

