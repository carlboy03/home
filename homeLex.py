# ------------------------------------------------------------
# homeLex.py
# ------------------------------------------------------------
import ply.lex as lex


reserved ={
'status': 'STATUS',
    'rooms': 'ROOMS',
    'room': 'ROOM',
    'add': 'ADD',
    'device': 'DEVICE',
    'remove': 'REMOVE',
    'move': 'MOVE',
    'edit': 'EDIT',
    'home': 'HOME',
    'timer':'TIMER',
    'devices':'DEVICES',
    'on': 'ON',
    'off': 'OFF',
    'exit': 'EXIT'

}
# List of token names. This is always required
tokens = [
    'NUMBER',
    'RESERVED',
    'PARAMETER'
]+list(reserved.values())

# Regular expression rules for simple tokens
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_ROOMS(t):
    r'[R][O][O][M][S]'
    return t

def t_ROOM(t):
    r'[R][O][O][M]'
    return t


def t_STATUS(t):
    r'[S][T][A][T][U][S]'
    return t

def t_ADD(t):
     r'[A][D][D]'
     return t

def t_DEVICES(t):
    r'[D][E][V][I][C][E][S]'
    return t

def t_DEVICE(t):
    r'[D][E][V][I][C][E]'
    return t


def t_REMOVE(t):
    r'[R][E][M][O][V][E]'
    return t

def t_MOVE(t):
    r'[M][O][V][E]'
    return t

def t_EDIT(t):
    r'[E][D][I][T]'
    return t

def t_HOME(t):
    r'[H][O][M][E]'
    return t

def t_TIMER(t):
    r'[T][I][M][E][R]'
    return t

def t_PARAMETER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'PARAMETER')    # Check for reserved words
    return t
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

