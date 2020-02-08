Name:   Fidel Hernandez
PID:    6045594

#Server:

#create global variable counter that increments every time a new connection is established

#Check if the port provided as command line argument is valid:
    #if it's not throw an error
    #If it is save it in a varible

#Try to bind HOST and PORT
    #Then as long as we have incoming connections:
        #Accept them
        #increment the counter
        #start a new thread that does the following:
            #listen if no data has been received from the client for 10 seconds
            #creates a file to write to in path specified by user/number of established connections.file
            #then while data is been sent from the client:
                #write that data to the created file
            #close connection
        #close socket


#Client:

#Validate Host and Port provided by user

#Try to connect to the specified host and port and set a timeout for 10 seconds

#open the file passed in as a command line 

#Then while the file file hasn't been transferred completely:
    #keep transfering the file to the server

#Close the socket


I used code I found on https://www.geeksforgeeks.org/socket-programming-multi-threading-python/ 
as starting point to understand multithreading in python. But I heavily modified this code to satisfy
my needs.



