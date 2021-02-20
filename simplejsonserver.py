import socket
import sys
import json

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
                    json_data = json.loads(res)
                    print(res)



if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
        startServer(port)
    except ValueError:
        print("Invalid port specified")
    except IndexError:
        print("Wrong number of arguments specified")
