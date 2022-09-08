import functions as fpy

fpy.NEW_GROUP("Script Example.csv")
fpy.READ_GROUP("Script Example.csv")

fpy.ADD_USER('user1', 7.50)
fpy.ADD_USER('user2', 3.1)
fpy.ADD_USER('user3', 12.30)
fpy.ADD_USER('user4')
fpy.ADD_USER('user5')
fpy.ADD_USER('user6', 5)
fpy.ADD_USER('user7', 5)
fpy.ADD_USER('user8', 55)

fpy.ITEM("user8",	"papas", 3.5)
fpy.ITEM("user8",	"papas", 3.5)
fpy.ITEM("user8",	"papas", 3.5)
fpy.ITEM("user1", "item1", 2, True)
fpy.ITEM("user1", "item2", 2, False)
fpy.ITEM("user3",	"item1", 3, True)
fpy.ITEM("user3",	"item3", 1.4, True)
fpy.ITEM("user3",	"item4", 1.4, True)
fpy.ITEM("user3",	"item5", 3)
fpy.ITEM("user3",	"item1", 4)


#SETTLE_ACC(None)
#BALANCE(<zero, positive, negative>)
#SEARCH_U("USR_ID")
#fpy.INVENTORY("USR_ID")
#DEPOSIT("USR_ID", "MONEY")
