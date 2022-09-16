# Programming Languages - FinancePY
 A domain specific language (DSL) based on Python that is oriented on carry groupal economy
  * Easy to use.
  * Helps to handle accounts between multiple persons.
  * Simple syntax to learn.
  
 See the "FinancePY.pdf" for more details over how the language was created and a deep description of the operations and how they works.

# Documentation
## Language variables Types:
 * ID tokens: any string of letters, can include underscores symbols, used to represent accounts and users names.
 * Strings: any string of symbols, used to represent items names.
 * Money: any float number that is composed by an integer followed by zero, one or two decimals.
 * Boolean: tag of true or false for, used to say if an item has or not takes included.
 * State token: a group of tags that are used to display the users with zero money, positive balance or negative balance.
 
## Opetations structures:
 * NEW_GROUP('group_id');
 * READ_GROUP('group_id');
 * ADD_USER('user_id');
 * DEPOSIT('user_id', money);
 * ITEM('user_id', 'item_id', money, boolean);
 * BALANCE(<zero, positive or negative>);
 * INVENTORY('user_id');
 * SETTLE_ACC();
