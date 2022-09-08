import csv
import os
###################################################
on_memory_file = None #acc_id on global use.
###################################################

# NEW_GROUP(acc_id)
# Create a file with the structure of the example, but empty
def NEW_GROUP(acc_id):
    with open(acc_id, mode='x') as account: #Mode x creates strictly a new file
        account_string = csv.writer(account, delimiter=',', quotechar='"')
        account_string.writerow(['*****'])
        account_string.writerow(['FILENAME', acc_id])
        account_string.writerow(['USERS']) #Possible to modify to the right
        account_string.writerow(['MONEY'])
        account_string.writerow(['BALANCE','T'])
        account_string.writerow(['*****'])
        account_string.writerow(['USER ID', 'ITEM ID', 'VALUE', 'TAXES']) #Possible to modify bellow

    global on_memory_file
    on_memory_file = acc_id


# ADD_USER(usr_id)
# If 'usr_id' on 'acc_id', return ERROR! and continue script
def ADD_USER(usr_id, money=0):
    global on_memory_file
    #Here we read and copy all
    with open(on_memory_file, mode="r") as file:
        read_f = csv.reader(file)
        tmp = [] #store info temporally

        for lines in read_f:
            tmp.append(lines)
        for rows in range(len(tmp)):
            if tmp[rows][0] == "USERS":
                if usr_id in tmp[rows]:
                    print('ERROR! user "{}" already exist!'.format(usr_id))
                    return None
                else:
                    tmp[rows].append(usr_id)
                    tmp[rows+1].append(money)
            if tmp[rows][0] == "BALANCE":
                tmp[rows][1] == False
    #Here we write the appended list
    with open(on_memory_file, mode='w') as file:        
        write_f = csv.writer(file)
        for lines in tmp:
            write_f.writerow(lines)


# ITEM(usr_id, item_id, tax_bool)
# Append to the account a new item with a user, value associated
def ITEM(usr_id, item_id, money, tax_bool=False):
    global on_memory_file
    with open(on_memory_file, mode='r') as file:
        read_f = csv.reader(file)
        tmp = []
        for rows in read_f:
            tmp.append(rows)
        for rows in range(len(tmp)):
            if tmp[rows][0] == "USERS":
                if usr_id not in tmp[rows]:
                    print('ERROR! user "{}" is not registered on this account!'.format(usr_id))
                    return None
                elif float(tmp[rows+1][tmp[rows].index(usr_id)]) <= 0:
                    print('ERROR! user "{}" has run out of money and is on negative values already!'.format(usr_id))
                else:
                    tmp[rows+1][tmp[rows].index(usr_id)] = round(float(tmp[rows+1][tmp[rows].index(usr_id)]) - float(money), 2)
                    tmp[rows+2][1] = False #Balance set to false
                    with open(on_memory_file, mode='w') as file:        
                        write_f = csv.writer(file)
                        for lines in tmp:
                            write_f.writerow(lines)
                                    
                    with open(on_memory_file, mode='a') as file:
                        write_f = csv.writer(file)
                        write_f.writerow([usr_id, item_id, money, tax_bool])


# READ_GROUP(acc_id)
# Return acc_id to be readed globally
def READ_GROUP(acc_id):
    #check if 'acc_id' exist on execution path
    #is exist, return 'acc_id' on_memory_file
    #else return None
    global on_memory_file 
    if acc_id in os.listdir('.'):
        on_memory_file = acc_id
        return on_memory_file
    else:
        print('ERROR! no such file "{}" on the current directory'.format(acc_id))
        on_memory_file = None


# INVENTORY(usr_id)
# Search for the 'ITEM_ID', 'VALUE', associated to a 'USR_ID' on a GROUP
def INVENTORY(usr_id):
    return None



#on_memory_file = "test2.csv"
#NEW_GROUP('test.csv')
#READ_GROUP("test2.csv")
#ADD_USER('user8', 55)
#ITEM('user2', 'brownies', 12.50)
