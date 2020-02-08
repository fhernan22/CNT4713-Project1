#!/usr/bin/env python3

import sys
import socket
import signal
import os
from _thread import *
import threading
import struct

HOST = '0.0.0.0'
establishedConnections = 0

def receiveSignal(signalNumber, frame):
    print('Exiting server with signanl number:', signalNumber)
    sys.exit(0)


def clientThreaded(conn, addr, connNum):
    conn.settimeout(10)

    with open(os.path.join(os.getcwd(), sys.argv[2], str(connNum) + '.file'), 'wb') as f:

        try:
            data = conn.recv(1024)

            while data:
                f.write(data)
                data = conn.recv(1024)

            conn.close()

        except socket.timeout as e:
            sys.stderr.write('ERROR: {}'.format(e))
            f.write('ERROR'.encode())
            sys.exit(1)



def main():
    try:
        if int(sys.argv[1]) > 1023:
            PORT = int(sys.argv[1])
        else:
            PORT = 'n/a'
            sys.stderr.write('ERROR: Port number must be greater than 1023\n')
            sys.exit(1)
    except IndexError:
        sys.stderr.write('ERROR: Port number must be supplied on the command line\n')
        sys.exit(1)
    except ValueError:
        sys.stderr.write('ERROR: Port number must be an integer\n')
        sys.exit(1) 

    if not os.path.exists(sys.argv[2]):
        os.mkdir(sys.argv[2], mode = 0o777) 

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        sys.stderr.write('ERROR: {}\n'.format(e))
        sys.exit(1)

    try:
        sock.bind((HOST, PORT))
        print("Server running on " + str(HOST) +  ":" + str(PORT))

        sock.listen(5)

        while True:
            conn, addr = sock.accept()
            global establishedConnections
            establishedConnections += 1
            print(establishedConnections)

            print('Connection to :', addr[0], ':', addr[1])


            start_new_thread(clientThreaded, (conn, addr, establishedConnections,)) 

        sock.close()

    except socket.error as e:
        sys.stderr.write('ERROR:{}\n'.format(e))
        sys.exit(1)
    
    except KeyboardInterrupt as e:
        sys.stderr.write('Shutting down server...\n')
        sys.exit(0)




if __name__ == '__main__':
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGTERM, receiveSignal)
    main()
