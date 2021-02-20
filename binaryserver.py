import socket
import sys

def startServer(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()

        while (True):
            print("Waiting for connection at port", port)
            conn, addr = s.accept()
            with conn:
                print('Connected to', addr)
                values = []
                inProgress = False
                while (True):
                    data = conn.recv(1024)
                    if not data:
                        break

                    print(data)
                    # for i in range(0, len(data)):
                    #     if (inProgress):
                    #         values.append(data[i])

                    #     if (data[i] == 128):
                    #         inProgress = not inProgress
                    #         if (not inProgress):
                    #             print(values)
                    #             inProgress = True
                    #             values = []



if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
        startServer(port)
    except ValueError:
        print("Invalid port specified")
    except IndexError:
        print("Wrong number of arguments specified")
