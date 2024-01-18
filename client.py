#Done by: Yusuf Abdulnoor saeed, 202100829
#Done by: Ali Mohammed Alasfoor, 202100850


import socket
from prettytable import PrettyTable

#creating the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#teying to establish connection with the server.
try:
    client_socket.connect(('127.0.0.1',7779))
except:
    print("could not connect to the server")
    exit(0) 


#creating the table
Table = PrettyTable(["Client_name"])


#Enter the client name
Client_name = input("Enter your name: ")
#Send the client name to the server
Client_name = Client_name.encode('utf-8')
client_socket.sendall(Client_name)


#fnn to decoding and printing the data
def Display_data(data):
    Data = data.decode('utf-8')
    print(Data)


while True:

    try:
        print("\n Choose one option:")
        print("1.Display arrived flights")
        print("2.Display delayed flights")
        print("3.Display flights from one specific city")
        print("4.Display details from one particular flight")
        print("5.Quit")
        option = input("Enter your selection: ")
    
	#Display arrived flights
        if option == "1":
            opt="a"
            client_socket.sendall(opt.encode('utf-8'))
            data = client_socket.recv()
            Display_data(data)
	
	#Display delayed flights
        elif option == "2":
            opt="b"
            client_socket.sendall(opt.encode('utf-8'))
            data = client_socket.recv()
            Display_data(data)
            opt2=input()
            client_socket.sendall(opt2.encode('utf-8'))
            data2 = client_socket.recv()
            Display_data(data2)
	
	#Display flights from one Specific City
        elif option == "3":
            opt="c"
            client_socket.sendall(opt.encode('utf-8'))
            city = input("Enter city code: ")
            client_socket.sendall(city.encode('utf-8'))
            data = client_socket.recv()
            Display_data(data)

	#Display details of one specific flight
        elif option == "4":
            opt="d"
            client_socket.sendall(opt.encode('utf-8'))
            flight = input("enter flight IATA:")
            client_socket.sendall(flight.encode('utf-8'))
            data = client_socket.recv()
            Display_data(data)
	
	#Closing the connection
        elif option == "5":
            opt="e"
            client_socket.sendall(opt.encode('utf-8'))
            print("Connection with server is closed")
            print("see ya!")
            client_socket.close()
            break
   
        else:
            print("Invalid option")
            
    except:
        print("Error establishing connection")
        break
    
        
	    
