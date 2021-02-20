import socket
import sys
import json
import keyboard
import traceback

base_value = None
EPS = 1.5
KEY = 'c'

# interprets the values and returns a key press button
def key_interpreter(value):
    global base_value
    global EPS
    global KEY

    if (base_value and value - base_value > EPS):
        print('Triggered', value, base_value)
        keyboard.send(KEY)

def processJSON(line):
    global base_value
    
    try:
        sensor_dict = json.loads(line)
        accel = sensor_dict['accelerometer']
        values = accel['value']

        key_interpreter(values[1])
        base_value = values[1]
    
    except json.decoder.JSONDecodeError:
        pass


def printToFile(line, fileHandle):
    sensor_dict = json.loads(line)
    accel = sensor_dict['accelerometer']
    timestamp = accel['timestamp']
    values = accel['value']

    formattedString = "{} {} {} {}\n".format(timestamp, values[0], values[1], values[2])
    fileHandle.write(formattedString)


def startServer(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()

        while (True):
            print("Waiting for connection at port", port)
            conn, addr = s.accept()
            with conn:
                print('Connected to', addr)

                while (True):
                    data = conn.recv(1024)
                    if not data:
                        break
                    res = str(data, 'utf-8')
                    lines = res.splitlines()
                    for string in lines:
                        processJSON(string)
                        # print(string)



if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
        startServer(port)
    except ValueError:
        print("Invalid port specified")
        traceback.print_exc()
    except IndexError:
        print("Wrong number of arguments specified")
