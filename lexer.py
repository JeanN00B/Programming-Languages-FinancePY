#==============================================#
#Lexer generator for "FinancePY"
#   1. Scanner (lexical annalysis)
#   2. Token stream
#   3. Parser (syntatic analysis)
#   4. Parse treee
#   5. Semantic anaylsis and code generation
#   6. Abstract syntaxt tree
#   7. ? backend stuff....
#==============================================#
from rply import LexerGenerator
from rply.token import BaseBox

#list of tokens
tokens = LexerGenerator()

#Ignore whitespace and comments
tokens.ignore(r'[ \t\r\f\v]+')
tokens.ignore(r'#[^\n]*\n')
tokens.ignore(r'\n')

#Users and Groups attributes
#and functions
tokens.add('SETTLE_ACC', r'SETTLE_ACC(?!\w)')
tokens.add('BALANCE', r'BALANCE(?!\w)')
tokens.add('ITEM', r'ITEM(?!\w)')
tokens.add('SEARCH_U', r'SEARCH_U(?!\w)')
tokens.add('NEW_GROUP', r'NEW_G(?!\w)')
tokens.add('READ_GROUP', r'READ_G(?!\w)')
tokens.add('ADD_USER', r'ADD_USR(?!\w)')
tokens.add('INVENTORY', r'INVENTORY(?!\w)')
tokens.add('DEPOSIT', r'DEPOSIT(?!\w)')

tokens.add('ZERO', r'zero(?!\w)')
tokens.add('POSITIVE', r'positive(?!\w)')
tokens.add('NEGATIVE', r'negative(?!\w)')

#Data types
tokens.add('ID_USR_ACC', r'("[a-zA-Z_\s]+[a-zA-Z](?!\w)")|(\'[a-zA-Z_\s]+[a-zA-Z](?!\w)\')')
tokens.add('STRING', r'(".?")|(\'.?\')')
tokens.add('MONEY', r'(-?\d+.\d\d)|(-?\d+.\d)|(-?\d+)')
tokens.add('BOOLEAN', r'(T)|(F)|(t)|(f)|(0)|(1)|(True)|(False)')

#Structure punctuation
tokens.add('SEMICOLON', r';')
tokens.add('COMMA', r',')
tokens.add('(', r'\(')
tokens.add(')', r'\)')


lexer = tokens.build()

#EXAMPLE OF THE GRAMMAR
#for token in lexer.lex('#this is a comment\n NEW_G("success");\n NEW_G("successxd");'):
#    print(token) #works!