# Yacc Parser

import ply.yacc as yacc
import homeFunctions
# Get the token map from the lexer.  This is required.
from homeLex import tokens


def p_STATUS(p):
    'expression : STATUS'
    #print('status found')
    homeFunctions.print_home()


def p_ROOMS(p):
    'expression : ROOMS'
    print('rooms found')

def p_EXIT(p):
    'expression : EXIT'
    print('Saving State')
    homeFunctions.write_home()
    print('Saved, now exiting')
    exit()

def p_ROOMS(p):
    'expression : ROOMS'
    try:
        homeFunctions.print_rooms()
    except KeyError:
        print('No rooms configured yet. Please add a room first')
def p_print_room_status_devices(p):
    'expression : ROOM PARAMETER STATUS'
    homeFunctions.print_room_status_devices(p[2])
def p_print_room_status_device(p):
    'expression : ROOM PARAMETER STATUS PARAMETER'
    homeFunctions.print_room_status_device(p[2], p[4])
def p_add_device(p):
    'expression : ADD DEVICE PARAMETER PARAMETER'
    homeFunctions.add_device_to_room(p[3],p[4])

def p_remove_device(p):
    'expression : REMOVE DEVICE PARAMETER PARAMETER'
    homeFunctions.remove_device_from_room(homeFunctions.home, p[3], p[4])
def p_remove_room(p):
    'expression : REMOVE ROOM PARAMETER'
    homeFunctions.remove_room(homeFunctions.home,p[3])

def p_add_room(p):
    'expression : ADD ROOM PARAMETER'
    homeFunctions.create_room(homeFunctions.home,p[3])
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input! Go to URL for allowed instructions.")

def p_print_room_devices(p):
    'expression : ROOM PARAMETER DEVICES'
    homeFunctions.print_room_devices(p[2])
# Build the parser
parser = yacc.yacc()

