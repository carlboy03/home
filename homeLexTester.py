import homeLex as homeLex

def printout_test(testing_array):
    for item in testing_array.values():
        homeLex.lexer.input(item)
        # Tokenize
        while True:
            tok = homeLex.lexer.token()
            if not tok:
                break      # No more input
            print(tok)
#lexer.input("OKAY 3")
testing_array={
    'status':'STATUS',
    'rooms': 'ROOMS',
    'room': 'ROOM',
    'add': 'ADDs',
    'device': 'DEVICE',
    'remove': 'REMOVE',
    'move': 'MOVE',
    'edit': 'ADDIN',
    'home': 'HOME',
    'timer': 'TIMER'
}

printout_test(testing_array)
# Testing of full statements

testing_array={
    'rooms': 'rooms'
}
print("\nExpected: LexToken(ROOMS,'rooms',1,0)")
printout_test(testing_array)
testing_array={'room': 'room bedroomname devices'}
print("\nExpected: LexToken(ROOM,'room',1,0), LexToken(PARAMETER, 'bedroom', 1, 5) LexToken(DEVICES, 'devices', 1, 17)")
printout_test(testing_array)

testing_array={'room': 'status'}
print("\nExpected: LexToken(STATUS,'status',1,0)")
printout_test(testing_array)

testing_array={'room': 'room bedroomname status'}
print("\nExpected: LexToken(ROOM,'room',1,0), LexToken(PARAMETER, 'bedroomname', 1, 5) LexToken(STATUS, 'status', 1, 17)")
printout_test(testing_array)

testing_array={'room': 'room bedroomname status devicename'}
print("\nExpected: LexToken(ROOM,'room',1,0), LexToken(PARAMETER, 'bedroomname', 1, 5) LexToken(STATUS, 'status', 1, 17) LexToken(PARAMETER, 'devicename', 1, 23)")
printout_test(testing_array)

testing_array={'room': 'add room bedroomname'}
print("\nExpected: LexToken(ADD,'add',1,0), LexToken(ROOM, 'room', 1, 5) LexToken(PARAMETER, 'bedroomname', 1, 17) LexToken(PARAMETER, 'devicename', 1, 23)")
printout_test(testing_array)
testing_array={'room': 'add device bedroomname devicename'}
print("\nExpected: LexToken(ADD,'add',1,0), LexToken(device, 'room', 1, 5) LexToken(PARAMETER, 'bedroomname', 1, 17) LexToken(PARAMETER,'devicename', 1, X) ")
printout_test(testing_array)


testing_array={'room': 'remove room bedroomname '}
print("\nExpected: LexToken(REMOVE,'remove',1,0), LexToken(ROOM, 'room', 1, 5) LexToken(PARAMETER, 'bedroomname', 1, 17)")
printout_test(testing_array)


testing_array={'room': 'move device devicename bedroomold bedroomnew '}
print("\nExpected: LexToken(MOVE,'move',1,0), LexToken(DEVICE, 'device', 1, 5)  LexToken(PARAMETER, 'devicename', 1, 17) LexToken(PARAMETER, 'bedroomold', 1, 17) LexToken(PARAMETER, 'bedroomnew', 1, X)")
printout_test(testing_array)

testing_array={'room': 'edit room roomname newroomname'}
print("\nExpected: EDIT: edit, ROOM: room, PARAMETER: roomname, PARAMETER:newroomname")
printout_test(testing_array)

testing_array={'room': 'edit device roomname devicename newdevicename'}
print("\nExpected: EDIT:edit, DEVICE:device PARAMETER:roomname PARAMETER:devicename PARAMETER:devicenewname")
printout_test(testing_array)


testing_array={'room': 'home on'}
print("\nExpected: HOME: home, ON: on")
printout_test(testing_array)


testing_array={'room': 'room roomname on'}
print("\nExpected: ROOM: roomname, PARAMETER:roomname, ON: on")
printout_test(testing_array)


testing_array={'room': 'device roomname devicename on'}
print("\nExpected: DEVICE: device, PARAMETER:roomname, PARAMETER: devicename, ON:on")
printout_test(testing_array)


testing_array={'room': 'timer on roomname devicename'}
print("\nExpected: TIMER: timer, ON:on, PARAMETER:roomname, PARAMETER:devicename")
printout_test(testing_array)

