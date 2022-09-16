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
        if self.booleanToken.getstr() in ['T', 't', 'True','true']:
            return True
        elif self.booleanToken.getstr() in ['F', 'f', 'False','false']:
            return False

class FunctionBox(BaseBox):
    def __init__(self, functionBox):
        self.functionBox = functionBox
    def eval(self):
        return self.functionBox.getstr()

class ActionBox(BaseBox):
    def __init__(self, functionNameBox, stateBox=None, textBox1=None, textBox2=None, moneyBox=None, booleanBox=None):
        self.functionNameBox = functionNameBox
        self.stateBox = stateBox    # state
        self.textBox1 = textBox1    # usr | acc | usr |
        self.textBox2 = textBox2    # ___ | ___ | str |
        self.moneyBox = moneyBox
        self.booleanBox = booleanBox
    def eval(self):
        global on_memory_file

        if self.functionNameBox == "NEW_GROUP":
            #NEW_GROUP -->  self.textBox1 = acc | self.textBox2 = None
            #Create a new group
            try:
                with open(self.textBox1, mode='x') as account: #Mode x creates strictly a new file
                    account_string = csv.writer(account, delimiter=',', quotechar='"')
                    account_string.writerow(['*****'])
                    account_string.writerow(['FILENAME', self.textBox1])
                    account_string.writerow(['USERS']) #Possible to modify to the right
                    account_string.writerow(['MONEY'])
                    account_string.writerow(['BALANCE','T'])
                    account_string.writerow(['*****'])
                    account_string.writerow(['USER ID', 'ITEM ID', 'VALUE', 'TAXES']) #Possible to modify bellow
                on_memory_file = self.textBox1
            except:
                print("ERROR! file already exist on current directory")
                pass

        elif self.functionNameBox == 'READ_GROUP':
            # READ_GROUP(acc_id) --> self.textBox1 = acc | self.textBox2 = None
            # Return acc_id to be readed globally
            if str(self.textBox1) in os.listdir('.'):
                on_memory_file = self.textBox1
                return on_memory_file
            else:
                print('ERROR! no such file "{}" on the current directory'.format(self.textBox1))
                on_memory_file = None
        
        elif self.functionNameBox == 'ADD_USER':
            if on_memory_file != None:
                #Here we read and copy all
                with open(on_memory_file, mode="r") as file:
                    read_f = csv.reader(file)
                    tmp = [] #store info temporally
                    for lines in read_f:
                        tmp.append(lines)
                    for rows in range(len(tmp)):
                        if tmp[rows][0] == "USERS":
                            if self.textBox1 in tmp[rows]:
                                print('ERROR! user "{}" already exist!'.format(self.textBox1))
                                return None
                            else:
                                tmp[rows].append(self.textBox1)
                                tmp[rows+1].append(str(self.moneyBox))
                        if tmp[rows][0] == "BALANCE":
                            tmp[rows][1] == False
                #Here we write the appended list
                with open(on_memory_file, mode='w') as file:        
                    write_f = csv.writer(file)
                    for lines in tmp:
                        write_f.writerow(lines)
            else:
                print("ERROR! No previous name charged on memory! to read an existing file use READ_GROUP(arg);")

        elif self.functionNameBox == 'ITEM':
            if self.booleanBox == None:
                self.booleanBox = False
            with open(on_memory_file, mode='r') as file:
                read_f = csv.reader(file)
                tmp = []
                for rows in read_f:
                    tmp.append(rows)
                for rows in range(len(tmp)):
                    if tmp[rows][0] == "USERS":
                        if self.textBox1 not in tmp[rows]:
                            print('ERROR! user "{}" is not registered on this account!'.format(self.textBox1))
                            return None
                        elif float(tmp[rows+1][tmp[rows].index(self.textBox1)]) <= 0:
                            print('ERROR! user "{}" has run out of money and/or is on negative values already!'.format(self.textBox1))
                        else:
                            tmp[rows+1][tmp[rows].index(self.textBox1)] = round(float(tmp[rows+1][tmp[rows].index(self.textBox1)]) - float(self.moneyBox), 2)
                            tmp[rows+2][1] = False #Balance set to false
                            with open(on_memory_file, mode='w') as file:        
                                write_f = csv.writer(file)
                                for lines in tmp:
                                    write_f.writerow(lines)
                                            
                            with open(on_memory_file, mode='a') as file:
                                write_f = csv.writer(file)
                                write_f.writerow([self.textBox1, self.textBox2, self.moneyBox, self.booleanBox])

        elif self.functionNameBox == 'SETTLE_ACC':
            #1st: see if there are users and how much they spent.
            if on_memory_file != None:
                print("\nCalculating how much money each user needs to recieve/give (negative values are who give and positive who recieve)")
                with open(on_memory_file, mode="r") as file:
                    read_f = csv.reader(file)
                    tmp = [] #store FILE info temporally
                    for lines in read_f:
                        tmp.append(lines)
                    for rows in range(len(tmp)):
                        if tmp[rows][0] == "USERS":
                            spent_money_by_usr = []
                            actual_money_by_usr = [] #store this data to calculate final output and print.
                            users_list = []
                            for i in range(1,len(tmp[rows])):
                                users_list.append(tmp[rows][i])
                                actual_money_by_usr.append(tmp[rows+1][i])#next row that are money values
                        ###################
                                money = 0
                                for users in range(len(tmp)):#check in the inventory for all users that matches
                                    if (tmp[users][0] == tmp[rows][i]) and (tmp[users][3] == "False"):
                                        money = money + float(tmp[users][2])
                                    elif (tmp[users] == tmp[rows][i]) and (tmp[users][3] == "True"):
                                        money = money + float(tmp[users][2]) + float(tmp[users][2])*0.12 # add IVA 12%
                                spent_money_by_usr.append(money) #stored all the data as "i" users are on the account
                        ###################
            #2nd: Users and money are stored {DONE}
            # OPERATIONS to calculate the differential and the differential itself.
                differential_calculated = 0
                for values in range(len(spent_money_by_usr)):
                    differential_calculated += spent_money_by_usr[values]
                differential_calculated = differential_calculated/len(users_list)
            #PRINT data
                settled_money_values = []
                for i in range(len(actual_money_by_usr)):
                    settled_money_values.append(float(actual_money_by_usr[i]) - differential_calculated + float(spent_money_by_usr[i]))
                print("USERS: {}".format(users_list))
                print("MONEY BEFORE SETTLE OPERATION: {}".format(actual_money_by_usr))
                print("SETTLED VALUES: {}".format(settled_money_values))
                print("The account is settled now!")
            #3rd MODIFY original document to settle the account and set actual money values
                for rows in range(len(tmp)):
                    if tmp[rows][0] == "MONEY":
                        for i in range(1,len(settled_money_values)):
                            tmp[rows][i] = settled_money_values[i]
                        tmp[rows+1][1] = True #balanced acc
                        pass
                    pass
                
                with open(on_memory_file, mode='w') as file:        
                    write_f = csv.writer(file)
                    for lines in tmp:
                        write_f.writerow(lines)
            else:
                print("ERROR! No previous name charged on memory! to read an existing file use READ_GROUP(arg);")

        elif self.functionNameBox == 'BALANCE':
            if on_memory_file != None:
                #recive zero, positive or negative.
                with open(on_memory_file, mode="r") as file:
                    read_f = csv.reader(file)
                    tmp = [] #store info temporally
                    for lines in read_f:
                        tmp.append(lines)
                    for rows in range(len(tmp)):
                        if tmp[rows][0] == "MONEY":
                            users_list = []
                            money_list = []
                            if self.stateBox == "zero":
                                for i in range(1,len(tmp[rows])):
                                    if float(tmp[rows][i]) == 0:
                                        users_list.append(tmp[rows-1][i])
                                        money_list.append(tmp[rows][i])
                            elif self.stateBox == "positive":
                                for i in range(1,len(tmp[rows])):
                                    if float(tmp[rows][i]) > 0:
                                        users_list.append(tmp[rows-1][i])
                                        money_list.append(tmp[rows][i])
                            elif self.stateBox == "negative":
                                for i in range(1,len(tmp[rows])):
                                    if float(tmp[rows][i]) < 0:
                                        users_list.append(tmp[rows-1][i])
                                        money_list.append(tmp[rows][i])
                            else:
                                print("ERROR! unexpected state token")
                            print("Accounts with <{}> balance on the account:".format(self.stateBox))
                            print("{}\n{}".format(users_list,money_list))
            else:
                print("ERROR! No previous name charged on memory! to read an existing file use READ_GROUP(arg);")
                                
        elif self.functionNameBox == 'INVENTORY':
            if on_memory_file != None:
                #if usr on file, return every buyed items ELSE return error.
                with open(on_memory_file, mode="r") as file:
                    read_f = csv.reader(file)
                    tmp = [] #store info temporally
                    for lines in read_f:
                        tmp.append(lines)
                    if (tmp[2][0] == "USERS") and (self.textBox1 in tmp[2]):
                        print("User {} inventory on current account:".format(self.textBox1))
                        print("ITEM | VALUE | TAXES")
                        for rows in range(len(tmp)):
                            if tmp[rows][0] == self.textBox1:
                                print("{} | {} | {}".format(tmp[rows][1], tmp[rows][2], tmp[rows][3]))
                    else:
                        print("ERORR! User does not exist on current account!")

            else:
                print("ERROR! No previous name charged on memory! to read an existing file use READ_GROUP(arg);")

        elif self.functionNameBox == 'DEPOSIT':
            if on_memory_file != None:
                #usr id + money
                with open(on_memory_file, mode="r") as file:
                    read_f = csv.reader(file)
                    tmp = [] #store info temporally
                    for lines in read_f:
                        tmp.append(lines)
                    if self.textBox1 not in tmp[2]:
                        print("ERROR! User is not registered on this account.")
                    else:
                        tmp[3][tmp[2].index(self.textBox1)] = round(float(tmp[3][tmp[2].index(self.textBox1)]) + float(self.moneyBox),2)
                        print(tmp[3][tmp[2].index(self.textBox1)])
                #Write time!
                with open(on_memory_file, mode='w') as file:        
                    write_f = csv.writer(file)
                    for lines in tmp:
                        write_f.writerow(lines)
            else:
                print("ERROR! No previous name charged on memory! to read an existing file use READ_GROUP(arg);")

        elif self.functionNameBox == None:
            print("ERROR! unexpected function on input")
