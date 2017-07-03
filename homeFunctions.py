from pprint import pprint
import json

#Read file into device variable and print
def open_home():
    home_file=open("home.txt", "r")
    global home
    try:
        home= dict(json.loads(home_file.read()))
        pprint(home)
    except:
        home={}
    pprint(home)
    file_output=json.dumps(home)
    home_file.close()

def write_home():
    home_file = open('home.txt', "w")
    home_file.write(json.dumps(home))
    home_file.close()
def create_device(devices, name):
    devices[name]={
        'name':name,
        'powered': False,
        'time_off':'',
        'time_on':''
    }

def create_room(home, room_name):
    try:
        home['rooms'][room_name]={}
    except KeyError:
        home['rooms']={}
        home['rooms'][room_name]={}


def rename_home(home,name):
    home['name']=name

def print_rooms():
    pprint(home['rooms'])

def print_home():
    pprint(home)

def remove_device_from_room(home,room_name, device_name):

    if device_name in  home['rooms'][room_name]:
        del home['rooms'][room_name][device_name]
        print('Device', device_name, 'has been deleted')
    else:
        print('Device does not exist or is not in specified room.')

def remove_room(home,room_name):

    if room_name in  home['rooms']:
        del home['rooms'][room_name]
        print('Room', room_name, 'has been deleted')
    else:
        print('Room does not exist.')

def print_room_devices(room_name):
    try:
        if len(home['rooms'][room_name])==0:
            print('No devices in the room')
        else:
            pprint(home['rooms'][room_name])
    except KeyError:
        print('Room name specified does not exist.')
def print_room_status_devices(room_name):
    try:
        if len(home['rooms'][room_name])==0:
            print('Room has no devices. Please add devices to see their status.')
        else:
            for device in home['rooms'][room_name].values():
                print(device['name'],' is ', device['powered'])
    except KeyError:
        print('Room name does not exist or is invalid.')
def print_room_status_device(room_name, device_name):
    if len(home['rooms'][room_name])==0:
        print('Room has no devices. Please add devices to see their status.')
    else:
        if home['rooms'][room_name][device_name]['powered']:
            powered_status='ON'
        else:
            powered_status='OFF'
        print(home['rooms'][room_name][device_name]['name'],' is ',powered_status)


def add_device_to_room(room_name,device_name):
    try:
        create_device(home['rooms'][room_name],device_name)
    except KeyError:
        print('Room name specified does not exist.')