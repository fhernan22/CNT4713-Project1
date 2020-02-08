#!/usr/bin/env python3

import socket
import sys
import os


def main():
    try:
        HOST = sys.argv[1]
    except IndexError:
        sys.stderr.write('ERROR: Host name or IP address must be supplied on the command line\n')
        sys.exit(1)

    try:
        if int(sys.argv[2]) > 1023:
            PORT = int(sys.argv[2])
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

  
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

        sock.settimeout(10)

        sock.connect((HOST,PORT)) 


        with open(sys.argv[3], "rb") as f:

            segment = f.read(1024)

            while segment: 

                sock.send(segment) 
    
                segment = f.read(1024)
            
            # close the connection 
            sock.close()

    except socket.error as e:
        sys.stderr.write('ERROR: {}\n'.format(e))
        sys.exit(1)

    except socket.timeout as e:
        sys.stderr.write('ERROR: {}\n'.format(e))
        sys.exit(1)


if __name__ == '__main__':
    main()
